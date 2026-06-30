import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get token from environment variable
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! I'm Photo Fix Bot. 📸\n"
        "I can help you with photo editing and fixes!\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "/about - About this bot"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /help is issued."""
    await update.message.reply_text(
        "🤖 Photo Fix Bot Help\n"
        "Commands available:\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "/about - About this bot\n\n"
        "Send me any message and I'll echo it back!\n"
        "More features coming soon! 🚀"
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /about is issued."""
    await update.message.reply_text(
        "📸 Photo Fix Bot v1.0\n"
        "Built with python-telegram-bot\n"
        "Deployed on Railway 🚀\n"
        "GitHub: @photofix8bot"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    user_message = update.message.text
    await update.message.reply_text(
        f"📝 You said: {user_message}\n\n"
        "I'm your Photo Fix Bot! 📸\n"
        "Send /help to see available commands."
    )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle unknown commands."""
    await update.message.reply_text(
        "❌ Sorry, I don't understand that command.\n"
        "Use /help to see available commands."
    )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    
    # Register message handler for non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Register handler for unknown commands
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the bot (polling)
    logger.info("Photo Fix Bot started! Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
