import telegram
import time
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram import ChatAction
import logging
from functools import wraps
import random
import dictionaries
import constants 
import telebot

bot = telebot.TeleBot('946377958:AAF0BrmVmYPjNtTJUU_fvLkaqYqnI9uYOQc')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    user_markup.row('Practice Tests', 'Книги')
    user_markup.row('Статьи для подготовки', 'Learn Vocabulary Words')
    user_markup.row('For Techers')
    user_markup.row('/help')
    bot.send_message(message.from_user.id, "Чем я могу помочь?", reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.from_user.id, constants.description)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Practice Tests":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Practice Test 1', 'Practice Test 2')
        user_markup.row('Practice Test 3', 'Practice Test 4')
        user_markup.row('Practice Test 5', 'Practice Test 6')
        user_markup.row('Practice Test 7', 'Practice Test 8')
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Выберите Practice Test", reply_markup=user_markup)

    if message.text == "Practice Test 1":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_one)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_one)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_one)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_one)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Practice Test 2":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_two)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_two)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_two)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_two)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Practice Test 3":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_three)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_three)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_three)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_three)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Practice Test 4":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_four)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_four)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_four)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_four)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Practice Test 5":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_five)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_five)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_five)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_five)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Practice Test 6":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_six)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_six)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_six)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_six)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Practice Test 7":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_seven)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_seven)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_seven)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_seven)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Practice Test 8":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_test_button = telebot.types.InlineKeyboardButton("Test", constants.url_test_eight)
        url_essay_button = telebot.types.InlineKeyboardButton("Essay", constants.url_essay_eight)
        url_answ_button = telebot.types.InlineKeyboardButton("Answers", constants.url_answ_eight)
        url_exp_button = telebot.types.InlineKeyboardButton("Explanations", constants.url_exp_eight)
        inline_keyboard.add(url_test_button)
        inline_keyboard.add(url_essay_button)
        inline_keyboard.add(url_answ_button)
        inline_keyboard.add(url_exp_button)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания для " + message.text, reply_markup=inline_keyboard)

    if message.text == "Книги":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("1", "2")
        user_markup.row("/start")
        bot.send_message(message.from_user.id, "Выберите страницу из списка книг", reply_markup=user_markup)

    if message.text == "1":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_book_button_one = telebot.types.InlineKeyboardButton(
            "Cracking the New SAT by Princeton Review 2016 edition", constants.url_book_one)
        url_book_button_two = telebot.types.InlineKeyboardButton("Erica Meltzer's The Critical Reader",
                                                                 constants.url_book_two)
        url_book_button_three = telebot.types.InlineKeyboardButton(
            "Erica Meltzer’s The Ultimate Guide to SAT Grammar", constants.url_book_three)
        url_book_button_four = telebot.types.InlineKeyboardButton(
            "500+ Practice Questions for the New SAT by The Princeton Review", constants.url_book_four)
        inline_keyboard.add(url_book_button_one)
        inline_keyboard.add(url_book_button_two)
        inline_keyboard.add(url_book_button_three)
        inline_keyboard.add(url_book_button_four)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания книг. Страница: " + message.text, reply_markup=inline_keyboard)

    if message.text == "2":
        inline_keyboard = telebot.types.InlineKeyboardMarkup()
        url_book_button_five = telebot.types.InlineKeyboardButton("Книга с SAT Vocabulary", constants.url_book_five)
        url_book_button_six = telebot.types.InlineKeyboardButton("Erica Meltzer's SAT Grammar Workbook 3rd edition",
                                                                 constants.url_book_six)
        url_book_button_seven = telebot.types.InlineKeyboardButton("The College Panda SAT Essay",
                                                                   constants.url_book_seven)
        url_book_button_eight = telebot.types.InlineKeyboardButton("McGraw-Hill Education SAT 2016 edition",
                                                                   constants.url_book_eight)
        url_book_button_nine = telebot.types.InlineKeyboardButton(
            "SAT Prep Black Book: The most effective SAT strategies ever", constants.url_book_nine)
        inline_keyboard.add(url_book_button_five)
        inline_keyboard.add(url_book_button_six)
        inline_keyboard.add(url_book_button_seven)
        inline_keyboard.add(url_book_button_eight)
        inline_keyboard.add(url_book_button_nine)
        bot.send_message(message.from_user.id, "Вот кнопки для скачивания книг. Страница: " + message.text, reply_markup=inline_keyboard)

    if message.text == "Статьи для подготовки":
        bot.send_message(message.from_user.id, "Cкоро...")

    if message.text == "Learn Vocabulary Words":
        bot.send_message(message.from_user.id, "В разработке...")

bot.polling(none_stop=True)