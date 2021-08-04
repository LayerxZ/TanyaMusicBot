from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from config import BOT_USERNAME
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CVEgMTAACE81hCsnWvf_ao9aBzJAhgUX08F9MBgAC7wEAAl7AKFSrtnT4_eRctSAE")
    await message.reply_text(
        f"""**👋🏻 Hello, My name is {bn} ✨

Powered by [UserLazy](https://UserLazyXBot).

want play music on vcg?, add me to your group.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ADD TO YOUR GROUP ➕", url="https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🌻 GROUP SUPPORT 🌻", url="https://t.me/OdaSupport"
                    ),
                    InlineKeyboardButton(
                        "🌸 UPDATES CHANNEL 🌸", url="https://t.me/UserLazyXBot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 DONATION", url="https://t.me/RxyMX"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ music player is online.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 CHANNEL 🌸", url="https://t.me/UserLazyXBot")
                ]
            ]
        )
   )


