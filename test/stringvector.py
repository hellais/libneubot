#!/usr/bin/env python
# Public domain, 2014 Simone Basso <bassosimone@gmail.com>.

""" Test for NeubotPollable """

import sys

sys.path.insert(0, "/usr/local/share/libneubot")

from libneubot import Poller
from libneubot import StringVector

def main():
    """ Main function """
    poller = Poller()
    stringvector = StringVector(poller, 12)

    stringvector.append("yet another")
    stringvector.append("random")
    stringvector.append("str")

    sys.stdout.write("%s %s %s\n" % (
      stringvector.get_next(),
      stringvector.get_next(),
      stringvector.get_next()))
    
    stringvector.destruct()

if __name__ == "__main__":
    main()
