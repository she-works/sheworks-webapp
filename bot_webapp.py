
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s — %(name)s — %(levelname)s — %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Открыть журнал", web_app=WebAppInfo(url="https://sheworks-webapp-git-main-natalies-projects-3099c34b.vercel.app"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в SHE WORKS!", reply_markup=reply_markup)

if __name__ == '__main__':
    app = ApplicationBuilder().token("7733807298:AAE28gdXYWcRViCih6ATgI4iT7KTO8yYFmE").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
