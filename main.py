import discord
from discord.ext import commands
from discord.ext.commands import is_owner
from webserver import keep_alive
import os

client = commands.Bot(command_prefix="n!")       
client.remove_command('help')

@client.event
async def on_connect():
  print("bot is online")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="NEON DEVELOPMENT"))
    
@client.command()
@is_owner()
async def start(ctx):
 await ctx.send("NEON SERVICES IS STARTED")

@client.command()
@is_owner()
async def help(ctx):
  h=discord.Embed(title="HELP MENU", description="error")
  await ctx.send(embed=h)



@client.command()
async def dev(ctx):
  await ctx.send("XTREAM#8374")

@client.command()
async def info(ctx):
  await ctx.send("Name : NEON PRIME | Version : 1.0.7 | Language : python 3")

@client.command()
async def suggest(ctx, *,message):
	e=discord.Embed(title="SUGGESTION",description=f"{message}")
	msg=await ctx.channel.send(embed=e)
	await msg.add_reaction("✅")
	await msg.add_reaction("❌")

@client.command(description="see the bot latency")
async def ping(ctx):
    await ctx.send(f"Pong! {int(client.latency * 1000)}ms")

@client.command(description="Sends what you want the bot to say.")
async def say(ctx, *, content):
    await ctx.send(content)

@client.command(aliases=['rev'])
async def reverse(ctx, *, content):
	embed = discord.Embed(
        description=content[::-1],
        color=0xffff80)
	embed.set_author(
        name=ctx.author,
        icon_url=ctx.author.avatar_url
    )
	await ctx.send(embed=embed)

@client.command(aliases=['rules'])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command(aliases=['c', 'purge', 'p'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=3):
    await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await member.send("You have been kicked from **𝔽𝕌ℕ 𝔾𝕌𝕐𝕊** server for "+reason)
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " has been from banned **𝔽𝕌ℕ 𝔾𝕌𝕐𝕊** server for "+reason)
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('>>')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member.name,member_disc):

            await ctx.uild.unban(user)
            await ctx.send(member.name +" has been unbanned!")
            return

    await ctx.send(member+"was not found!")

@client.command()
@is_owner()
async def neon(ctx):
  await ctx.send("https://dsc.gg/neon-bot")

keep_alive()
token = os.environ.get("TOKEN")
client.run(token)