"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

from datetime import datetime

# file settings
LOG_FILENAME = '/home/xyz/PyBulkMail/pymail.log'
CSV_RETRY_FILENAME = '/home/xyz/PyBulkMail/pymail.csv'
STATS_FILE = '/home/xyz/PyBulkMail/pymail-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# the address and name the email comes from
FROM_NAME = 'xyz'
FROM_EMAIL = 'xyz@yahoo.in'



