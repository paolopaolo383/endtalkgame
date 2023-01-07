
import asyncio
import discord
import pickle
import random
import time
from discord.utils import get

import asyncio
from warnings import catch_warnings
import discord
import os
from discord.errors import HTTPException
from discord.utils import get



reaction_list = ['\U00000030\U0000FE0F\U000020E3','1️⃣', '2️⃣', '3️⃣','\U00000034\U0000FE0F\U000020E3','\U00000035\U0000FE0F\U000020E3','\U00000036\U0000FE0F\U000020E3','\U00000037\U0000FE0F\U000020E3','\U00000038\U0000FE0F\U000020E3','\U00000039\U0000FE0F\U000020E3']
word = [' ', ' ']
doom = [['름' ,'늠'] ,['라' ,'나'] ,['릇' ,'늣'] ,['락' ,'낙'] ,['루' ,'누'] ,['로' ,'노'] ,['리' ,'이'] ,['랑' ,'낭'] ,['려' ,'여']
        ,['립' ,'닙'] ,['륨' ,'윰'] ,['례' ,'예'] ,['량' ,'양'] ,['릴' ,'일'] ,['랄' ,'날'],['룩','눅']]
add = '0'
mes = '0'
cut =False
soo = 0
double = []
client = discord.Client()
i = 0
game = 0
isgaming = False
things = ['이 유튜브 채널은 어떠세요? https://www.youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A',
          '이 유튜브 채널은 어떠세요? https://www.youtube.com/channel/UCDetLsdPIXIHzxUyIWa0LlA',
          '마인크래프트를 해보는 건 어떨까요? 다운:https://www.minecraft.net/ko-kr/', '할게 없을 땐 공부라도 하세요']
players = []
playersid = []
failedplayers = []
start = ['가', '나', '다', '라', '마', '바', '음', '누', '스', '고', '자', '주', '소', '조', '사', '우', '이', '구']
lists = []
token = "ODE2NTQ3NTgzOTgzMjIyNzk2.YD8jMg.JQj3Zl3YyQRJ95rrjbkCiOVt19Y"
isdest = True
channel_id = 881498177700773889


isbad=True
bad = ["씨발", "ㅅㅂ","Tlqkf","미친년","ㅁㅊ", "지랄","ㅈㄹ","ㅆㅂ","ㅗ","새끼","ㅅㄲ","ㅄ","ㅂㅅ","병신","쒸발","야발","tlqkf","rotoRl","alcls","tprtm","시발","시팔","ㅈ같네","자지","섹스","보지"]
lastbad = None
lasttexts = None
lastbadperson = None
lasttextperson = None

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    await client.change_presence(status=discord.Status.offline, activity = discord.Game('상태메시지'))



