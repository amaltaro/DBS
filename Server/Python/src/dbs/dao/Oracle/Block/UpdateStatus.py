#!/usr/bin/env python
"""
This module provides Block.UpdateStatus data access object.
"""
__revision__ = "$Id: UpdateStatus.py,v 1.2 2010/06/23 21:21:18 afaq Exp $"
__version__ = "$Revision: 1.2 $"

from WMCore.Database.DBFormatter import DBFormatter

class UpdateStatus(DBFormatter):

    """
    Block Update Statuss DAO class.
    """

    def __init__(self, logger, dbi, owner):
        """
        Add schema owner and sql.
        """
        DBFormatter.__init__(self, logger, dbi)
	self.owner = "%s." % owner if not owner in ("", "__MYSQL__") else ""
        self.sql = """UPDATE %sBLOCKS SET OPEN_FOR_WRITING = :open_for_writing , LAST_MODIFICATION_DATE = :ltime where BLOCK_NAME = :block_name""" %  self.owner 
        
    def execute ( self, conn, block_name, open_for_writing, ltime, transaction=False ):
        """
        for a given file
        """	
	if not conn:
            raise Excpetion("dbsException-1", "%s Oracle/Block/UpdateStatus.  Expects db connection from upper layer.\n"\
                    %DBSEXCEPTIONS["dbsException-1"])
	binds = { "block_name" : block_name , "open_for_writing" : open_for_writing , 'ltime':ltime}
        result = self.dbi.processData(self.sql, binds, conn, transaction)
    
