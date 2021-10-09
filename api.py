import requests
import json
def getTranslation(text):

    url = "https://libretranslate.de/translate"

    data = {
        "q": "text",
        "source": "en",
        "target": "fr",
    }

    r= requests.post(url, data = data)
    data = r.json()
    return data

print(getTranslation("Hello!"))
