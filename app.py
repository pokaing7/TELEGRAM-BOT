from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from urllib.parse import urlparse

# /start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 Please enter your website link:")

# Function to handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # Parse the URL
    parsed_url = urlparse(text)
    if parsed_url.netloc:  # agar domain mila
        await update.message.reply_text(f"✅ Shortcut: {parsed_url.netloc}")
    else:
        await update.message.reply_text("❌ Invalid link! Please send a valid website link (e.g., https://example.com)")

def main():
    # ⚠️ Yaha apna BotFather se liya hua TOKEN paste karo
    TOKEN = "8326515238:AAHYELSxlG7NL9ev9ZGcypumpZtE1OI-cKU"

    # Bot application start
    app = Application.builder().token(TOKEN).build()

    # Command aur message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run bot
    print("🤖 Bot is running... Press CTRL+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()