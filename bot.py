import discord

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
intents.messages = True

from discord.ext import commands

bot = commands.Bot(command_prefix='$',intents=intents) #Build a discord bot(entity) and store in bot
                                       #When we call the bot, we need the Command prefix(字首) 

#When bot is switch on(啟動) -> trigger event -> run on_ready()
@bot.event #events under the bot
async def on_ready(): #on_ready already exists in discord , when we Override, need async
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member): #Triggered automatically when a member joins
    channel = bot.get_channel(1031071894390190160)  #Text channel's ID
    await channel.send(f'{member} join!') #Go to offical api to know what need await(coroutine)
                                          #member is a variable, use 'f'string can let the member keep changing
        
@bot.event
async def on_member_remove(member):
        channel = bot.get_channel(1031071894390190160)  #Text channel's ID
        await channel.send(f'{member} leave')

#ctx = context(上下文),use ctx to let bot know what's channel have new information, and reply
@commands.command()  #When we write command, we need ctx argument
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms') #send the ping(ms)


bot.run("MTAzMTA3MTQwMDA0MTEyMzg4MQ.GVH9Di.W65MkLVOgqK4MQ8Y1C6bbvQ0IZaj7Sn-zLEE6w")