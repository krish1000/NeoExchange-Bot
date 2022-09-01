import json
from replit import db  #, Database , ReplInfo

# def put_serverChannelID(serverID, channelID):
#   asdf = db["asdf"]
#   print(asdf)


def put_number_of_cdrs(num_rows):
  # if "num_cdrs" in db.keys():
  db["num_cdrs"] = num_rows

def put_cdrData(data):
  j = json.dumps(data)
  db["cdrData"] = j
