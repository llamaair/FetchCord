def loaddiscord():
  from discord import fetchdycord

def loadpredicts():
  from predicts import PredictDigits


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