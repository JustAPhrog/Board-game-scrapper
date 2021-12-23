from pathlib import Path
from sqlite3 import connect, Error


def if_file_exists(pure_path:Path):
    return pure_path.exists() and pure_path.is_file()


class Storage:
    def __init__(self, file_name, file_path='.'):
        pure_path = Path(file_path, file_name)
        if if_file_exists(pure_path):
            print('Found database')
        else:
            print('No db file. Will create one')
        self.file_path = pure_path
        try:
            self.conn = connect(self.file_path)
        except Error as err:
            print('Cannot connect to db:{}'.format(err))

    def __del__(self):
        if self.conn is not None:
            self.conn.close()

    def add_board_game(self, game_name, link, price):
        pass


if __name__ == '__main__':
    pass
