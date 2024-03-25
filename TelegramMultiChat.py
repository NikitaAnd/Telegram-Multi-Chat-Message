from pyrogram import Client
import asyncio
import configparser
import os

def create_sample_files():
    if not os.path.exists("config.ini"):
        with open("config.ini", "w") as config_file:
            config_file.write("[pyrogram]\napi_id = YOUR_API_ID\napi_hash = YOUR_API_HASH\nuser_session = YOUR_SESSION_NAME\ninterval = 15\n")
            print("config.ini создан. Пожалуйста, заполните его вашими данными API.")

    if not os.path.exists("chats.txt"):
        with open("chats.txt", "w") as chats_file:
            chats_file.write("@example_chat\n")
            print("chats.txt создан с примером. Пожалуйста, замените его на актуальные данные.")

    if not os.path.exists("message.txt"):
        with open("message.txt", "w") as message_file:
            message_file.write("Пример текста сообщения.")
            print("message.txt создан с примером сообщения.")

create_sample_files()

config = configparser.ConfigParser()
config.read("config.ini")
api_id = config.get("pyrogram", "api_id")
api_hash = config.get("pyrogram", "api_hash")
user_session = config.get("pyrogram", "user_session")
interval = int(config.get("pyrogram", "interval"))

with open("chats.txt", "r") as f:
    chats = [line.strip() for line in f.readlines()]

with open("message.txt", "r") as f:
    message_text = f.read()

async def send_message(client, chat, message):
    try:
        await client.send_message(chat, message)
        print(f"Сообщение успешно отправлено в {chat}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения в {chat}: {e}")

async def main():
    async with Client(user_session, api_id=api_id, api_hash=api_hash) as app:
        tasks = []
        for chat in chats:
            # Создание задачи для каждого чата
            task = asyncio.create_task(send_message(app, chat, message_text))
            tasks.append(task)
        
        await asyncio.gather(*tasks)
        await asyncio.sleep(interval)

if __name__ == "__main__":
    while True:
        asyncio.run(main())