@client.event
async def on_message(message):
    global isdest
    global isgaming
    global players
    global playersid
    global word
    global cut
    global double
    global doom
    global lists
    global failedplayers
    global reaction_list
    global lastbad
    global lasttextperson
    global lastbadperson
    global lasttexts

    with open('dict.txt', 'r', encoding='UTF-8') as f:
        lists = f.read().splitlines()

    if message.author.bot:
        return None
    print("메시지")
    # if message.author.name=="멘션을 하면 기부니가 좋아지는 란토":
    # return
    def checkend(mg):
        global doom
        global word
        global lists
        global isgaming
        global cut
        if not isgaming:
            raise ValueError("isn't gameing")
        isex = False
        if mg.author.name == now and len(mg.content) > 1:
            if mg.content.startswith( word[0]) or mg.content.startswith(word[1]):
                ho = mg.content
                hod = ho[len(ho) - 1]
                for st in doom:
                    if st[0] == word[0]:
                        word[1] = st[1]
                for txt in lists:
                    if txt[0] == hod:
                        isex = True
                        break
                if ho in lists and not ho in double:
                    if not cut:
                        if isex:
                            double.append(ho)

                            return True
                        else:
                            print("한방")
                    else:
                        double.append(ho)
                        return True

                else:
                    print("사전에 단어가 없거나 중복")
            else:
                print("시작이 다름")

        print("사람이 다름")
        return False
    if message.content == '코딩':
        channel = message.channel
        await channel.send('python 3.9')

    if message.content == '숙제 보여줘':
        channel = message.channel
        await channel.send('숙제는 자기가 챙겨야지')

    if message.content == '김기오 바보':
        channel = message.channel
        await channel.send('응 아니야')

    if message.content == '비밀':
        channel = message.channel
        await channel.send('제작자:킹갓 울트라 캡슝 김기오&ZiZon이예준')

    if message.content.endswith('도움말') or message.content.startswith('도움말'):
        channel = message.channel
        embed = discord.Embed(title="   ", color=0x008a35)
        embed.set_author(name="도움말")
        embed.add_field(name="숙제 보여줘", value="숙제 보여줌", inline=False)
        embed.add_field(name="김기오 바보", value="비밀", inline=False)
        embed.add_field(name="이학습터", value="이학습터 바로가기", inline=False)
        embed.add_field(name="비밀", value="궁금하면 해봐", inline=False)
        embed.add_field(name="심심해 또는 심심하다", value="심심할 때 처보3", inline=False)
        embed.add_field(name="코딩", value="코딩 정보 알려줌", inline=False)
        embed.add_field(name="ㄱㄱ", value="끝말잇기 참가/시작", inline=False)
        embed.add_field(name="ㅇㅈ", value="유저 확인", inline=True)
        embed.add_field(name="ㅍㄱ", value="방 파괴(방장만 가능)", inline=False)
        embed.add_field(name="Made by", value="WibaWiba & 이에준", inline=False)
        await channel.send(embed=embed)

    if message.content.endswith('아하') or message.content.endswith('ㅇㅎ') or message.content.startswith(
            '아하') or message.content.startswith('ㅇㅎ'):
        channel = message.channel
        await channel.send('알기는 뭘 알아')

    if message.content == '심심해' or message.content == '심심하다' or message.content.startswith('심심하네'):
        channel = message.channel
        await channel.send(random.choice(things))
    if message.content == '야':
        await message.channel.send('뭐')

    # 끝말 코드
    dan = ''
    add = ''

    a = len(players)
    if message.content == 'ㅍㄱ' or message.content == '파괴':
        i = a + 1
        channel = message.channel
        if len(players) == 0:
            channel = message.channel
            await channel.send('진행중인 게임이 없습니다.')
        else:
            channel = message.channel
            if message.author.name == players[0]:
                players.clear()
                playersid.clear()
                isdest = True
                await channel.send('끝말잇기 방을 파괴했습니다.')
                isgaming = False

            elif message.author.name == '이예준':
                players.clear()
                playersid.clear()
                isdest = True
                isgaming = False
                await channel.send('이예준님의 요청으로 끝말잇기 방을 파괴했습니다.')

            else:
                channel = message.channel
                await channel.send('방 파괴는 방장만 가능합니다.')
    if message.content == "한방막기":
        if not isgaming and not isdest:
            if players[0] == message.author.name:
                await message.channel.send("한방단어를 비활성화 했습니다.")
                cut = False
            else:
                await message.channel.send("설정은 방장만 가능합니다.")
        elif isgaming:
            await message.channel.send("게임중에는 설정할 수 없습니다.")
        else:
            await message.channel.send("설정할 게임이 없습니다.")
    if message.content == "한방허용":
        if not isgaming and not isdest:
            if players[0] == message.author.name:
                await message.channel.send("한방단어를 활성화 했습니다.")
                cut = False
            else:
                await message.channel.send("설정은 방장만 가능합니다.")
        elif isgaming:
            await message.channel.send("게임중에는 설정할 수 없습니다.")
        else:
            await message.channel.send("설정할 게임이 없습니다.")
    if message.content == "옵션":
        embed = discord.Embed(title="끝말읻기 옵션", description="명령어")
        embed.set_author(name="도움")
        embed.add_field(name="한방 막기(키고 끄기)", value="[한방허용]", inline=True)
        embed.add_field(name="기본 한방 막기", value="[한방막기]", inline=True)
        await message.channel.send(embed=embed)

    if message.content == 'ㄱㄱ' or message.content == 'ㄲ':
        if not isgaming :
            i = 0
            soo = 0
            add = message.author.name
            mention = '<@'+str(message.author.id)+'>'
            channel = message.channel
            if a == 0 and isdest:
                isdest = False
                players.append(message.author.name)
                playersid.append(message.author.id)
                await channel.send(mention + '님이 끝말잇기 게임을 만드셨습니다.참가하시려면 [ㄱㄱ]를 입력해 주세요.')
                await channel.send("방장은 [옵션] 명령어를 통해 옵션설정이 가능합니다")
                i = 0
                soo = len(players)
                embed = discord.Embed(title="   ", color=0x008a35)
                for soo in players:
                    embed.add_field(name="플레이어", value=players[i], inline=False)
                    i += 1
                await channel.send(embed=embed)
                sec = 120
            elif add == players[0]:
                if a > 1 and not isdest:
                    word[0] = random.choice(start)
                    double.clear()
                    await channel.send('게임을 시작합니다! ' + mention + '님은 20초 안에 [' + word[0] + ']으로 시작하는 단어를 입력해주세요.')
                    isgaming = True
                    i = 0
                    embed = discord.Embed(title="   ", color=0x008a35)
                    for soo in players:
                        embed.add_field(name="플레이어", value=players[i], inline=False)
                        i += 1
                    await channel.send(embed=embed)
                    i = 0
                    failedplayers.clear()
                    mes = message.content
                    playernum = len(players)
                    while True:
                        if isdest: return
                        now = players[i % playernum]
                        isnot = False
                        try:
                            mg = await client.wait_for('message', timeout=20.0, check=checkend)
                            if isdest: return
                            i += 1
                            if i>99:
                                await mg.add_reaction(reaction_list[int(i/100)])
                                await mg.add_reaction(reaction_list[int((i% 100)/10)])
                                await mg.add_reaction(reaction_list[((i % 100) % 10)])
                            elif  i>9:
                                await mg.add_reaction(reaction_list[int(i/10)])
                                await mg.add_reaction(reaction_list[i % 10])
                            else:
                                await mg.add_reaction(reaction_list[i])

                        except:
                            if isdest: return
                            if isgaming:
                                await channel.send("<@"+str(playersid[i % playernum]) + '>님이 시간초과로 인하여 탈락하셨습니다.')
                                failedplayers.append(now)
                                isnot = True
                                del players[i % playernum]
                                del playersid[i % playernum]
                                playernum -=1
                                if playernum == 1:
                                    isgaming = False
                                    twinner = players[0]
                                    embed = discord.Embed(title="랭킹", color=0x008a35)
                                    embed.add_field(name="1위", value=twinner, inline=False)
                                    rank=2
                                    for play in reversed(failedplayers):
                                        embed.add_field(name=str(rank)+"위", value=play, inline=False)
                                        rank += 1
                                    await channel.send(embed=embed)
                                    isgaming = False
                                    await channel.send('게임을 종료되었습니다.')
                                    players.clear()
                                    playersid.clear()
                                    isdest = True

                                    return
                            else:
                                return
                        if isdest: return
                        if not isnot:
                            ho = mg.content
                            await channel.send(now + '님이[' + ho + ']를 입력하셨습니다.')
                            word[0] = ho[len(ho) - 1]
                            word[1] = ' '
                            for doomb in doom:
                                if doomb[0] == word[0]:
                                    word[1] = doomb[1]
                        if isdest: return
                        if word[1] == ' ':
                            await channel.send("<@"+str(playersid[i % playernum]) + '>님은 20초 안에 [' + word[0] + ']로 시작하는 단어를 써주세요.')
                        else:
                            await channel.send("<@"+str(playersid[i % playernum]) + '>님은 20초 안에 [' + word[0] + ']또는 [' + word[
                                1] + ']로 시작하는 단어를 써주세요.')


                else:
                    if isdest: return
                    await channel.send(add + '님, 혼자서는 게임을 진행 할 수 없습니다')

            else:
                if isdest: return
                if add in players:
                    await channel.send(add + '님은 이미 참가하셨습니다.')
                elif isgaming :
                    await channel.send("이미 게임이 시작되었습니다.")
                else:
                    await channel.send(add + '님이 참가하셨습니다.')
                    i = 0
                    soo = len(players)
                    players.append(message.author.name)
                    playersid.append(message.author.id)
                    embed = discord.Embed(title="   ", color=0x008a35)
                    for soo in players:
                        embed.add_field(name="플레이어", value=players[i], inline=False)
                        i += 1
                    await channel.send(embed=embed)

        #게임 징행중

    if message.content == 'ㅌㅅㅌ':
        channel = message.channel
        if message.author.name == '이예준' and len(players) > 0:
            players.append("이예준")
            playersid.append(596708010768990209)
            await channel.send('테스트 플레이어(이예준)가 참가했습니다')

        elif message.author.name == '러마' and len(players) > 0:
            players.append("러마")
            playersid.append(709533146034602084)
            await channel.send('테스트 플레이어(러마)가 참가했습니다')

        elif not message.author.name == '이예준' and not message.author.name == '러마':
            await channel.send('관리자만 테스트 플레이어를 추가 할 수 있습니다')
        elif isgaming:
            await channel.send("이미 게임이 시작되었습니다")
    if message.content == 'ㅇㅈ':
        i = 0
        channel = message.channel
        if len(players) == 0:
            channel = message.channel
            await channel.send('진행중인 게임이 없습니다.')
        else:
            channel = message.channel
            soo = len(players)
            embed = discord.Embed(title="   ", color=0x008a35)
            for soo in players:
                embed.add_field(name="플레이어", value=players[i], inline=False)
                i += 1
            await channel.send(embed=embed)
    if message.content.startswith("."):
        channel = message.channel
        if message.content.split('.')[1] in lists:
            await channel.send("있는단어")
        else:
            await channel.send("없는단어")


client.run('ODgxNDk4MTc3NzAwNzczODg5.GZoWrC.7_jlReSWm8PR6lmF3Je9paizV9VHI_LjuvVZZU')


