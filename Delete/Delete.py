# -*- coding:utf-8 -*-
from os import remove, path
from config import *


def Delete(bot, message):
    chat_id = message["chat"]["id"]
    doc_name = message["text"][8:]
    doc_path = f'{post_path}/{doc_name}.md'

    if path.exists(doc_path):
        remove(doc_path)
        bot.sendMessage(chat_id, f'Article {doc_name} was deleted successfully!')
    else:
        bot.sendMessage(chat_id, 'Article not found!')
