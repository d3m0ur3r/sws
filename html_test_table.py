import html
from prettytable import PrettyTable


def main() -> int:
    pt = PrettyTable(["Date", "URL"])
    url = 'https://www.baidu.com'
    pt.add_row(['2018-10-10', f"<a href=\"{url}\">test</a>"])
    text = pt.get_html_string(format=True)
    text = html.unescape(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
