# -*- coding:utf-8 -*-
import os

def Create(bot, message):
    text = {}
    chat_id = message["chat"]["id"]
    with open(bot.path_converter(bot.plugin_dir + "Create/__init__.py"), "r", encoding="utf-8") as init:
        prefix = init.readline()[1:].strip()
    docname = message["text"][len(prefix)+1:]
    doclist = os.listdir("./posts")
    if docname+'.md' in doclist:
        bot.sendMessage(chat_id, "The article has been created!")
    else:
        file = open("./posts/"+docname+".md", "w")
        file.close()
        docname = message["text"][len(prefix)+1:]
        bot.sendMessage(chat_id, "Article "+docname+"  was created successfully!")
