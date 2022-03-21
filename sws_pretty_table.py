from prettytable import PrettyTable


def sort_output(url_list, switch_color) -> list:
    """Handles formatting of the output"""
    table_list = []
    for table_no, (table_id, table_rate, table_author, table_userid, table_title) in enumerate(url_list, start=1):
        dim: int = 0
        if switch_color:
            if table_no % 2 == 0:
                dim = 2

            table_no = "\x1b[{0};37m{1}\x1b[0m".format(dim, table_no)
            table_id = "\x1b[{0};32m{1}\x1b[0m".format(dim, table_id)
            table_rate = "\x1b[{0};33m{1}\x1b[0m".format(dim, "*" * table_rate)
            table_author = "\x1b[{0};34m{1}\x1b[0m".format(dim, table_author)
            table_userid = "\x1b[{0};35m{1}\x1b[0m".format(dim, table_userid)
            table_title = "\x1b[{0};36m{1}\x1b[0m".format(dim, table_title)

        else:
            table_rate = "{0}".format("*" * table_rate)

        table_list.append((table_no, table_id, table_rate, table_author, table_userid, table_title))

    return table_list


def sws_prettytable(url_list, switch_all, switch_color, page_title, page_range) -> None:
    """Handles the actual prettytable"""

    table = PrettyTable()
    table.title = f"{page_title} @ Page {page_range}".upper()
    table.add_column('\x1b[37mNO.\x1b[0m' if switch_color else 'NO.', [])
    table.add_column(f'\x1b[32mID\x1b[0m' if switch_color else 'ID', [])
    table.add_column(f'\x1b[33mSTARS\x1b[0m' if switch_color else 'STARS', [])
    table.add_column('\x1b[34mAUTHOR\x1b[0m' if switch_color else 'AUTHOR', [], align='l')
    table.add_column('\x1b[35mSTEAM USERID\x1b[0m' if switch_color else 'STEAM USERID', [], align='l')
    table.add_column(f'\x1b[36mTITLE\x1b[0m' if switch_color else 'TITLE', [], align="l")

    sorted_list = sort_output(url_list, switch_color)

    if not switch_all:  # Filters star rating 1 and above
        for no, table_id, table_rate, table_author, table_userid, table_title in sorted_list:
            table.add_row(
                [no, table_id, table_rate, table_author, table_userid, table_title]) if '*' in table_rate else None

    else:  # Gets anything regardless of star rating
        for no, table_id, table_rate, table_author, table_userid, table_title in sorted_list:
            table.add_row([no, table_id, table_rate, table_author, table_userid, table_title])

    print(table)


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
