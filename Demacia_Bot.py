import discord
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    #대화
    if message.content.startswith("/데마시아"):
        await message.channel.send("데마시아 봇 도움말")
        await message.channel.send("모든 명령어는 앞에 /를 붙여주세요")
        await message.channel.send("- 옵쥐 : OP.GG 링크")
        await message.channel.send("- 전적 (닉네임) : 전적 검색하기 - 닉네임 띄어쓰기X")
        await message.channel.send("- 챔 (챔피언 이름) : 챔피언 정보 검색하기 - 챔피언 이름 띄어쓰기X")
        await message.channel.send("- 롤체 (닉네임) : 롤토체스 전적 검색하기 - 닉네임 띄어쓰기X")
        await message.channel.send("- LCK : LCK 유튜브 링크")
        await message.channel.send("2020-03-20")

    if message.content.startswith("/옵쥐"):
        await message.channel.send("https://www.op.gg/")

    if message.content.startswith("/전적"):
        nick = message.content[4:]
        await message.channel.send("https://www.op.gg/summoner/userName="+(nick))

    if message.content.startswith("/챔"):
        cham = message.content[3:]
        await message.channel.send("https://www.op.gg/champion/"+(cham)+"/statistics")

    if message.content.startswith("/롤체"):
        nick = message.content[4:]
        await message.channel.send("https://lolchess.gg/profile/kr/"+(nick))

    if message.content.startswith("/LCK"):
        await message.channel.send("https://www.youtube.com/channel/UCw1DsweY9b2AKGjV4kGJP1A/featured")


    #이미지 업로드
    if message.content.startswith("/이미지"):
        img = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(img))

    #특정 채널에 메시지 보내기
    #/채널메시지 (채널코드) (할말)
    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    #DM보내기
    #/dm (유저ID) (할말)
    if message.content.startswith("/dm"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    #역할변경
    if message.content.startswith("/벌레"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="벌레")
        await author.add_roles(role)

    if message.content.startswith("/면죄"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="벌레")
        await author.remove_roles(role)

    #경고
    if message.content.startswith("/경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고 2회 누적입니다. 서버에서 추방됩니다.")
                else:
                    await message.channel.send("경고를 1회 받았습니다.")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author.id)
                sheet["B" + str(1)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1회 받았습니다.")
                break
            i += 1

client.run("Njg1NDU1MzExMTUwMjUyMDQy.XnCXwg.lqkgHsWpueWg0A-SXCtHrL3jrKo")