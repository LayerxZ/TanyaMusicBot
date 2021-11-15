import asyncio
from pyrogram import Client as Bot
from pytgcalls import idle
from database.functions import clean_restart_stage
from database.queue import (get_active_chats, remove_active_chat)
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

async def load_start():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[INFO]: SENDING RESTART STATUS")
        try:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted the Bot Successfully.**",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        print("Error came while clearing db")
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)                                         
        except Exception as e:
            print("Error came while clearing db")
            pass     
    print("[INFO]: STARTED")
    
   
loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
run()
idle()
loop.close()
