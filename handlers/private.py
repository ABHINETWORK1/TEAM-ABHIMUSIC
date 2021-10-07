from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm SNEHABHI MUSIC🎵

I can play music in your group's voice call. Developed by [ABHISHEK & SNEHU](https://t.me/SNEHABHI_SERVER).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://t.me/SNEHABHI_SERVER")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/SNEHABHI_SERVER"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ABHI_NETWORK1"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/SNEHU_IS_MINE")
                ],[
                    InlineKeyboardButton(
                        "💫𝙾𝚆𝙽𝙴𝚁 𝚀𝚄𝙴𝙴𝙽✨", url="HTTP://T.ME/ABHI_IS_MINE")
                ],[
                    InlineKeyboardButton(
                        "💫𝙾𝚆𝙽𝙴𝚁 𝙺𝙸𝙽𝙶✨", url="HTTP://T.ME/SNEHU_IS_MINE")
                ]
          ],
     disable_web_page_preview=True
    )



