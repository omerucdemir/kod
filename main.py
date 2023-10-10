import discord
from discord.ext import commands
from mantik import *

#ayrıcakları tanımlıyoruz.
ayricaliklar = discord.Intents.default()
#Mesaj içeriklerine ulaşım sağlamamı sağlar.
ayricaliklar.message_content = True

# prefix parametresine odaklayın - bu, komutları tanımlamamızı sağlayan bir tanımlayıcıdır!
bot = commands.Bot(command_prefix='$', intents=ayricaliklar)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


#bot komutlarını işleyen komutu yazmak.
@bot.command
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def pasw(ctx):
    await ctx.send(sifre_olusturucu(10))

bot.run("MTE1ODgxNDQwODE1MjE5OTE2OA.GRA5gm.jTxR4Vhlc5g3a8NZrD5QcncTEkHRihuZ3CMexk")
