from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm SNEHABHI MUSIC🎵

I can play music in your group's voice call. Developed by [ABHISHEK](https://t.me/ABHI_NETWORK).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://t.me/ABHI_NETWORK")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/ABHI_NETWORK"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ABHI_NETWORK1"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/SNEHU_IS_MINE"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**SNEHABHI MUSIC PLAYER IS Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ABHI_NETWORK1")
                ]
            ]
        )
   )


