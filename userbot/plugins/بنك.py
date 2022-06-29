# الملف عائد لجيبثون
# By : @Jepthon
# edit : Dragon - @S_L_3
import time
import re
from ..Config import Config
from ..sql_helper.bank import add_bank, del_bank, get_bank, update_bank, des_bank
from telethon import Button, events
import glob, os
import os.path
from ..helpers import get_user_from_event
from telethon import types
from random import randint
import random
from . import jmthon
from ..core.managers import edit_delete, edit_or_reply

import asyncio

plugin_category = "utils"
#----Timers----#
t = {}
#--------------#
def convert(seconds): 

    seconds = seconds % (24 * 3600) 

    seconds %= 3600

    minutes = seconds // 60

    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)

@jmthon.ar_cmd(pattern="tdata")

async def td(event):
    return await edit_or_reply(event, str(t))

@jmthon.ar_cmd(pattern="توب الفلوس(.*)")
   
async def d(message):
    users = des_bank()
    if not users: 
        return edit_or_reply(message, "لا يوجد حسابات في البنك")
    list = '**قائمة اغنى عشرة في السورس**\n'
    count = 0
    for i in users:
        count += 1
        list += f'**{count} -** [{i.first_name}](tg://user?id={i.user_id}) {i.balance} 💵\n'
        
    await edit_or_reply(message, list)
    return await edit_or_reply(message, str(des_bank()))

@jmthon.ar_cmd(pattern="حذف حسابي بنكي(.*)")
   
async def d(message):
    me = await message.client.get_me()
    acc = get_bank(me.id)
    if acc is None:
        await edit_delete(message, "᥀︙لا تملك حساب بنكي لحذفه")
    else:
        row = del_bank(me.id)
        await message.delete()
        await message.client.send_message(message.chat_id, "᥀︙ تم حذف حسابك بنكي")

@jmthon.ar_cmd(
    pattern=" انشاء حساب بنكي(?:\s|$)([\s\S]*)",
    command=("انشاء حساب بنكي", plugin_category),
)
async def start(event):
    me = await event.client.get_me()
    sta = await edit_or_reply(event, f"""</strong>

👋  {me.first_name} مرحبًا
 ━━━━━━━━━━━━━━━━━
- لأنشاء حساب اختر احد البنوك الاتية

- ᥀︙انشاء حساب البنك الدولي

- ᥀︙ انشاء حساب مصرف ترند بنكي
 ━━━━━━━━━━━━━━━━━

</strong>""",parse_mode="html")



@jmthon.on(admin_cmd(pattern="(فلوسي|اموالي) ?(.*)"))
async def a(message):
    me = await message.client.get_me()
    if get_bank(me.id) is None:
         noa = await edit_or_reply(message, f"<strong>انت لا تملك حساب في المصرف</strong>", parse_mode="html")
    else:
         acc = get_bank(me.id)
         mo = int(acc.balance)
         ba = await edit_or_reply(message,f"<strong>فلوسك : {mo}  💵</strong>",parse_mode="html")



@jmthon.on(admin_cmd(pattern="(بنكي|مصرفي) ?(.*)"))
async def myb(message):

    me = await message.client.get_me()
    
    if get_bank(me.id) is not None:
         acc = get_bank(me.id)
         nn = acc.first_name
         balance = acc.balance
         ba = acc.bank
         ifn = f"""
- ================= -
᥀︙ الاسم : {nn} 
᥀︙ رقم الحساب : {me.id} 
᥀︙ الفلوس : {balance} 💵
᥀︙ اسم البنك : {ba} 
- ================= -
          """
         acinfo = await edit_or_reply(message,f"<strong>{ifn}</strong>",parse_mode="html")

    else:
         ca = await edit_or_reply(message,f"<strong>ليس لديك حساب في المصرف!</strong>",parse_mode="html")


@jmthon.ar_cmd(func=lambda m:"راتب")
async def ga(message):
    mee = await message.client.get_me()
    ms = message.text
    acc = get_bank(mee.id)
 
    if ms == ".البنك" or ms == ".المصرف" or ms == ".مصرف":


        help = """
        .انشاء حساب (لانشاء حساب بنكي)
᥀︙ - مثال: .انشاء حساب البنك الدولي او ترند بنكي
᥀︙ 1 - .استثمار (مبلغ) 
᥀︙ - مثال : استثمار 18276
᥀︙ 2 - .حظ (المبلغ)
᥀︙ - مثال : حظ 17267
᥀︙ 3 - .راتب ( - يعطيك راتب كل 10 دقائق )
᥀︙ 4 - .كنز ( - يعطيك كنز كل 10 دقائق )
᥀︙ 5 - .بخشيش ( يعطيك بخشيش كل 10 دقائق )
᥀︙ 6 - .فلوسي | لرؤية فلوسك
᥀︙ 7 - .بنكي او .مصرفي | لاضهار معلومات حسابك في المصرف
᥀︙ وهذه هي كل الاوامر : @VV399

      """
