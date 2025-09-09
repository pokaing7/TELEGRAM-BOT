from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# /start command ka response
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Match start ho gaya! 🏏⚽\nKesa ha kutta? 😂")

# Agar koi message bheje jisme "match" ho
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "match" in text:
        await update.message.reply_text("Match chal raha hai bhai... Kesa ha kutta? 😆")
    else:
        await update.message.reply_text("Samajh nahi aaya 🤔 'match' likho.")

def main():
    # ⚠️ Apna BotFather se liya hua token yaha daalna
    TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

    app = Application.builder().token(TOKEN).build()

    # Command handler (/start)
    app.add_handler(CommandHandler("start", start))
    # Message handler (normal text)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
