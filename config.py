import os
import sys
import re


PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_DATA_PATH = PROJECT_ROOT_PATH + '/Testing_Data/'
#Split bases on \ or / for Unix and windows
PROJECT_NAME = re.split(r'\/|\\', PROJECT_ROOT_PATH)[-1]
REPORTS_ROOT_PATH = PROJECT_ROOT_PATH + '/src/Reports/'

sys.path.insert(0, PROJECT_ROOT_PATH)
sys.path.insert(1, PROJECT_ROOT_PATH + '/src/')