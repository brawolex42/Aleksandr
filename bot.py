
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот 😊")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7833050610:AAFd24xIYBUpzk-Ecpzl7dfK8E6y8oFPcew").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
