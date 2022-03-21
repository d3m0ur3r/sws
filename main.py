"""
Steam Workshop Scraper is built around scraping appid's.
SWS is built in python 3.9
SWS is a script designed to scrape steam workshop for mods.
It does so by looking through a range of pages and then scrape all the urls.
Should be used in conjunction with https://steamworkshopdownloader.io/
"""
import requests
import re
import concurrent.futures
import os
import math
from rich.progress import track
from sws_rich_table import sws_rich_table
from sws_pretty_table import sws_prettytable
from sws_argparser import arg_parser

creator_and_author = 'd4r4k0n'


class SWS:
    def __init__(self):
        super(SWS, self).__init__()

        _all_ = {'self.url_list': 'Main list with all output going into table',
                 'self.raw_ids': 'Contains ids only',
                 'self.sws_filter_author': '--filter-author, author search method',
                 'self.sws_search': '-s, --search, search method',
                 'self.sws_echo': '-e, --echo, echoes output to terminal, is set True as default',
                 'self.sws_rich': '--rich-table, determines if rich tables is used instead of the default prettytable'
                 }

        # ═══════════════════════════════════════════════[ LISTS ]═══════════════════════════════════════════════════ #
        self.url_list: list = []  # Main list with all output going into table.
        self.raw_ids: list = []  # Contains harvested ids only for ease of use with https://steamworkshopdownloader.io
        self.sws_filter_author: list = []  # --filter-author, author search method.
        self.sws_search: list = []  # -s, --search, search method.
        # ═══════════════════════════════════════════════════════════════════════════════════════════════════════════ #
        # ########################################################################################################### #
        # ═══════════════════════════════════════════════[ BOOLS ]═══════════════════════════════════════════════════ #
        self.sws_echo: bool  # -e, --echo, echoes output to terminal, is set True as default.
        self.sws_rich: bool  # --rich-table, rich tables is used instead of the default prettytable.
        self.sws_all: bool  # -a, --all, all outputs.
        self.sws_fast: bool  # -f, --fast,  faster search, uses concurrent.futures.
        self.sws_color: bool  # -c, --color, colored output.
        self.sws_most_subs: bool  # --most-subs, lists mods with most subscribers.
        # ═══════════════════════════════════════════════════════════════════════════════════════════════════════════ #
        # ########################################################################################################### #
        # ════════════════════════════════════════════════[ INTS ]═══════════════════════════════════════════════════ #
        self.sws_app_id: int = 0  # -i, --id, app_id - defaults to arma 3 if no input is specified.
        self.low_num: int = 0  # low range number.
        self.high_num: int = 0  # high range number.
        # ═══════════════════════════════════════════════════════════════════════════════════════════════════════════ #
        # ########################################################################################################### #
        # ══════════════════════════════════════════════[ STRINGS ]══════════════════════════════════════════════════ #
        self.sws_range: str = ""  # -r, --range, range method. valid inputs: [x] [x-x].
        self.sws_output: str = ""  # -o, --outfile, saves ids only as output into a file. see line 40 @ self.raw_ids.
        self.title: str = ""  # stores game title.
        self.workshop: str = ""  # stores validity of workshop. 'Workshop available' or 'No workshop available'.
        self.entries: str = ""  # stores how many entries(mods) available on at a workshop.
        self.sws_sort_by: str = ""  # --sort-by, stores sort by id, stars, author, userid, title
        self.sws_user_id: str = ""  # -u, --user, stores userid being searched
        self._url_search_string: str = ""  # stores current url
        # ═══════════════════════════════════════════════════════════════════════════════════════════════════════════ #
        self.args = arg_parser()  # argparse main variable.
        # ═══════════════════════════════════════════════[ ARGS ]════════════════════════════════════════════════════ #
        self.sws_range = "1" if not self.args.range else self.args.range  # flag -r, --range,     defaults to page 1
        self.sws_app_id = 107410 if not self.args.id else self.args.id  # flag -i, --id,        defaults to 107410
        self.sws_all = self.args.all  # flag -a, --all
        self.sws_output = self.args.outfile  # flag -o, --output
        self.sws_echo = True if not self.sws_output else self.args.echo  # flag -e, --echo       True if not -o
        self.sws_search = self.args.search  # flag -s, --search
        self.sws_fast = self.args.fast  # flag -f, --fast
        self.sws_rich = self.args.rich_table  # flag     --rich-table
        self.sws_color = self.args.color  # flag -c, --color
        self.sws_most_subs = self.args.most_subs  # flag     --most-subs
        self.sws_filter_author = self.args.filter_author  # flag     --filter-author
        self.sws_sort_by = self.args.sort_by  # flag    --sort-by
        self.sws_user_id = self.args.user  # flag -u, --user
        # ═══════════════════════════════════════════════════════════════════════════════════════════════════════════ #

        if self.sws_most_subs and self.sws_user_id:
            print('[{0}] You can\'t use --most-subs and --user together!'.format(self.icons('!')))
            raise SystemExit(0)

        if self.sws_app_id and self.sws_range:

            single = re.compile(r'(\d+)')  # expression
            split_range = re.findall(single, self.sws_range)  # find all digits

            try:
                if len(split_range) == 1:
                    self.low_num = int(self.sws_range)
                    self.high_num = int(self.sws_range)

                elif len(split_range) == 2 and '-' in self.sws_range:
                    low_num, high_num = split_range
                    self.low_num = int(low_num)
                    self.high_num = int(high_num)

                else:
                    print('[{0}] You must specify a valid range. Example: <1-10>'.format(self.icons('!')))
                    # parser.print_help()
                    raise SystemExit(0)

            except Exception:

                print('[{0}] You must specify a valid range. Example: <1-10>'.format(self.icons('!')))
                # parser.print_help()
                raise SystemExit(0)

            if self.high_num < self.low_num:

                print('[{0}] You must specify a valid range. Example: <1-10>'.format(self.icons('!')))
                # parser.print_help()
                raise SystemExit(0)

            elif self.low_num == self.high_num:
                # requests running here
                self.run()

            else:
                # requests running here
                self.run()

    @staticmethod
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

    def run(self) -> None:
        """Main run method."""

        workshop_validity = self.probe_app_id()  # resolves name and workshop validity.
        if self.sws_fast and workshop_validity:
            self.get_steam_workshop_links(True)  # 'requests.get' with concurrent.futures
        elif workshop_validity:
            self.get_steam_workshop_links()  # regular 'requests.get' behavior

    def save_file(self) -> None:
        """Saves output to file"""
        with open(os.path.abspath(self.sws_output), "w") as file:
            file.writelines(self.raw_ids)

    def probe_app_id(self) -> str:
        """Probes the AppId and formats the output"""

        print(f"[{self.icons('!')}] Probing AppId >> [\x1b[1;33m{self.sws_app_id}\x1b[0m]")

        self.workshop = self.workshop_check(self.web_search(self.low_num))
        icon = self.icons('+') if "Workshop available" in self.workshop else self.icons('-')

        print(
            f"[{icon}] "
            f"[\033[1;33m{self.title}\033[0m] "
            f"[\033[1;34m{self.workshop}\033[0m] "
            f"[\033[1;35m{self.entries} Entries\033[0m] "
            f"[\033[1;36m{math.ceil(int(self.entries) / 30)} Pages\033[0m]"
        )

        return self.workshop

    def workshop_check(self, _url) -> str:
        """Checks if the corresponding appId has a workshop"""
        r = requests.get(_url, allow_redirects=False)

        if not r.status_code == 200:
            print(f"[{self.icons('-')}] No workshop available")
            raise SystemExit(0)

        else:
            try:
                self.entries = self.resolve_mods_amount(r.text)  # Resolves amount of mods available
                self.title = self.name_resolver(r.text)  # Name resolver
            except AttributeError:
                print(f'[{self.icons("-")}]',
                      'Search did not return anything.' if self.sws_search else 'Invalid user id')
                raise SystemExit(0)
            return "Workshop available"

    def name_resolver(self, _request) -> str:
        """Resolves the appId to it's corresponding title"""
        try:
            pattern_name = re.compile(r'(?<=class="apphub_AppName ellipsis">).+(?=</div>)')
            search = re.search(pattern_name, _request).group()
        except Exception as e:  # username search
            # print(e)
            pattern_name = re.compile(f'(?<={self.sws_app_id}">).+(?=</a>)')
            search = re.search(pattern_name, _request).group()
            # print(search)

        return search

    @staticmethod
    def resolve_mods_amount(site_content) -> str:
        """Resolves the amount of available mods"""
        pattern = re.compile(r'(?<=class="workshopBrowsePagingInfo">).+(?=</div>)')
        entries = re.search(pattern, site_content).group()

        pattern2 = re.compile(r'(?<=of )[\d,]+(?= entries)')
        amount = re.search(pattern2, entries).group().replace(",", "")

        return amount

    def web_search(self, _page: int = 1) -> str:
        """Handles the url search type
        :param _page: current page number being handled
        :type _page: int
        """
        url_app_id: str = f'https://steamcommunity.com/workshop/browse/?appid={self.sws_app_id}'  # Main url

        steam_web_strings = [self.search_user() if self.sws_user_id else '',
                             f'&searchtext={"+".join(self.sws_search)}&actualsort=textsearch&browsesort=textsearch' if self.sws_search else '',
                             '&browsesort=totaluniquesubscribers&section=readytouseitems&actualsort=totaluniquesubscribers' if self.sws_most_subs else '']

        string = url_app_id if not self.sws_user_id else '' + ''

        for v in steam_web_strings:
            if v:
                string += v

        string += f'&browsesort=trend&days=90' if string == url_app_id else ''

        self._url_search_string = string + '&p='
        _url_page: str = self._url_search_string + str(_page)

        return _url_page

    def harvest_ids(self, _page: str) -> None:
        """Harvests all ids
        :param _page: url + page number being processed
        :type _page: str"""

        # print(_page)

        def request_get(_page: str) -> list:
            """Does most of the heavy lifting with requests and regex
            :param _page: url + page number being processed
            :type _page: str
            :return output_list: list containing tuples of data (id, stars, author, userid, title)
            :rtype output_list: list
            """

            try:

                r: requests.models.Response = requests.get(_page, allow_redirects=False)
                webpage: str = r.text

                search_id: list = re.findall(
                    r'(?<=href=")https://steamcommunity.com/sharedfiles/filedetails/\?id=([0-9]+)',
                    webpage)
                search_rating: list = re.findall(
                    r'(?<=/images/sharedfiles/)(\d|not-yet)',
                    webpage)
                # print(search_rating) # Debug
                search_title: list = re.findall('(?<=workshopItemTitle ellipsis">).+(?=</div>)', webpage)

                for x in search_id:
                    while search_id.count(x) > 1:
                        search_id.remove(x)

                for idx, rate in enumerate(search_rating):  # turns all ratings into integers.
                    if rate == "not-yet":
                        search_rating[idx] = 0
                    else:
                        search_rating[idx] = int(search_rating[idx])

                if not self.sws_user_id:
                    search_author: list = re.findall(fr'(?<=myworkshopfiles/\?appid={self.sws_app_id}">).+(?=</a>)',
                                                     webpage)
                    search_username: list = re.findall(r'[\w\d-]+(?=/myworkshopfiles)', webpage)

                elif self.sws_user_id.isdigit():

                    search_author: list = re.findall(
                        f'(?<=https://steamcommunity.com/profiles/{self.sws_user_id}">).+(?=</a>)', webpage) * len(
                        search_id)
                    search_username: str = re.search(r'[\d]+(?=/myworkshopfiles)', webpage).group()
                    search_username: list = [search_username for _ in range(len(search_id))]

                else:
                    search_author: list = re.findall(
                        f'(?<=https://steamcommunity.com/id/{self.sws_user_id}">).+(?=</a>)', webpage,
                        re.IGNORECASE) * len(search_id)

                    search_username: str = re.search(r'[\w\d-]+(?=/myworkshopfiles)', webpage).group()
                    search_username: list = [search_username for _ in range(len(search_id))]

                # DEBUGGING
                # print(
                #     search_id,
                #     search_rating,
                #     search_author,
                #     search_username,
                #     search_title,
                # )

                output_list: list = [(s_id, s_ra, s_au.capitalize(), s_un, s_na.capitalize()) for
                                     s_id, s_ra, s_au, s_un, s_na in
                                     zip(search_id, search_rating, search_author, search_username, search_title)]

                return output_list

            except Exception:

                print(f"[-] [Something went wrong trying @ Page: {_page}]")

            del search_id, search_title, search_author, search_username, search_rating  # Deletes variable lists to save memory

        self.url_list += request_get(_page)

        if not self.sws_all:  # gets raw ids only
            self.raw_ids = [search_id + "\n" for search_id, search_rate, _, _, _ in self.url_list if search_rate != "0"]
        else:
            self.raw_ids = [search_id + "\n" for search_id, _, _, _, _ in self.url_list]

    def search_user(self) -> str:
        """searches for a user @ app id [profiles/id]"""
        if self.sws_user_id.isdigit():
            return f'https://steamcommunity.com/profiles/{self.sws_user_id}/myworkshopfiles/?appid={self.sws_app_id}&numperpage=30'

        else:
            return f'https://steamcommunity.com/id/{self.sws_user_id}/myworkshopfiles/?appid={self.sws_app_id}&numperpage=30'

    def sort_output(self, sort='STARS'):
        """sorts list by given arg"""

        if sort.upper() == 'TITLE' or sort.upper() == 'AUTHOR' or sort.upper() == 'USERID':
            order = False
        else:
            order = True

        sorting_dic = {'ID': 0,
                       'STARS': 1,
                       'AUTHOR': 2,
                       'USERID': 3,
                       'TITLE': 4
                       }

        self.url_list.sort(key=lambda s_ra: s_ra[sorting_dic.get(sort.upper(), 1)], reverse=order)  # Sorts by STARS ASC

    def filter_author(self) -> list:
        """Filters a/or multiple authors
        :return search_list: list of sorted author/authors
        :rtype search_list: list"""

        author = " ".join(self.sws_filter_author)
        authors = author.split(",")
        search_list = []

        for author in authors:
            search = [(search_id, search_rate, search_author, search_userid, search_title) for
                      search_id, search_rate, search_author, search_userid, search_title in self.url_list if
                      author.lower() in search_author.lower()]

            search_list += search

        self.sort_output(self.sws_sort_by) if self.sws_sort_by else self.sort_output()

        return search_list

    def get_steam_workshop_links(self, switch: bool = False) -> None:
        """Retrieves workshop links via Regex"""

        urls = [self._url_search_string + str(x) for x in range(self.low_num, self.high_num + 1)]

        if switch:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                _ = *track(executor.map(lambda _page: self.harvest_ids(_page), urls),
                           total=((self.high_num + 1) - self.low_num),
                           complete_style='#BA55D3',
                           finished_style='#BA55D3',
                           description='[#BA55D3 bold]Fetching IDs'),

        else:
            for _page in track(urls,
                               total=((self.high_num + 1) - self.low_num),
                               complete_style='#BA55D3',
                               finished_style='#BA55D3',
                               description='[#BA55D3 bold]Fetching IDs'):
                self.harvest_ids(_page)

        self.sort_output(self.sws_sort_by) if self.sws_sort_by else self.sort_output()

        if self.sws_filter_author:
            self.url_list = self.filter_author()

        if self.sws_echo:  # if -e switch is used, echoes to terminal.

            if self.sws_rich:
                sws_rich_table(self.url_list, self.sws_all, self.sws_color, self.title,
                               self.sws_range)  # Uses rich tables
            else:
                sws_prettytable(self.url_list, self.sws_all, self.sws_color, self.title,
                                self.sws_range)  # Uses prettytable
        if self.sws_output:  # if -o switch is used, saves output to a file.
            self.save_file()


def main() -> int:
    sws = SWS()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
