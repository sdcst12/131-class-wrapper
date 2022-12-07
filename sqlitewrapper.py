#!python

class sqlite3Wrapper:
  file = ""
  connection = ""
  cursor = ""
  table = ""
  
  def __init__(self,filename,table):
    # constructor must establish a connection to the sqlite file
    # this connection will use the self.connection to establish connection to self.file specified by filename
    # table will be used specifically for connections to this table
    # we should create self.cursor for future commands
   
  def addRow(self,data):
    # command to insert data into the database
    # data will be a dictionary that contains rownames (keys) and the data (values) to be entered for each item
  
  def modifyRow(self,id,data):
    # command to modify data in the database
    # id is the id of the record to be modified
    # data is a dictionary that contains the rownames (as keys) and data (as values) to be modified
  
  
  
