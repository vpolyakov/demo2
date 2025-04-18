import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define trading hours for exchanges
TRADING_HOURS = {
    "NYSE": "9:30 AM - 4:00 PM (EST)",
    "NASDAQ": "9:30 AM - 4:00 PM (EST)",
    "LSE": "8:00 AM - 4:30 PM (GMT)",
    "JPX": "9:00 AM - 3:00 PM (JST)",
}

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Send /hours <exchange> to get trading hours.")

# Hours command handler
def hours(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text("Please specify an exchange. Example: /hours NYSE")
        return

    exchange = context.args[0].upper()
    if exchange in TRADING_HOURS:
        update.message.reply_text(f"Trading hours for {exchange}: {TRADING_HOURS[exchange]}")
    else:
        update.message.reply_text(f"Sorry, I don't have trading hours for {exchange}.")

# Main function to start the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("YOUR_BOT_TOKEN")
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("hours", hours))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()