from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update, Bot
import os
import re
import time
import argparse
import asyncio


#TELETOKEN="5166706434:AAF0g1LbCG-xTBBG0B9LQHSmblf1lgnRpuo"


def get_env():
    path = f"{os.getenv('HOME')}/.config/telebot/"
    env_path = f"{path}teletoken.env"
    file = open(env_path,"r")
    token = file.read()
    file.close()
    if token == None:
        print("Token is not assigned please set token by 'token -s token' command")
        exit()
    return token

def save_env(token):
    path = f"{os.getenv('HOME')}/.config/telebot/"
    if not os.path.exists(path):
        os.makedirs(path)
    env_path = f"{path}teletoken.env"
    print(env_path)
    file= open(env_path,"w")
    file.write(token)
    file.close()


def save_chat_id(chat_id):
    path = f"{os.getenv('HOME')}/.config/telebot/"
    if not os.path.exists(path):
        os.makedirs(path)
    env_path = f"{path}teleuserid"
    print(env_path)
    file= open(env_path,"w")
    file.write(chat_id)
    file.close()

def get_chat_id():
    path = f"{os.getenv('HOME')}/.config/telebot/"
    env_path = f"{path}teleuserid"
    file = open(env_path,"r")
    chatid = file.read()
    if chatid == None:
        print("""Chat id not found!, get chat-id by messsgaing xyz.. word from telegram and then in app run 'telebot-cli chats'
                  to check all chats get your id from terminal and set it by 'telebot token --set-userid {id}'""")
        exit()
    file.close()
    return chatid



file_names = []

async def send_text(message,parse_mode=None):
    env_token = get_env()
    chat_id = get_chat_id()
    tbot = Bot(token=env_token)
    await tbot.sendMessage(chat_id=chat_id,text=message,parse_mode=parse_mode)
    print("messge sent")

async def send_file():
    env_token = get_env()
    chat_id = get_chat_id()
    tbot = Bot(token=env_token)

    print("started sending files",file_names)
    cfilepath = os.getcwd()
    extpath = re.sub(r'/telegram_cli/telegram_cli/telebot$','',cfilepath)
    print(extpath)
    current_dir_files = []
    if len(file_names)!=0:
        print("sending file -> ",",".join(file_names))
        current_dir_files = file_names
    else:
        current_dir_files = os.listdir(extpath)
        print(f"sending all files in {extpath} ->", ",".join(current_dir_files))
    for file_name in current_dir_files:
        if '.' in file_name:
            ext = file_name.split('.')[1]
            if ext in ["png","jpeg","jpg"]:
                print(f"{extpath}/{file_name}")
                file = open(f"{extpath}/{file_name}","rb")
                await tbot.sendPhoto(chat_id=chat_id, photo = file)
            elif ext in ["html","doc","docx","txt","json","xml","csv","py"]:
                file = open(f"{extpath}/{file_name}","rb")
                print(f"{extpath}/{file_name}")
                await tbot.sendDocument(chat_id=chat_id,document=file)
            elif ext in ["mp4","mpeg","gif"]:
                file = open(f"{extpath}/{file_name}","rb")
                print(f"{extpath}/{file_name}")
                await tbot.sendVideo(chat_id=chat_id,video=file)
            else:
                file = open(f"{extpath}/{file_name}","rb")
                print(f"{extpath}/{file_name}")
                await tbot.sendDocument(chat_id=chat_id,document=file)



async def print_chatid():
    env_token = get_env()
    tbot = Bot(token=env_token)
    chats = await tbot.getUpdates()
    for chat in chats:
        print(f"id:{chat.message.chat_id} name: {chat.message.chat.first_name} {chat.message.chat.last_name}")




#        await update.message.reply_text(f"{extpath}{file_name}")

#async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    """Echo the user message."""
#    await update.message.reply_text(update.message.text)

def run_main():
    global file_names
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    # get files
    parser_sendfile = subparser.add_parser('sendfile',help="send files to bot using /sendme command")
    parser_sendfile.add_argument('-f','--file-name',help="file name to send")
#    parser_sendfile.add_argument('-m','--multifile-names',help="send multiple files exmp1.jpg,exmp2.jpg..etc")
    parser_welcom = subparser.add_parser("aboutyou",help="Just for fun")
    parser_chatids = subparser.add_parser("chatids",help="Prints recently sent chat-ids")
    parser_token = subparser.add_parser("setting",help="used to set bot token and user-id ")
    parser_token.add_argument('-s','--set-token',help="set & saves the token of telebot")
    parser_token.add_argument('-u','--set-chatid',help="set & saves the userid for telebot")
    parser_text = parser.add_argument("-m","--send-message", help="send text message") 
    arg = parser.parse_args()

    if arg.command == "sendfile":
#        env_token = get_env()
#        if env_token == None:
#            print("Token is not assigned please set token by 'token -s token' command")
#            exit()
        if arg.file_name != None:
            if ',' in arg.file_name:
                file_names.extends(arg.file_name.split(","))
            else:
                file_names.append(arg.file_name)
#        print("type /sendme in telegram bot to get files")
#        tbot = Bot(token=env_token)
#        chat_id = get_chat_id()
#        if chat_id == None:
#            print("""Chat id not found!, get chat-id by messsgaing xyz.. word from telegram and then in app run 'telebot-cli chats'
#                  to check all chats get your id from terminal and set it by 'telebot token --set-userid {id}'""")
#            exit()
        asyncio.run(send_file())
#        app = Application.builder().token(env_token).build()
#        app.add_handler(CommandHandler("sendme",send_file))
#       app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
#        app.run_polling(allowed_updates=Update.ALL_TYPES)
    elif arg.command == "setting":
        if arg.set_token!=None:
            save_env(arg.set_token.strip())
        if arg.set_chatid!=None:
            save_chat_id(arg.set_chatid.strip())
    elif arg.command == "chatids":
        asyncio.run(print_chatid())
    elif arg.command == "aboutyou":
        print("""
              Name:telebot-cli
              Version:1.0.4
              author: Mahesh r mesta""")
    elif arg.send_message != None:
        asyncio.run(send_text(arg.send_message))
    else:
        print("Check --help to see options")



#run_main()
