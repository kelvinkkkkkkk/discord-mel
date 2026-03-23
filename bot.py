import discord
from discord.ext import commands
import random

# 🔥 INTENTS (ESSENCIAL)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

perguntas = [
    {"material": "garrafa pet", "resposta": "plastico"},
    {"material": "casca de banana", "resposta": "lixo umido"},
    {"material": "papel", "resposta": "reciclavel"},
    {"material": "vidro", "resposta": "vidro"},
    {"material": "lata", "resposta": "reciclavel"}
]

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# ✅ comando de teste
@bot.command()
async def teste(ctx):
    await ctx.send("✅ Estou funcionando!")

# 🌱 comando quiz
@bot.command()
async def quiz(ctx):
    p = random.choice(perguntas)

    await ctx.send(
        f"🌱 Onde descartar: **{p['material']}**?\n"
        "Responda com: plastico / vidro / reciclavel / lixo umido"
    )

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", timeout=20.0, check=check)

        if msg.content.lower() == p["resposta"]:
            await ctx.send("✅ Acertou!")
        else:
            await ctx.send(f"❌ Errou! Resposta correta: {p['resposta']}")

    except:
        await ctx.send("⏰ Tempo esgotado!")

bot.run("token")
