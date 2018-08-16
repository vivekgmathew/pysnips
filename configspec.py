# Author : Vivek Mathew
# Email : vivekgmathew@gmail.com

import os


class ConfigSpec(dict):

    def __init__(self, file_name):
        self._file_name = file_name
        if os.path.isfile(self._file_name):
            with open(self._file_name) as fh:
                for line in fh:
                    if not line.startswith('#'):
                        line = line.strip()
                        line = line.replace('\\', "")
                        key, value = line.split('=', 1)
                        dict.__setitem__(self, key, value)





