import json
from replit import db  #, Database , ReplInfo

def get_number_of_cdrs():
  if "num_cdrs" in db.keys():
    return db["num_cdrs"]
  else:
    return -1 #represents key not existing

def get_cdrData():
  if "cdrData" in db.keys():
    return json.loads(db["cdrData"])
  else:
    return {} #represents key not existing

def is_number_of_cdrs_changed(rows):
  db_data = get_number_of_cdrs()

  if db_data == -1: #means no data exists
    return False
  elif db_data != rows: #number of cdrs has changed
    return True
  return False

def get_changed_cdrData(data):
  db_data = get_cdrData()
  print(data.keys() - db_data.keys())
  return data.keys() - db_data.keys()
