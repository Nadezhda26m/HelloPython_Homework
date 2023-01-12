from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, CallbackQueryHandler)
# from HW023_requisite import bot_token
from HW023_requisite2 import bot_token
from HW023_bot_command import *

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def message(update, context):
    if update.message.text == 'Том':
        context.bot.send_message(update.effective_chat.id, 'Привет, Том! Я ждал тебя!')
    else:
        context.bot.send_message(update.effective_chat.id, 'Ты не Том. Уходи!')

def unknown_command(update, context):
    msg = update.message.text
    msg = msg.split()
    if msg[0] == '/start':
        pass
    elif msg[0] == '/fileshow':
        pass
    elif msg[0] == '/addrecord':
        pass
    elif msg[0] == '/help':
        pass
    else:
        context.bot.send_message(update.effective_chat.id,
                                 'Я еще юн, такой команды не знаю')


def button(update, context):
    query = update.callback_query
    variant = query.data
    query.answer()
    # query.edit_message_text(text=f"Выбранный вариант: {variant}")
    if variant == '1':
        text_file = 'Колонка TO DO >\n'
        text_file += kanban.read_all_file_string('HW023_to_do.txt')
        context.bot.send_message(update.effective_chat.id, text_file)
    elif variant == '2':
        text_file = 'Колонка DOING >\n'
        text_file += kanban.read_all_file_string('HW023_doing.txt')
        context.bot.send_message(update.effective_chat.id, text_file)
    elif variant == '3':
        text_file = 'Колонка CHECK >\n'
        text_file += kanban.read_all_file_string('HW023_check.txt')
        context.bot.send_message(update.effective_chat.id, text_file)
    elif variant == '4':
        text_file = 'Колонка DONE >\n'
        text_file += kanban.read_all_file_string('HW023_done.txt')
        context.bot.send_message(update.effective_chat.id, text_file)


# передает созданную команду боту
dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(CommandHandler('fileshow', file_show_command))
dispatcher.add_handler(CommandHandler('addrecord', add_record_command))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))
dispatcher.add_handler(MessageHandler(Filters.text, message))
dispatcher.add_handler(CallbackQueryHandler(button))


updater.start_polling()
updater.idle()


