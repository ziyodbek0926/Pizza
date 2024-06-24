from dotenv import load_dotenv
import os

from telegram.ext import (
    Updater, 
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)

from handlers import (
    start,
    about,
    feedback,
    star5,
    language,
    choose_language,
    star3,
    star4,
    maxsulotlar_uchun
    
)


# getting the token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

# create updater object
updater: Updater = Updater(token=TOKEN)

# create dispatcher object
dispatcher: Dispatcher = updater.dispatcher


# create main function
def main():
    # add the message handlers to the dispatcherhandlers
    dispatcher.add_handler(handler=CommandHandler(command="start", callback=start))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("😊Menga hamma narsa yoqdi, 5 ❤️"), callback=star5))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️"), callback=star4))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🙂Qoniqarli, 3 ⭐️⭐️⭐️"), callback=star3))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("😐Qoniqarsiz, 2 ⭐️ ⭐️"), callback=star3))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("😡Yomon, 1 ⭐️"), callback=star3))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("ℹ️ Ma'lumot"), callback=about))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🔥 Mahsulotlar"), callback=maxsulotlar_uchun))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("✍️ Izoh qoldirish"), callback=feedback))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🌐 Tilni tanlash"), callback=language))

    # add the callback query handlers to the dispatcher
    dispatcher.add_handler(handler=CallbackQueryHandler(callback=choose_language))

    # start the bot
    updater.start_polling()
    updater.idle()


# run the main function
if __name__ == "__main__":
    main()
