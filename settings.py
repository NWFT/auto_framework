import os
import time

# base_dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# test cases
TEST_CASES_DIR = os.path.join(BASE_DIR, 'test_cases')

# test reports
TEST_REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# Log files config
LOG_CONFIG = {
    'name': 'AT',
    'dir': os.path.join(BASE_DIR,'logs'),
    'filename': "AT-" + time.strftime("%Y%m%d-%H%M%S") + '.log',
    'mode': 'w',
    'encoding': 'utf-8',
    'debug': True
}

# database
DB_CONFIG = {
    'host': '192.168.1.165',
    'port': 3306,
    'database': 'users',
    'user': 'alex',
    'password': '12345678',
    'charset': 'utf8'
}

# wait time (seconds)
IMPLICITLY_TIME = 10
EXPLICITLY_TIME = 10
POLL_FREQUENCY = 0.5
HARD_WAIT_TIME = 5





