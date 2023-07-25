import random

# Функция для получения случайного ответа
def get_random_response():
    responses = ["Привет!", "Здравствуйте!", "Как дела?", "Чем могу помочь?", "До свидания!"]
    return random.choice(responses)

# Функция для обработки вопроса пользователя
def handle_user_input(user_input):
    if "привет" in user_input.lower():
        return get_random_response()
    elif "как дела" in user_input.lower():
        return "Хорошо, спасибо! Как у вас?"
    elif "имя" in user_input.lower():
        return "Меня зовут Чат-бот. А как вас зовут?"
    elif "пока" in user_input.lower() or "до свидания" in user_input.lower():
        return get_random_response()
    else:
        return "Извините, я не понимаю ваш запрос."

# Основной цикл работы чат-бота
def main():
    print("Чат-бот: Привет! Я готов к общению. Для выхода введите 'пока' или 'до свидания'.")
    
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'пока' or user_input.lower() == 'до свидания':
            print("Чат-бот: " + get_random_response())
            break
        response = handle_user_input(user_input)
        print("Чат-бот:", response)

if __name__ == "__main__":
    main()
