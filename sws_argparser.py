import sys
import argparse

banner = r"""
 _____  _    _  _____ 
/  ___|| |  | |/  ___|
\ `--. | |  | |\ `--. 
 `--. \| |/\| | `--. \
/\__/ /\  /\  //\__/ /
\____/  \/  \/ \____/ 
"""


def icons(icon):  # styling on icons

    dash_icon = '\x1b[1;31m-\x1b[0m'
    plus_icon = '\x1b[1;32m+\x1b[0m'
    exclamation_icon = '\x1b[1;33m!\x1b[0m'

    if icon == '-':
        icon = dash_icon
    elif icon == '+':
        icon = plus_icon
    elif icon == '!':
        icon = exclamation_icon
    else:
        icon = 'none'

    return icon


def arg_parser() -> argparse.Namespace:
    # ArgParser - Define Usage
    prog_name = sys.argv[0]
    parser = argparse.ArgumentParser(prog=prog_name,
                                     epilog="""
╔═══════════════════════════════════════════════[ Examples ]══════════════════════════════════════════════╗                                         
║   -i <APPID>                                                                                            ║
║   -i <APPID> -r <RANGE>                                                                                 ║
║   -i <APPID> -r <RANGE> -o <FILE>                                                                       ║
║   -i <APPID> -r <RANGE> --most-subs                                                                     ║
║   -i <APPID> -r <RANGE> --most-subs --filter-author <AUTHOR>                                            ║
║   -i <APPID> -s <SEARCH STRING>                                                                         ║ 
╠═════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ SWS is a script designed to scrape steam workshop for mods.                                             ║
║ It does so by looking through a range of pages and then scrape all the urls.                            ║
║ Should be used in conjunction with https://steamworkshopdownloader.io/                                  ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""",
                                     usage=f"{prog_name} [options] -i <appid> -r <range>",
                                     prefix_chars="-",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-r', '--range',
                        action='store',
                        metavar='Range',
                        type=str,
                        help=f'Range: [lownum-highnum] example: 1-40 or 1 for page 1 etc.')

    parser.add_argument('-u', '--user',
                        action='store',
                        metavar='user',
                        type=str,
                        help='Searches for mods at a user with app id')

    parser.add_argument('-e', '--echo',
                        action='store_true',
                        help='Echoes output to terminal')

    parser.add_argument('--rich-table',
                        action='store_true',
                        help='Uses rich tables to display output')

    parser.add_argument('-c', '--color',
                        action='store_true',
                        help="Colors the output")

    parser.add_argument('-f', '--fast',
                        action='store_true',
                        help='Improves performance')

    parser.add_argument('-a', '--all',
                        action='store_true',
                        help='Gets all output')

    parser.add_argument('--most-subs',
                        action='store_true',
                        help='Sorts by most subscribed of all time')

    parser.add_argument('--filter-author',
                        action='store',
                        metavar='Filter Author',
                        nargs='+',
                        help='Filters chosen author')

    parser.add_argument('--sort-by',
                        action='store',
                        metavar='Sort',
                        type=str,
                        help='Sorts by chosen input [ID, STARS, AUTHOR, USERID, TITLE]')

    parser.add_argument('-s', '--search',
                        action='store',
                        metavar='Search',
                        type=str,
                        nargs='+',
                        help="Searches for a particular mod")

    parser.add_argument('-i', '--id',
                        action='store',
                        metavar='AppId',
                        type=int,
                        required=False,
                        help=f'Steam AppId number example: 920210')

    parser.add_argument('-o', '--outfile',
                        action='store',
                        metavar='Outfile',
                        type=str,
                        help='Saves output to a file')

    parser.add_argument('-v', action='version',
                        version=f'{banner}'
                                f'\nSteam '
                                f'\nWorkshop '
                                f'\nScraper v1.4.4 by \x1b[1;35md4r4k0n\x1b[0m ',
                        help=f'Prints the version of {prog_name}')

    args = parser.parse_args()  # Engages ArgParser

    # ═══════════════════════════════════════════════[ ARGS ]════════════════════════════════════════════════════ #
    sws_range = "1" if not args.range else args.range  # flag -r, --range,     defaults to page 1
    sws_app_id = 107410 if not args.id else args.id  # flag -i, --id,        defaults to 107410
    sws_all = args.all  # flag -a, --all
    sws_output = args.outfile  # flag -o, --output
    sws_echo = True if not sws_output else args.echo  # flag -e, --echo       True if not -o
    sws_search = args.search  # flag -s, --search
    sws_fast = args.fast  # flag -f, --fast
    sws_rich = args.rich_table  # flag     --rich-table
    sws_color = args.color  # flag -c, --color
    sws_most_subs = args.most_subs  # flag     --most-subs
    sws_filter_author = args.filter_author  # flag     --filter-author
    sws_sort_by = args.sort_by  # flag    --sort-by
    sws_user_id = args.user  # flag -u, --user
    # ═══════════════════════════════════════════════════════════════════════════════════════════════════════════ #

    return args


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
