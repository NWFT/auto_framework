import logging

"""
debug/info/warning/error/critical
"""


def create_logger(file, level="DEBUG"):
    # 1. create a logger
    log = logging.getLogger('name')

    # 2. set collection level
    log.setLevel(level)

    # 3. set output method: console/file
    # 3.1 file
    out_f = logging.FileHandler(file, encoding="utf-8")
    out_f.setLevel(level)
    log.addHandler(out_f)
    # 3.2 console
    out = logging.StreamHandler()
    out.setLevel(level)
    log.addHandler(out)

    # 4. format
    log_f = logging.Formatter('%(asctime)s:%(message)s')
    out_f.setFormatter(log_f)
    out.setFormatter(log_f)

    return log


if __name__ == '__main__':
    log = create_logger("test.log")

    log.info("xxxxxxxxxxx")