#edit Dragon - ↯ @S_L_3

        hr = await edit_or_reply(message,f"<strong>{help}</strong>",parse_mode="html")


    if ms == ".كنز":
        if "كنز" in t:
              tii = t["كنز"] - time.time()
              return await edit_or_reply(message,"<strong> ليس هنالك كنز لقد اخذته بالفعل انتضر {}</strong>".format(convert(tii)),parse_mode="html")
           #edit Dragon - ↯ @S_L_3   
     
        else: #edit drgoon - ↯ @S_L_3
              rt = randint(50,3000)
              acca = get_bank(mee.id).balance
              ga = int(rt) + int(acca)
              update_bank(mee.id, ga)
              tx = await edit_or_reply(message,f"<strong>💸 لقد حصلت على الكنز!🤩\n- حصلت على {rt} 💵.\n- فلوسك الان : {ga} 💵 .</strong>",parse_mode="html")
              t["كنز"] = time.time() + 600 
              await asyncio.sleep(600)
              del t["كنز"]
     
    if ".استثمار" in ms:
        value = message.text.replace(".استثمار","")
        if "استثمار" in t:
            ti2 = t["استثمار"] - time.time()
            return await edit_or_reply(message,"<strong> للاستثمار مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")
        lss = ["Done","Fail"]
        ls = random.choice(lss)
        ppe = acc.balance
        if int(value) > int(ppe):
            return await edit_delete(message, "<strong>! انت لا تملك هذا القدر من الفلوس للاستثمار</strong>", parse_mode="html")
        isv = value.isnumeric()
        if not isv:
         return await edit_delete(message, "<strong>!ادخل رقم صالِح للاستثمار</strong>", parse_mode="html")
        if "Done" in ls:
            kf = int(value) + int(randint(int(ppe),int(ppe)))
            update_bank(mee.id, kf)
            d = ["1%","2%","4%","8%","9%"]
            ra = random.choice(d)
            ma = await edit_or_reply(message,f"""<strong>
===================
᥀︙ استثمار ناجح  💰
᥀︙ نسبة الربح  ↢ {ra}
᥀︙ مبلغ الربح  ↢ ( {ppe} 💵 )
᥀︙ فلوسك الان  ↢ ( {kf}  💵 )
===================
</strong>""",parse_mode="html")
            t["استثمار"] = time.time() + 600
            await asyncio.sleep(600)
            del t["استثمار"]
        if "Fail" in ls:
             await edit_or_reply(message, "استثمار فاشل لم تحصل على اي ارباح")
             t["استثمار"] = time.time() + 600
             await asyncio.sleep(600)
             del t["استثمار"]
             

    if f".حظ"in message.text:
        value = message.text.replace(".حظ","")
        ppe = acc.balance
        if "حظ" in t:
            ti2 = t["حظ"] - time.time()
            return await edit_or_reply(message,"<strong> للعب الحظ مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")

        if int(value) > int(ppe):
            return await edit_delete(message, "<strong>! انت لا تملك هذا القدر من الفلوس للحظ</strong>", parse_mode="html")
        ls = ["Done","Fail"]
        sv = random.choice(ls)
        if "Done" in sv:
        
            kf = int(value) + int(randint(int(ppe),int(ppe)))
            update_bank(mee.id, kf)
            cong = await edit_or_reply(message,f"""<strong>          
======================
᥀︙ مبروك لقد ربحت بالحظ 🥳
᥀︙ فلوسك السابقة  ↢ ( {ppe}  💵 ) .
᥀︙ فلوسك الان  ↢ ( {kf}  💵 ) .
======================
</strong>""",parse_mode="html")
            t["حظ"] = time.time() + 600
            await asyncio.sleep(600)
            del t["حظ"]
        else:
            pa = acc.balance
            pop = int(pa) - int(value)
            update_bank(mee.id, pop)
            heh = await edit_or_reply(message,f"""<strong>
=======================
😕 لسوء الحظ , خسرت في الحظ ᥀︙
- ᥀︙ فلوسك السابقة  ↢ ( {pa} 💵 )  
- ᥀︙ فلوسك الان  ↢ ( {pop} 💵 ) .
========================
</strong>""",parse_mode="html")

            t["حظ"] = time.time() + 600
            await asyncio.sleep(600)
            del t["حظ"]
    if ms == ".بخشيش":
        ppe = acc.balance
        if "بخشيش" in t:
            ti2 = t["بخشيش"] - time.time()
            return await edit_or_reply(message,"<strong> لقد اخذت بخشيش انتضر {}</strong>".format(convert(ti2)),parse_mode="html")
        else:
              rt = randint(70,2000)
              ga = int(rt) + int(ppe)
              tp = await edit_or_reply(message,f"<strong>=================\n- •تم ايداع البخشيش 💸\n- • حصلت على  {rt} 💵.\n- • فلوسك الان : {ga} 💵\n=================</strong>",parse_mode="html")
              update_bank(mee.id, ga)
              t["بخشيش"] = time.time() + 600
              await asyncio.sleep(600)
              del t["بخشيش"]
    
    if ms == ".راتب":
        ba = acc.balance
        if "راتب" in t:
            ti2 = t["راتب"] - time.time()
            return await edit_or_reply(message,"<strong> لأخذ راتب مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")

        else:


              list = ["مبرمج 💻-1000","ملك 🤴-10000","قاضي 👨‍⚖-20000","عامل 🧑‍🔧-1000","روبوت 🤖-2300","سائق 🚓-4000","تاجر مخدرات 🚬-5000","تاجر اسلحة 🔫-9000","طيار ✈️-7000","قبطان 🛳-8000"]

              rt = random.choice(list)
              name = rt.split("-")[0]
              ratb = rt.split("-")[1]
              ga = int(ratb) + int(ba)
              update_bank(mee.id, ga)
              sal = await edit_or_reply(message,f"<strong>==================\n- • تم ايداع راتبك! 💸🤩\n- • حصلت على {ratb} 💵\n- • لأنك {name}.\n- • فلوسك الان : {ga} 💵 \n==================</strong>",parse_mode="html")
              t["راتب"] = time.time() + 600
              await asyncio.sleep(600)
              del t["راتب"]

