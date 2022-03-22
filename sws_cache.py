"""Handles cache"""
import json


class SWSCache:
    def __init__(self, command):
        super(SWSCache, self).__init__()

        self.raw_command: list = command
        self.current_command: dict = self.parse_command(command)
        self.last_command: dict = {}

    def handle_cache(self) -> list:
        try:
            self.load_command()
            if equal := self.current_command == self.last_command:
                try:
                    # print(equal)
                    url_list = self.load_cache()
                    return url_list
                except Exception:
                    print('Something went wrong:', self.last_command)
                    return []
            else:
                return []

        except Exception:
            return []

    @staticmethod
    def parse_command(command):
        command: dict = command.__dict__

        new_command = {}
        ignore = ['rich_table', 'fast', 'all', 'filter_author', 'outfile', 'color', 'echo', 'debug', 'sort_by']
        for k, v in command.items():
            if k not in ignore:
                new_command.update({k: v})

        return new_command

    @staticmethod
    def load_cache() -> list:
        with open('./SWScache.json', 'r', encoding='utf-8') as cache_file:
            output = json.load(cache_file)
            return output

    @staticmethod
    def save_cache(output) -> None:
        with open('./SWScache.json', 'w', encoding='utf-8') as cache_file:
            cache_file.writelines(json.dumps(output))

    def save_command(self) -> None:
        with open('./SWSCache_command.json', 'w', encoding='utf-8') as cache_file:
            json.dump(self.current_command, cache_file)

    def load_command(self) -> None:
        with open('./SWSCache_command.json', 'r', encoding='utf-8') as cache_file:
            self.last_command = json.load(cache_file)


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
