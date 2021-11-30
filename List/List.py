# -*- coding:utf-8 -*-
from os import listdir
from config import *


def List(bot, message):
    chat_id = message["chat"]["id"]
    doc_list = listdir(posts_path)

    if not doc_list:
        bot.sendMessage(chat_id, "You don't have article.")
    else:
        doc_list_text = ''
        for doc in doc_list:
            doc_list_text += f'{doc}\n'
        bot.sendMessage(chat_id, text=doc_list_text)
