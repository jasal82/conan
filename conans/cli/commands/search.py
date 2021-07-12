from conans.cli.command import conan_command, Extender, COMMAND_GROUPS
from conans.cli.commands.list import list_recipes_cli_formatter, json_formatter


search_formatters = {
    "cli": list_recipes_cli_formatter,
    "json": json_formatter
}


@conan_command(group=COMMAND_GROUPS['consumer'], formatters=search_formatters)
def search(conan_api, parser, *args, **kwargs):
    """
    Searches for package recipes in a remote or remotes
    """
    parser.add_argument("query",
                        help="Search query to find package recipe reference, e.g., 'boost', 'lib*'")
    parser.add_argument("-r", "--remote", default=None, action=Extender,
                        help="Remote to search. Accepts wildcards. To search in all remotes use *")
    args = parser.parse_args(*args)

    remotes = conan_api.get_active_remotes(args.remote)

    results = []
    for remote in remotes:
        results.append(conan_api.search_remote_recipes(args.query, remote))
    return results
