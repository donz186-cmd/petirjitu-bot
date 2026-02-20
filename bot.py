import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# ==============================
# WELCOME + HAPUS JOIN MESSAGE
# ==============================

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:

        # Hapus notifikasi "joined the group"
        await update.message.delete()

        keyboard = [
            [InlineKeyboardButton("DAFTAR SEKARANG", url="https://tinyurl.com/a6f5dt6e")],
            [InlineKeyboardButton("RTP GACOR 98%", url="https://petirsatu.store/")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo="https://i.postimg.cc/rpnQ8CmW/6.png",
            caption=(
                f"Salam hangat dan selamat datang {member.first_name}! 👋\n\n"
                "Terima kasih telah bergabung di PETIRJITU OFFICIAL.\n\n"
                "🎁 Informasi bonus & promo\n"
                "🚀 RTP 98% SIAP GACOR!\n\n"
                "Tekan tombol di bawah untuk melanjutkan."
            ),
            reply_markup=reply_markup
        )


# ==============================
# ANTI LINK
# ==============================

async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message and message.text:
        text = message.text.lower()

        if "http://" in text or "https://" in text or "t.me" in text or "www." in text:
            await message.delete()
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"⚠️ Link tidak diperbolehkan di grup ini, {message.from_user.first_name}."
            )


# ==============================
# RUN BOT
# ==============================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_links))

print("Bot is running...")
app.run_polling()
