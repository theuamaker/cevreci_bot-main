import discord
from discord.ext import commands
import random
import time
from model import error
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba, ismim {bot.user}! Ben bir botum, benim hakkımda daha fazla bilgi için "$yardım" komutunu kullanabilirsin!')

@bot.command()
async def cevre_kirliligi_nasil_onlenir(ctx):
    await ctx.send(f'1- Geri dönüşüm yapilabilir! \n \n Geri Dönüşüm Nasıl Yapılır? \n \n Geri dönüşüm işlemi dört aşamada gerçekleşir, işte bunlardan birisi: \n \n 1- Kaynakta ayrı toplanması \n Değerlendirilebilir atıklar, oluştukları yerde çöplerden ayrılarak biriktirilir. \n \n Ambalaj atıklarının diğer atıklardan ayrı olarak oluştukları yerlerde ayrı olarak biriktirilmesi zorunludur. \n \n 28.12.2017 tarih ve 30283 sayılı Resmi Gazete’de yayımlanarak yürürlüğe giren Ambalaj Atıklarının Kontrolü Yönetmeliği kapsamında, \n \n Ambalaj atığı üreticileri, ambalaj atıklarını, bağlı bulundukları belediyenin ambalaj atıkları yönetim planına uygun olarak, ayrı biriktirmek ve belediyelerce belirlenen şekilde belediyenin toplama sistemine veya atık getirme merkezlerine vermekle yükümlüdür. \n \n Kaynağında ayrı toplama uygulamalarında, tüketicilerin evlerinde ya da işyerlerinde evsel atıklardan ayrı olarak biriktirdikleri ambalaj atıklarının düzenli olarak belediyeler ya da anlaşmalı oldukları Lisanslı Toplama Ayırma Tesisleri tarafından alınması gerekmektedir. \n \n Kaynağında Ayrı Toplama Uygulamalarında, ambalaj atıklarının ayrı toplanabilmesi için konteynır, kumbara, iç mekân kutuları ve geri kazanım torbaları gibi ekipmanlar kullanılmaktadır. \n \n Ben çevreci bot, ve sana yardımcı olduysam bundan büyük mutluluk duyarım \U0001f642')

@bot.command()
async def yardım(ctx):
    await ctx.send("Biraz yardım mı gerekiyor, benim hakkımda daha fazla bilgi için şu komutları kullanabilirsin; \n \n $mim3 - sana 3 numaralı mimi gönderir \n \n $bye - sana emoji gönderir \n \n $cevre_kirliligi_nasil_onlenir - sana çevre kirliliğini önlemek hakkında bilgi verir \n \n $yazitura - yazı-tura oyununu oynamanı sağlar \n \n şimdilik bu kadar, ancak şunu unutma; her an yeni komutlar eklenebilir, bu bot gelişim aşamasında!")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def mim3(ctx):
    with open('aa\images\mim3.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def yazi_tura():
    para = random.randint(0, 1)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"

@bot.command()
async def yazitura(ctx):
    para = yazi_tura()
    await ctx.send("yazı mı tura mı, süren başladı(4sn)")
    time.sleep(4)
    await ctx.send(f"Sonuç: {para}")


@bot.command()
async def upload_image(ctx):
    attachments = ctx.message.attachments
    if attachments:
      #print(files)
        for attachment in attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
        await ctx.send("Dosya yükledi!")
        await ctx.send(error(file_path))
        class_info = error(file_path)
        if class_info[0] == 'syntax error':
            print("Bu hatalar, programlama diline ilişkin bir özelliğin yanlış kullanımından veya en basit şekilde programcının yaptığı yazım hatalarından kaynaklanır. Programcının hataları genellikle SyntaxError şeklinde ortaya çıkar. Bu hatalar çoğunlukla programcı tarafından farkedilir ve program kullanıcıya ulaşmadan önce programcı tarafından düzeltilir. Bu tür hataların tespiti diğer hatalara kıyasla kolaydır. Çünkü bu tür hatalar programınızın çalışmasını engellediği için bunları farketmemek pek mümkün değildir…")

    else:
        await ctx.send("Dosya yüklemedin!")

#söz dizimi    Bu hatalar, programlama diline ilişkin bir özelliğin yanlış kullanımından veya en basit şekilde programcının yaptığı yazım hatalarından kaynaklanır. Programcının hataları genellikle SyntaxError şeklinde ortaya çıkar. Bu hatalar çoğunlukla programcı tarafından farkedilir ve program kullanıcıya ulaşmadan önce programcı tarafından düzeltilir. Bu tür hataların tespiti diğer hatalara kıyasla kolaydır. Çünkü bu tür hatalar programınızın çalışmasını engellediği için bunları farketmemek pek mümkün değildir…

bot.run("MTE0NTA1NDI4NDkxNjk4NTkzNw.Gd8ufP.1SExH5Te7j7kw3kSF3xEUT0OtotfcuKk81zGcE")
