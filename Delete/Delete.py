# -*- coding:utf-8 -*-
import os


def delete(bot, message):
    chat_id = message["chat"]["id"]
    with open(bot.path_converter(bot.plugin_dir + "Delete/__init__.py"), "r", encoding="utf-8") as init:
        prefix = init.readline()[1:].strip()  # 获取指令名
    docname = message["text"][len(prefix) + 1:]  # 指令后参数
    os.remove("./posts/" + docname + ".md")
    bot.sendMessage(chat_id, "Article " + docname + " was deleted successfully!")
