# -*- coding:utf-8 -*-
import time
from os import path
from config import *


def Create(bot, message):
    chat_id = message['chat']['id']
    doc_name = message['text'][8:]
    doc_path = f'{posts_path}/{doc_name}.md'

    if path.exists(doc_path):
        bot.sendMessage(chat_id, 'The article has been created!')
    else:
        # TODO 获取tags和categories
        tags = ''
        categories = ''
        data = '---\n' \
               f'title: {doc_name}\n' \
               f'date: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}\n' \
               f'tags: {tags}\n' \
               f'categories: {categories}\n' \
               'toc: true\n' \
               '---\n'
        with open(doc_path, 'a', encoding='utf-8') as file:
            file.write(data)
        bot.sendMessage(chat_id, f'Article *{doc_name}* was created successfully!', parse_mode="Markdown")