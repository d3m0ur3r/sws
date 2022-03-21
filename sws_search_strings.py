"""Steam search strings"""
import requests
import re


def sws_details(url):
    details_stat_right = re.compile('(?<=detailsStatRight">).+(?=</div>)')
    r = requests.get(url)
    r = r.text

    search: list = re.findall(details_stat_right, r)

    return search[-1]


def main() -> int:
    pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
