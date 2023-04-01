from telegram.ext import Updater, CommandHandler

print("Бот запущен. Нажмите Ctrl+C для завершения")

def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я бот")


token = "802414251:AAGGRWasfg8UmXVJPk79zNdjBQG3w33mvGE"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))

updater.start_polling()
updater.idle()



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		number = float(text)
		rate = 80.34
		soms = number * rate
		context.bot.send_message(chat_id=chat.id, text=str(soms) + " сом")
	except:
		context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода")


dispatcher.add_handler(MessageHandler(Filters.all, on_message))


@dp.message_handlers(commands=["start"])

@dp.message_handlers()

