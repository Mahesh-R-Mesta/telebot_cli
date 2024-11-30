from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update
import os
import re
import time
import argparse


#TELETOKEN="5166706434:AAF0g1LbCG-xTBBG0B9LQHSmblf1lgnRpuo"


def get_env():
    path = f"{os.getenv('HOME')}/.config/telebot/"
    env_path = f"{path}teletoken.env"
    file = open(env_path,"r")
    token = file.read()
    file.close()
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


file_names = []

async def send_file(update:Update,context:ContextTypes.DEFAULT_TYPE):
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
                await update.message.reply_photo(photo = file)
            elif ext in [".doc","docx","txt","json","xml","csv"]:
                file = open(f"{extpath}/{file_name}","rb")
                print(f"{extpath}/{file_name}")
                await update.message.reply_document(document=file)
            elif ext in [".mp4"]:
                file = open(f"{extpath}/{file_name}","rb")
                print(f"{extpath}/{file_name}")
                await update.message.reply_video(video=file)


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
    parser_welcom = subparser.add_parser("aboutyou",help="Just for fun")

    parser_token = subparser.add_parser("token",help="Bot tokens subparser")
    parser_token.add_argument('-s','--set-token',help="set & saves the token of telebot")

    arg = parser.parse_args()

    if arg.command == "sendfile":
        env_token = get_env()
        if env_token == None:
            print("Token is not assigned please set token by 'token -s token' command")
            exit()
        if arg.file_name != None:
            file_names.append(arg.file_name)
        print("type /sendme in telegram bot to get files")
        app = Application.builder().token(env_token).build()
        app.add_handler(CommandHandler("sendme",send_file))
#       app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        app.run_polling(allowed_updates=Update.ALL_TYPES)
    elif arg.command == "token":
        if arg.set_token == None:
            print("error: argument not found")
            exit()
        save_env(arg.set_token)

    elif arg.command == "aboutyou":
        print("""
              Name:telebot-cli
              Version:1.0.4
              author: Mahesh r mesta""")
    else:
        print("Check --help to see options")

#run_main()
