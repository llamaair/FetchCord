import json
def loaddiscord():
  from discord import fetchdycord

def loadpredicts():
  from predicts import PredictDigits

def get_db_data():
  with open("db.json", 'r') as f:
    status = json.load(f)
    return db

print("FetchCord waking up...")
print("Loading modules")
print("Loading discord cog")
loaddiscord()
print("Successfully loaded discord")
print("Loading predicts cog")
loadpredicts()
print("Successfully loaded predicts")

print("FetchCord is alive!")


key="something"
while key != "q":
  loadings=str(input())
  if loadings=="import imports":
    print("Loading imports")
    import imports
    loadings=None
  elif loadings=="import predicts":
    print("Loading predicts")
    loadpredicts()
    loadings=None
  elif loadings=="import discord":
    print("Loading discord")
    loaddiscord()
    loadings=None
  elif loadings=="quit":
    print("Killing FetchCord")
    quit()
  elif loadings=="keep_alive":
    print("Keeping alive!")
    from keep_alive import keep_alive
    keep_alive()
  elif loadings=="import bot":
    print("Loading bot")
    from defines import bot
    loadings=None
  elif loadings=="read.db":
    get_db_data()
    print(db)
  elif loadings=="import api":
    import api
  elif loadings=="import config":
    import config
    print("Config loaded!")