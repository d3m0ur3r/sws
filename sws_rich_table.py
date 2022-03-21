from rich.table import Table
from rich import print as tprint


def sws_rich_table(url_list, switch_all, switch_color, page_title, page_range):

    if switch_color:
        table_style = 'none'  # #F8F8FF on #282828
        no_color = 'white'
        id_color = '#ADFF2F'
        star_color = '#FFD700'
        author_color = '#728FCE'
        username_color = '#FA8072'
        title_color = '#F8B88B'

    else:
        table_style = 'none'
        no_color = 'none'
        id_color = 'none'
        star_color = 'none'
        author_color = 'none'
        username_color = 'none'
        title_color = 'none'

    table = Table(style=table_style)
    table.title = f'{page_title} @ Page {page_range}'
    table.add_column(f'[{no_color}]NO.')
    table.add_column(f'[{id_color}]ID', justify='center')
    table.add_column(f'[{star_color}]STARS', justify='center')
    table.add_column(f'[{author_color}]AUTHOR')
    table.add_column(f'[{username_color}]STEAM USERID')
    table.add_column(f'[{title_color}]TITLE', justify='full')

    if not switch_all:

        for table_no, (table_id, table_rate, table_author, table_userid, table_title) in enumerate(url_list, start=1):

            if table_no % 2 == 0:
                dim = 'dim'
            else:
                dim = ''

            table.add_row(f"[{no_color} {dim}]{table_no}",
                          f"[{id_color} {dim}]{table_id}",
                          f"[{star_color} {dim}]{'*' * table_rate}",
                          f"[{author_color} {dim}]{table_author}",
                          f'[{username_color} {dim}]{table_userid}',
                          f'[{title_color} {dim}]{table_title}',
                          style=rf"link https://steamcommunity.com/sharedfiles/filedetails/?id={table_id}") if table_rate != 0 else 0

        if table.rows:
            tprint(table)
        else:
            print(f"[\033[1;31m-\033[0m] Nothing interesting here")
            raise SystemExit(0)

    else:

        for table_no, (table_id, table_rate, table_author, table_userid, table_title) in enumerate(url_list, start=1):
            if table_no % 2 == 0:
                dim = 'dim'
            else:
                dim = ''

            table.add_row(f"[{no_color} {dim}]{table_no}",
                          f"[{id_color} {dim}]{table_id}",
                          f"[{star_color} {dim}]{'*' * table_rate}",
                          f"[{author_color} {dim}]{table_author}",
                          f'[{username_color} {dim}]{table_userid}',
                          f'[{title_color} {dim}]{table_title}',
                          style=rf"link https://steamcommunity.com/sharedfiles/filedetails/?id={table_id}")
        tprint(table)


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
