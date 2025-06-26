import pyttsx3

engine = pyttsx3.init()

# Настройка речи
engine.setProperty('rate', 140)     # медленная речь
engine.setProperty('volume', 0.9)   # громкость
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # смена голоса

# Озвучка
engine.say("Это пример синтеза речи")
engine.runAndWait()

engine.save_to_file("Привет!", "voice.mp3")
engine.runAndWait()