import pyttsx3

# Создаем объект движка синтеза речи
engine = pyttsx3.init()

# Настраиваем движок синтеза речи
engine.setProperty('rate', 200) #220
engine.setProperty('volume', 0.9)

# Получаем текст для озвучивания
text = f"запрос от пользователя ураганига. Вот так будет слышшен сохранёный голосовой запрос."

# Озвучиваем текст
engine.say(text)

# Сохраняем озвучку в файл
engine.save_to_file(text, 'data\\user_data\\requests\\example_VoiceActing.mp3')

# Запускаем движок синтеза речи
engine.runAndWait()