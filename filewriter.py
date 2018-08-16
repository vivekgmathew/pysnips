# Author : Vivek Mathew
# Email  : vivekgmathew@gmail.com

import abc
from datetime import datetime


class FileWriter(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, file_name):
        self.file_name = file_name

    def write_line(self, text):
        fh = open(self.file_name, 'a')
        fh.write(text + "\n")
        fh.close()


class LogWriter(FileWriter):

    def write(self, the_line):
        dt = datetime.now()
        dt_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}    {1}'.format(dt_str, the_line))


class DelimiterWriter(FileWriter):

    def __init__(self, file_name, delimiter):
        super(DelimiterWriter, self).__init__(file_name)
        self.delimiter = delimiter

    def write(self, the_list):
        line = self.delimiter.join(str(elem) for elem in the_list)
        self.write_line(line)






