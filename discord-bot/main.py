import discord, os, asyncio, json
from discord.ext import commands
from BUDDY import guild_id, shop_id, token
def conver_duration(duration: str):
    multiplier = 60 if duration.endswith("m") else 3600
    return int(duration[:-1]) * multiplier
def save_warn(ctx, member: discord.Member,reason: str):
    if not os.path.exists('warns.json'):
        with open('warns.json', 'w') as f:
            json.dump({}, f)

    with open('warns.json', 'r') as f:
        try:
            warns = json.load(f)
        except json.JSONDecodeError:
            warns = {}

    if str(member.id) not in warns:
        warns[str(member.id)] = []

    warns[str(member.id)].append(reason)
    with open('warns.json', 'w') as f:
        json.dump(warns, f)

def remove_warn(ctx, member: discord.Member, amount: int):
    with open('warns.json', 'r') as f:
        warns = json.load(f)

    if str(member.id) in warns:
        warns[str(member.id)] = warns[str(member.id)][amount:]

    with open('warns.json', 'w') as f:
        json.dump(warns, f)
def warns_check(member: discord.Member):
    with open('warns.json', 'r') as f:
        try:
            warns = json.load(f)
        except json.JSONDecodeError:
            warns = {}

    return len(warns.get(str(member.id), []))
token = os.getenv("tok_name")
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.bot_log_channel = None
class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.channel_id = None
    @discord.ui.button(label="🎫eopen ticket",style=discord.ButtonStyle.green)
    async def ticket(self, interaction:discord.Interaction, button:discord.ui.Button):
        user = interaction.user
        channel = await user.guild.create_text_channel(f"ticket for {user.name}")
        admin = discord.utils.get(user.guild.roles, name="admin")
        await channel.set_permissions(user, read_messages=True, send_messages=True)
        await channel.send(f"{user.mention} welcome to the shop an {admin.mention} well join you soon")
        everyone = discord.utils.get(user.guild.roles, name="member")
        await channel.set_permissions(everyone,read_messages=False,send_messages=False)
        self.channel_id = channel.id
@bot.event
async def on_ready():
    print("login succful")
    guild = bot.get_guild(guild_id)
    channel_com_name = "bot-log"
    for channel in guild.channels:
        if channel.name == channel_com_name:
            bot.bot_log_channel = channel
            break
    else:
        overwrites ={
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True)
            }
        bot.bot_log_channel = await guild.create_text_channel(channel_com_name, overwrites=overwrites)
    print(f"Bot log channel ID: {bot.bot_log_channel.id}")
    channelID = bot.get_channel(shop_id)
    view = Menu()
    role = discord.utils.get(guild.roles, name="admin")
    everyone = discord.utils.get(guild.roles, name="member")
    for channel in guild.channels:
        if channel.name == channel_com_name:
            print("bot-log channel already exists")
            return
    channel_command = await guild.create_text_channel(channel_com_name)
    await channel_command.set_permissions(role,read_messages=True,send_messages=False)
    await channel_command.set_permissions(everyone,read_messages=False,send_messages=False)
    channel_ID = channel_command.id
    bot.bot_log_channel = bot.get_channel(channel_ID)
    
@bot.event
async def on_member_join(member):#done
    guild = member.guild
    member_role = discord.utils.get(guild.roles, name="member")
    if member_role is not None:
        await member.add_roles(member_role)
@bot.listen()
@commands.has_permissions(moderate_members=True)
async def on_message(message):#semi-done
    words = ["nigga","fuck"]
    if message.author.bot:
        return 
    user = message.author
    role = discord.utils.get(message.guild.roles, name="mute")
    for word in words:
        if word in message.content:
            await user.add_roles(role,reason="saying bad word")
            await message.delete()
            channel = bot.bot_log_channel
            await channel.send(f"{user.mention} has been muted for saying {word}")
            return
@bot.command(name="cltk")
async def cltk(ctx):
    channel = ctx.channel
    if channel:
        await channel.delete()
    else:
        await ctx.send(f"{channel} does not existe")
@bot.command(name="mute")
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member:discord.Member,duration:int,*,reason:None):#done
    duration_sec = conver_duration(duration)
    is_admin = discord.utils.get(ctx.guild.roles, name="admin")
    if ctx.author.roles is not is_admin:
        await ctx.send(f"{ctx.author.mention} you are not admin")
        return
    if ctx.author == member:
        await ctx.send(f"{ctx.author.mention} you cant mute your self")
        return
    is_muted = discord.utils.get(ctx.guild.roles, name="mute")
    if member.roles is is_muted:
        await ctx.send(f"{ctx.author.mention} {member.mention} is already muted")
        return
    await member.add_roles(is_muted)
    await bot.bot_log_channel.send(f"{member.mention} has been muted for {duration}.")
    await ctx.send(f"{member.mention} has been muted for {duration}.")
    await asyncio.sleep(duration_sec)
    await member.remove_roles(is_muted)
    await bot.bot_log_channel.send(f"{member.mention} has been unmuted.")
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, mem:discord.Member,*, reason=None):#done
    role = discord.utils.get(ctx.author.roles, name="admin")
    if role is not None and role.name == "admin":  
        if mem == None or mem == ctx.message.author:
            await ctx.send("You can't ban yourself!")
            return
        if reason == None:
            reason = "No reason provided"
        message = f"You have been kicked from {ctx.guild.name} for {reason}"
        channel = bot.bot_log_channel
        await channel.send(f"{mem.mention} has been kicked for {reason}")
        await mem.send(message)
        await ctx.guild.kick(mem, reason=reason)
    else:
        await ctx.send(f"{ctx.author.mention} you dont have admin")
        return
