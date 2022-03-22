"""Handles cache"""
import json
import os
import random
import string


class SWSCache:
    def __init__(self, command):
        super(SWSCache, self).__init__()

        self.raw_command: dict = command.__dict__
        self.app_id = self.raw_command['id']
        self.current_command: dict = self.parse_command(command)
        self.last_command: dict = {}
        self.path = f'./.cache/{self.app_id}/'
        self.salt_path = os.path.join(self.path, '/.salt/')

        self.data_file = self.filename_generator('data')
        self.arg_file = self.filename_generator('arg')

    def handle_cache(self) -> list:

        try:
            self.load_args()

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

    def filename_generator(self, file_type) -> str:

        master_string = ''

        ignore = ['rich_table', 'fast',
                  'all', 'filter_author',
                  'outfile', 'color',
                  'echo', 'debug',
                  'sort_by', 'clear_cache']

        for k, v in self.raw_command.items():
            if k not in ignore:
                if isinstance(v, list):
                    v = '-'.join(v).lower()
                elif v is None or not v:
                    v = '0'

                master_string += f'{k[0]}_{v}'

        while len(master_string) < 50:
            master_string += '0'

        seed = file_type + master_string
        random.seed(seed)
        return ''.join(random.choices(string.hexdigits, k=len(master_string))) + '.json'

    @staticmethod
    def parse_command(command):
        command: dict = command.__dict__

        new_command = {}
        ignore = ['rich_table', 'fast',
                  'all', 'filter_author',
                  'outfile', 'color',
                  'echo', 'debug',
                  'sort_by', 'clear_cache']

        test_string = ''
        for k, v in command.items():
            if k not in ignore:
                new_command.update({k: v})
        print(test_string)
        return new_command

    def store_data(self, output):

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        self.store_cache(output)
        self.store_args()

    def store_cache(self, output) -> None:
        """Saves table data into a JSON file"""
        with open(os.path.join(self.path, self.data_file), 'w', encoding='utf-8') as cache_file:
            cache_file.write(json.dumps(output))

    def load_cache(self) -> list:
        """Loads a json file with table data from last search"""
        with open(os.path.join(self.path, self.data_file), 'r', encoding='utf-8') as cache_file:
            output = json.load(cache_file)
            return output

    def store_args(self) -> None:
        """Stores the args in a JSON file"""

        with open(os.path.join(self.path, self.arg_file), 'w', encoding='utf-8') as cache_file:
            json.dump(self.current_command, cache_file)

    def load_args(self) -> None:
        """Loads a JSON file containing ARGS from last search"""
        with open(os.path.join(self.path, self.arg_file), 'r', encoding='utf-8') as cache_file:
            self.last_command = json.load(cache_file)

    def flush_cache(self):
        files: list = [os.path.abspath(os.path.join(self.path, file)) for file in os.listdir(self.path)]

        if not files:
            print('[!] You haven\'t got a cache to clear yet!')

        else:

            for file in files:
                file = f"\x1b[1;31m{file}\x1b[0m"
                print(file)

            prompt = input('\x1b[1;33mClear cache ? [y/N]: \x1b[0m')

            while True:
                if prompt == 'y':

                    for file in files:
                        print(f'[!] Removing cache >> \x1b[1;31m{file}\x1b[0m')
                        os.remove(file)
                    break

                elif prompt == 'N':
                    print('\x1b[1;32m[!] Aborting\x1b[0m')
                    break

                else:
                    print('[!] y or N, case sensitive!')
                    prompt = input('\x1b[1;5;31mClear cache ? [y/N]: \x1b[0m')


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
