# Dead module
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# Copyright (C) 2022-2023 by Kakegurui-Domain@Github, < https://github.com/Kakegurui-Domain >.

# This file is part of < https://github.com/theblacklinen/Erina-Ultra-Bot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/theblacklinen/Erina-Ultra-Bot/blob/master/LICENSE >
#
# All rights reserved.
#

import time

from pyrogram import filters
from pyrogram.types import Message

from timi import bot as app
from plugins.Database import add_afk, is_afk, remove_afk

from typing import Union
from datetime import datetime, timedelta

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

cleanmode = {}

async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=5),
    }
    cleanmode[chat_id].append(put)


#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# Copyright (C) 2022-2023 by theblacklinen@Github, < https://github.com/theblacklinen >.

# This file is part of < https://github.com/theblacklinen/Erina-Ultra-Bot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/theblacklinen/Erina-Ultra-Bot/blob/master/LICENSE >
#
# All rights reserved.
#

import time

from pyrogram import filters
from pyrogram.types import Message

from Erina import bot as app
from Erina.Database import add_afk, is_afk, remove_afk

from typing import Union
from datetime import datetime, timedelta

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

cleanmode = {}

async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=5),
    }
    cleanmode[chat_id].append(put)

@app.on_message(filters.command(["afk", f"afk@TimiCuteBot"]))
async def active_afk(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    verifier, reasondb = await is_afk(user_id)
#     if verifier:
#         await remove_afk(user_id)
#         try:
#             afktype = reasondb["type"]
#             timeafk = reasondb["time"]
#             data = reasondb["data"]
#             reasonafk = reasondb["reason"]
#             seenago = get_readable_time((int(time.time() - timeafk)))
#             if afktype == "text":
#                 send = await message.reply_text(
#                     f"**{message.from_user.first_name}** is back online and was away for {seenago}",
#                     disable_web_page_preview=True,
#                 )
#             if afktype == "text_reason":
#                 send = await message.reply_text(
#                     f"**{message.from_user.first_name}** is back online and was away for {seenago}\n\nReason: `{reasonafk}`",
#                     disable_web_page_preview=True,
#                 )
#             if afktype == "animation":
#                 if str(reasonafk) == "None":
#                     send =  await message.reply_animation(
#                         data,
#                         caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}",
#                     )
#                 else:
#                     send = await message.reply_animation(
#                         data,
#                         caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}\n\nReason: `{reasonafk}`",
#                     )
#             if afktype == "photo":
#                 if str(reasonafk) == "None":
#                     send = await message.reply_photo(
#                         photo=f"downloads/{user_id}.jpg",
#                         caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}",
#                     )
#                 else:
#                     send = await message.reply_photo(
#                         photo=f"downloads/{user_id}.jpg",
#                         caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}\n\nReason: `{reasonafk}`",
#                     )
#         except Exception as e:
#             send =  await message.reply_text(
#                 f"**{message.from_user.first_name}** is back online",
#                 disable_web_page_preview=True,
#             )
#         await put_cleanmode(message.chat.id, message.id)
#         return
    if len(message.command) == 1 and not message.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and not message.reply_to_message:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif (
        len(message.command) == 1
        and message.reply_to_message.animation
    ):
        _data = message.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif (
        len(message.command) > 1
        and message.reply_to_message.animation
    ):
        _data = message.reply_to_message.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif (
        len(message.command) == 1 and message.reply_to_message.sticker
    ):
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif (
        len(message.command) > 1 and message.reply_to_message.sticker
    ):
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_afk(user_id, details)
    send = await message.reply_text(
        f"{message.from_user.first_name} is now afk!"
    )
    await put_cleanmode(message.chat.id, message.id)

    
@app.on_message(filters.group & filters.all)
async def afkhandler(_, message: Message):  
    user_id = message.from_user.id
    verifier, reasondb = await is_afk(user_id)
    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                send = await message.reply_text(
                    f"**{message.from_user.first_name}** is back online and was away for {seenago}",
                    disable_web_page_preview=True,
                )
            if afktype == "text_reason":
                send = await message.reply_text(
                    f"**{message.from_user.first_name}** is back online and was away for {seenago}\n\nReason: `{reasonafk}`",
                    disable_web_page_preview=True,
                )
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send =  await message.reply_animation(
                        data,
                        caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}\n\nReason: `{reasonafk}`",
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**{message.from_user.first_name}** is back online and was away for {seenago}\n\nReason: `{reasonafk}`",
                    )
        except Exception as e:
            send =  await message.reply_text(
                f"**{message.from_user.first_name}** is back online",
                disable_web_page_preview=True,
            )
        await put_cleanmode(message.chat.id, message.id)
        return
    
