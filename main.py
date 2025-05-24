from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from api import token

TOKEN = token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send me a sticker or GIF, and I will return their ID in a convenient way.")

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.sticker:
        file_id = update.message.sticker.file_id
        reply = f"ID Stiker =\n```\n{file_id}\n```"
        await update.message.reply_text(reply, parse_mode='Markdown')
    elif update.message.animation:
        file_id = update.message.animation.file_id
        reply = f"ID Gif =\n```\n{file_id}\n```"
        await update.message.reply_text(reply, parse_mode='Markdown')
    else:
        await update.message.reply_text("Please send me a sticker or a GIF.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, handle_media))

app.run_polling()
