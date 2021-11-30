# -*- coding:utf-8 -*-

def deploy(bot, message):
    # root_id = bot.root_id
    # bot_id = bot.bot_id
    # author = bot.author
    # version = bot.version
    # plugin_dir = bot.plugin_dir
    # plugin_bridge = bot.plugin_bridge
    # uptime = bot.uptime
    # response_times = bot.response_times
    # response_chats = bot.response_chats
    # response_users = bot.response_users

    chat_id = message["chat"]["id"]
    user_id = message["from"]["id"]
    message_id = message["message_id"]

    message_type = message["message_type"]
    chat_type = message["chat"]["type"]

    prefix = ""
    with open(bot.path_converter(bot.plugin_dir + "Deploy/__init__.py"), "r", encoding="utf-8") as init:
        prefix = init.readline()[1:].strip()

    # Write your plugin code below