@jmthon.ar_cmd(
    pattern="زرف(?:\s|$)([\s\S]*)",
    command=("زرف", plugin_category),
)
async def thief(message):
    mee = await message.client.get_me()
    user, custom = await get_user_from_event(message)
    accu = get_bank(user.id)
    acc = get_bank(mee.id)
    if "زرف" in t:
        ti2 = t["زرف"] - time.time()
        return await edit_or_reply(message,"<strong> لقد زرفت قبل قليل انتظر {}</strong>".format(convert(ti2)),parse_mode="html")
    else:
        if not user:
            return await edit_or_reply(message,"<strong> يجب عليك الرد على شخص لزرفته </strong>", parse_mode="html")
        if get_bank(user.id) is None:
            return await edit_or_reply(message,"<strong> لا يمكنك زرفة شخص لا يمتلك حساب بنكي </strong>", parse_mode="html")
        if get_bank(mee.id) is None:
            return await edit_or_reply(message,"<strong> لا يمكنك الزرفة لانك لا تملك حساب بنكي </strong>", parse_mode="html")
        if int(accu.balance) < 2000:
           return await edit_or_reply(message,"<strong> لا يمكنك زرفته لان امواله اقل من 2000$ </strong>", parse_mode="html")
    rt = randint(70,2000)
    ppe = int(acc.balance)
    be = int(accu.balance)
    jep = int(be) - int(rt)
    update_bank(user.id, jep)
    jepthon = mee.first_name.replace("\u2060", "") if mee.first_name else mee.username
    ga = int(rt) + int(ppe)
    update_bank(mee.id, ga)
    await jmthon.send_file(
                message.chat_id,
                "https://telegra.ph/file/45735f4cfa1bd527abc31.jpg",
                caption=f"زرف [{jepthon}](tg://user?id={mee.id}) من [{user.first_name}](tg://user?id={user.id})\n المبلغ: {rt} 💵",
                )
    t["زرف"] = time.time() + 600
    await asyncio.sleep(600)
    del t["زرف"]
    
    
@jmthon.ar_cmd(pattern="انشاء حساب  بنكي(.*)")
async def bankar(message):
    input = message.pattern_match.group(1)
    mee = await message.client.get_me()
    if get_bank(mee.id) is not None:
        return await edit_or_reply(message, f"<strong>لديك حساب بنكي بالفعل</strong>",parse_mode="html")
    if input == "ترند بنكي":
        bankn = "مصرف ترند بنكي"
    elif input == "البنك الدولي":
    	bankn = "البنك الدولي"
    elif input != "البنك الدولي" or "ترند بنكي":
         return await edit_or_reply(message, "᥀︙لا يوجد هكذا مصرِف !")
    add_bank(mee.id, mee.first_name, 50, bankn)
    cbs = await edit_or_reply(message,f"<strong>تم انشاء حساب بنكي بالمعلومات التالية:\nاسم صاحب الحساب:{mee.first_name}|\nايدي الحساب:{mee.id}|\nاسم البنك:{bankn}|\nالفلوس المودوعة:50$</strong>", parse_mode="html")
