import pyttsx3

text = "Пошёл на фиг!"
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru', )
tts.say(f'{text}')
tts.runAndWait()

