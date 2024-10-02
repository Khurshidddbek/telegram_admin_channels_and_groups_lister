from telethon.sync import TelegramClient

# Вставьте сюда свои данные API из https://my.telegram.org/apps
api_id = 'MY_API_ID'
api_hash = 'MY_API_HASH'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    async with client:
        admin_chats = []

        # Получаем диалоги из главной папки
        dialogs = await client.get_dialogs(limit=None, folder=0)
        # Получаем диалоги из архивированной папки
        archived_dialogs = await client.get_dialogs(limit=None, folder=1)

        all_dialogs = dialogs + archived_dialogs

        for dialog in all_dialogs:
            chat = dialog.entity

            if hasattr(chat, 'creator') and chat.creator:
                admin_chats.append(f'Вы создатель: {chat.title}')
            elif hasattr(chat, 'admin_rights') and chat.admin_rights:
                admin_chats.append(f'Вы админ: {chat.title}')

        for admin_chat in admin_chats:
            print(admin_chat)

client.start()
client.loop.run_until_complete(main())
