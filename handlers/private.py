from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CXmQRiwABA4gCYVwZZV-lxUmj7LOokgi7yX0khmAAAogDAAKtNIhWkzwOc8A6MJQhBA")
    await message.reply_text(
        f"""**Hey, I'm 𓆩S̾h̾u̾b̾h̾a̾n̾s̾h̾u̾𓆪 MUSIC🎵

I can play music in your group's voice call. Developed by [ABHISHEK](https://t.me/ABHI_NETWORK).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://t.me/greatpersonxd")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/greatpersonxd"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/greatpersonxd"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/greatpersonxd"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** 𓆩S̾h̾u̾b̾h̾a̾n̾s̾h̾u̾𓆪 MUSIC PLAYER IS Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/greatpersonxd")
                ]
            ]
        )
   )


