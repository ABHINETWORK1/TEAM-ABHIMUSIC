from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm SNEHABHI MUSICπ΅

I can play music in your group's voice call. Developed by [ABHISHEK & SNEHU](https://t.me/SNEHABHI_SERVER).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π  Source Code π ", url="https://t.me/SNEHABHI_SERVER")
                  ],[
                    InlineKeyboardButton(
                        "π¬ Group", url="https://t.me/SNEHABHI_SERVER"
                    ),
                    InlineKeyboardButton(
                        "π Channel", url="https://t.me/ABHI_NETWORK1"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "β Add To Your Group β", url="https://t.me/SNEHU_IS_MINE")
                ],[
                    InlineKeyboardButton(
                        "π«πΎππ½π΄π πππ΄π΄π½β¨", url="HTTP://T.ME/ABHI_IS_MINE")
                ],[
                    InlineKeyboardButton(
                        "π«πΎππ½π΄π πΊπΈπ½πΆβ¨", url="HTTP://T.ME/SNEHU_IS_MINE"
                    )]
                ]
            ),
     disable_web_page_preview=True
    )
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**SNEHABHI SERVER IS OΙ΄ΚΙͺΙ΄α΄ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πUα΄©α΄α΄α΄α΄s", url="https://t.me/ABHI_NETWORK1")
                ]
            ]
        )
    )