@bot.command(name="banID")
@commands.has_permissions(ban_members=True)
async def banID(ctx, id: int,*, reason=None):#done
    user = await bot.fetch_user(id)
    role = discord.utils.get(ctx.author.roles, name="admin")
    if role is not None and role.name == "admin":
        if user == ctx.message.author:
            await ctx.send(f"{ctx.author.mention} you are cant ban yourself")
        channel = bot.bot_log_channel
        await channel.send(f"{user.mention} has been banned for {reason}")
        await ctx.guild.ban(user)
    else:
        await ctx.send(f"{ctx.author.mention} you dont have admin")
        return
@bot.command(name="ping")
async def ping(ctx):#done???
    await ctx.send("Pong!")
@bot.command(name="mention")
async def mention(ctx):#done
    await ctx.send("@everyone")
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, mem:discord.Member,*, reason=None):#done
    role = discord.utils.get(ctx.author.roles, name="admin")
    if role is not None and role.name == "admin":  
        if mem == None or mem == ctx.message.author:
            await ctx.send("You can't ban yourself!")
            return
        if reason == None:
            reason = "No reason provided"
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        channel = bot.bot_log_channel
        await mem.send(message)
        await ctx.guild.ban(mem, reason=reason)
        await channel.send(f"{mem} has been banned for {reason}")
    else:
        await ctx.send(f"{ctx.author.mention} you dont have admin")
        return
@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):#done
    user = await bot.fetch_user(id)
    author = ctx.author
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role not in author.roles:
        await ctx.send(f"{author.mention} you dont have admin")
        return
    if user == author:
        await ctx.send("You can't unban yourself!")
        return
    message = discord.Embed(title="unban",description=f"{author.mention} has unban {user.mention}")
    await ctx.guild.unban(user)
    await bot.bot_log_channel.send(embed=message)
    user_mes = discord.Embed(title="unban", description=f"{author.mention} has unban you")
    await user.send(embed=user_mes)
@bot.command(name="warn")
@commands.has_permissions(kick_members=True)
async def warn(ctx,member:discord.Member,*,reason):
    save_warn(ctx,member=member,reason=reason)
    role = discord.utils.get(ctx.author.roles, name="admin")
    user = ctx.author
    if role not in user.roles:
        await ctx.send(f"{user.mention} you dont have admin")
        return
    dm = await bot.fetch_user(member.id)
    em=discord.Embed(title="Warning", description=f"Server: {ctx.guild.name}\nReason: {reason}")
    await dm.send(embed=em)
    warns = warns_check(member)
    if warns >= 4:
        reason=f"having more thatn 3 warning"
        mes = discord.Embed(title="kick", description=f"Server: {ctx.guild.name}\nReason: {reason}")
        mess = discord.Embed(title="kick",description=f"member: {member.mention}\nReason: {reason}")
        await bot.bot_log_channel.send(embed=mess)
        await dm.send(embed=mes)
        await ctx.guild.kick(member)
@bot.command()
async def rmwarn(ctx, member: discord.Member, amount: int):
      remove_warn(ctx, member, amount)
      role = discord.utils.get(ctx.author.roles, name="admin")
      user = ctx.author
      if role not in user.roles:
          await ctx.send(f"{user.mention} you dont have admin")
          return
      mess = discord.Embed(title="remove warn",description=f"{ctx.author.mention}\nhas removed {amount} of warns for {member.name}")
      await bot.bot_log_channel.send(embed=mess)
@bot.command(name="swmode")
async def swmode(ctx, duration: int):
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role not in ctx.author.roles:
        await ctx.send(f"{ctx.author.mention} you dont have admin")
        return
    await ctx.channel.edit(slowmode_delay = duration)
    message = discord.Embed(title="slow mode",description=f"{ctx.author.mention} has set slow mode for {duration}s in this channel")
    await ctx.send(embed=message)
@bot.command(name="welcome")
async def welcome(ctx,member:discord.Member):
    em=discord.Embed(title="Welcome", description="Hello and welcome to our server:)")
    await member.send(embed=em)
bot.run(token)