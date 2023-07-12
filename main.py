import json
import psycopg2
   #Введи тут свои данные
db_params = {
    'host': 'localhost', #обычно localhost
    'database': 'message_table', #можешь тут изменить название БД, в коде ниже тоже нужно будет заменить message_table на другое название
    'user': 'postgres', #обычно postgres
    'password': '123456789' #твой пароль от pgadmin4
}
 
json_file_path = 'C:/Users/qwe/PycharmProjects/pythonProject1/result.json' #свой путь до этого файлика
 
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()
 
create_table_query = """
    CREATE TABLE IF NOT EXISTS message_table (
        chat_name TEXT,
        chat_type TEXT,
        chat_id BIGINT,
        message_id BIGINT,
        message_type TEXT,
        message_date TIMESTAMP,
        message_from TEXT,
        message_from_id TEXT,
        message_text TEXT
    )
"""
cursor.execute(create_table_query)
 
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
 
    chats = data['chats']['list']
    for chat in chats:
        chat_name = chat.get('name', '')
        chat_type = chat['type']
        chat_id = chat['id']
        messages = chat['messages']
        for message in messages:
            message_type = message.get('type', '') if isinstance(message, dict) else ''
            if message_type == 'message':
                message_id = message['id']
                message_date = message['date']
                message_from = message['from'] or ''
                message_from_id = message['from_id']
 
                if 'text' in message and message['text']:
                    message_text = json.dumps(message['text'], ensure_ascii=False)
                else:
                    message_text = ''
 
                insert_message_query = """
                    INSERT INTO message_table (
                        chat_name, chat_type, chat_id, message_id, message_type, message_date, message_from, message_from_id, message_text
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_message_query, (
                    chat_name, chat_type, chat_id, message_id, message_type, message_date, message_from,
                    message_from_id, message_text
                ))
 
conn.commit()
cursor.close()
conn.close()
 
print("Данные успешно сохранены в базе данных.")
 