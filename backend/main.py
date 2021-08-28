import os
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

# run python dotenv
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='سلام به کانال تلگرامی من خوش آمدید')


def main():
    # connect to telegram bto with toke
    token = os.getenv('TOKEN')
    updater = Updater(token)

    # create command in telegram
    start_handler = CommandHandler('start', start)

    # send command to bot
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)

    # with /start bot start again
    updater.idle()


# run main function
if __name__ == '__main__':
    main()
