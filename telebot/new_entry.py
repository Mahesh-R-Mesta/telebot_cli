import telegram
import asyncio


bot = telegram.Bot(token="5166706434:AAF0g1LbCG-xTBBG0B9LQHSmblf1lgnRpuo")

async def introduction():
    d = await bot.getMe()
    print('Botname',d['first_name'],'\nusername',d['username'])

my_chat_id = "1238509487"

async def send_file():
    await introduction()
    chats = await bot.getUpdates() #[-1].message.chat_id
    if len(chats)!=0:
        chat_id = chats[-1].message.chat_id
        print(chat_id)
        await bot.sendMessage(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")


if __name__ == "__main__":
    asyncio.run(send_file())
    


