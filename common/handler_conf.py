from configparser import ConfigParser


class Config(ConfigParser):
    """create object, load config file content"""
    def __init__(self, file):
        super().__init__()
        self.read(file, encoding='utf-8')


if __name__ == '__main__':

    cp = Config('../conf/env.ini')
    level = cp.get('logging', 'level')
    print(level)