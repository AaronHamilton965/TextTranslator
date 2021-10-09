import requests
import json
def getTranslation():

    url = "https://libretranslate.de/translate"

    data = {
        "q": "Hello my name is Kyle! How are you?",
        "source": "en",
        "target": "fr",
    }

    r= requests.post(url, data = data)
    r = r.json()
    print("English: Hello my name is Kyle! How are you?")
    print("French: " + r['translatedText'])

getTranslation()
