# Импорт load_dotenv
from dotenv import load_dotenv

# Импорт библиотеки для работы с окружением
import os

# Загрузка переменных из .env
success = load_dotenv(dotenv_path='.env')
if not success:
    print("Предупреждение: файл .env не найден или не загружен")

print('Hello from repository!')

def print_author():
    author = os.getenv('AUTHOR')
    if author is None:
        print("Ошибка: переменная AUTHOR не задана в .env")
        return None
    return author

# Вызов функции и сохранение результата
author_name = print_author()

# Вывод результата (с проверкой на None)
if author_name is not None:
    print(f"Автор проекта: {author_name}")
