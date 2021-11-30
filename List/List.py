# -*- coding:utf-8 -*-
import os
import time


def List(bot, message):
    chat_id = message["chat"]["id"]
    doclist = os.listdir("./posts")
    doc = 'Document List:\n'
    if not doclist:
        bot.sendMessage(chat_id, "You don't have article.")
    else:
        for i in doclist:
            doc = doc + i + '\n'
        bot.sendMessage(chat_id, text=str(doc))
