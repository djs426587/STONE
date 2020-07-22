import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    game = discord.Game('𝓢𝓣𝓞𝓝𝓔#7690 구매 및 배너문의 dm 주세요')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("!dm"):
        for i in message.guild.members:
            if i.bot == False:
                a = message.content[1:]
                embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="인피니티 봇")
                embed.add_field(name="공지합니다", value=a, inline=True)
                embed.set_footer(text=f"https://discord.gg/9HJ7UFu")
                await i.send(embed=embed)
            else:
                pass

access_token = os.environ["token"]
client.run(access_token)
