
'''
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",action="store_false", dest="verbose", default=True,help="don't print status messages to stdout")
args = ["-f", "foo.txt"]
(options, args) = parser.parse_args(args)
print(options.filename)
'''

'''
执行时，输入--help
'''

def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="some boolean option")
    parser.addoption("--foo", action="store", default="bar",
                     help="foo: bar or baz")
