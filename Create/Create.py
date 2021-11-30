# -*- coding:utf-8 -*-
from os import path
from config import *


def Create(bot, message):
    chat_id = message['chat']['id']
    doc_name = message['text'][8:]
    doc_path = f'{hexo_path}/_posts/{doc_name}.md'

    if path.exists(doc_path):
        bot.sendMessage(chat_id, 'The article has been created!')
    else:
        file = open(doc_path, 'w')
        file.close()
        bot.sendMessage(chat_id, f'Article {doc_name} was created successfully!')