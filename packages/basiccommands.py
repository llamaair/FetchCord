def ping():
  @client.command()
  async def ping(ctx):
    await ctx.reply("Pong!")

def fetchcord():
  @client.command()
  async def fetchcord(ctx):
    await ctx.reply("FetchCord is a easy-to-use discord API")