from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**👋🏻 halo, saya adalah {bn} ✨

saya dapat memutar musik di voice chat group anda dengan mudah.
dikelola oleh [Levina](https://t.me/dlwrml).

ingin memutar musik di vcg?, tambahkan saya ke grup anda.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ADD TO YOUR GROUP ➕", url="https://t.me/veezmusicbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🌻 GROUP SUPPORT 🌻", url="https://t.me/gcsupportbots"
                    ),
                    InlineKeyboardButton(
                        "🌸 UPDATES CHANNEL 🌸", url="https://t.me/levinachannel"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 DONATION", url="https://t.me/dlwrml"
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
                        "🌸 CHANNEL 🌸", url="https://t.me/levinachannel")
                ]
            ]
        )
   )


