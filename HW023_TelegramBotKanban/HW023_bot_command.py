from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, CallbackQueryHandler)
import HW023_kanban_commands as kanban

def start_command(update, context):
    # context.bot.send_message(update.effective_chat.id, 'Привет!')
    update.message.reply_text(f'Привет {update.effective_user.first_name}!')


def file_show_command(update, context):
    keyboard = [
        [InlineKeyboardButton('TO DO', callback_data='1'),
        InlineKeyboardButton('DOING', callback_data='2')],
        [InlineKeyboardButton('CHECK', callback_data='3'),
        InlineKeyboardButton('DONE', callback_data='4')]
    ]
    update.message.reply_text('Какую колонку показать?', reply_markup=InlineKeyboardMarkup(keyboard))

def add_record_command(update, context):
    msg = update.message.text
    len_command = len('/addrecord')
    if len(msg) > len_command + 1:
        file_name = 'HW023_to_do.txt'
        text_file = kanban.read_all_lines_with_numb(file_name)
        size = len(text_file)
        event = msg[len_command + 1:]
        print(event)
        if size > 0:
            last_num = int(text_file[size - 1][0])  # выцепить последний номер
            new_num = '{:03}'.format(last_num + 1)
            kanban.append_new_record(file_name, event, new_num)
        else:
            kanban.append_new_record(file_name, event)
            new_num = '001'
        update.message.reply_text(f'Вы добавили в колонку TO DO событие:\n{new_num} {event}')
    else:
        update.message.reply_text(f'Вы не добавили сообщение\n'
                                  f'Напишите: /addrecord новая запись')

def help_command(update, context):
    update.message.reply_text(f'/start\n/fileshow\n'
                              f'/addrecord новая запись'
                              f'\n/help')

# def move_record_command(update, context):
#     msg = update.message.text
#     print(msg)
#     update.message.reply_text(f'{msg}')
#
# def start(update, context):
#     update.message.reply_text(f'')
















# def get_mode(update, context):
#     keyboard = [
#         [InlineKeyboardButton('Показать данные', callback_data='1')],
#         [InlineKeyboardButton('Добавить запись', callback_data='2')],
#         [InlineKeyboardButton('Переместить запись', callback_data='3')],
#         [InlineKeyboardButton('Изменить запись', callback_data='4')],
#         [InlineKeyboardButton('Удалить запись', callback_data='5')]
#     ]
#     update.message.reply_text('Выбери режим', reply_markup=InlineKeyboardMarkup(keyboard))

# 1 Показать данные
# def get_file_show(update, context):
#     keyboard = [
#         [InlineKeyboardButton('TO DO', callback_data='11'),
#          InlineKeyboardButton('DOING', callback_data='12')],
#         [InlineKeyboardButton('CHECK', callback_data='13'),
#          InlineKeyboardButton('DONE', callback_data='14')]
#     ]
#     update.message.reply_text('Выбери столбик', reply_markup=InlineKeyboardMarkup(keyboard))
#
# mode_handler_show = CommandHandler('getmode', get_file_show)
# dispatcher.add_handler(mode_handler_show)
