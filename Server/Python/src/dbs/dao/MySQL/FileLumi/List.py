#!/usr/bin/env python
"""
This module provides FileLumi.List data access object.
"""
__revision__ = "$Id: List.py,v 1.2 2010/02/11 19:39:32 afaq Exp $"
__version__ = "$Revision: 1.2 $"

from dbs.dao.Oracle.FileLumi.List import List as OraFileLumiList

class List(OraFileLumiList):
        pass

