import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        keyboard = [
            [InlineKeyboardButton("DAFTAR SEKARANG", url="https://google.com")],
            [InlineKeyboardButton("PREDIKSI AKURAT", url="https://google.com")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

       await update.message.reply_text(
    f"Salam hangat dan selamat datang {member.first_name}! 👋\n\n"
    "Terima kasih telah bergabung di PETIRJITU OFFICIAL.\n\n"
    "🎁 Informasi bonus & promo\n"
    "⚡ Prediksi akurat setiap hari\n\n"
    "Tekan tombol di bawah untuk melanjutkan.",
    reply_markup=reply_markup
)

        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

print("Bot is running...")
app.run_polling()
