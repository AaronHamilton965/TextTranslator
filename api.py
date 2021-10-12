import json, sys
import requests


# TODO: ReDo function in order to accomdate different Languages
def getTranslation(text):

    url = "https://translate.astian.org/translate"

    data = {
        "q": text,
        "source": "en",
        "target": "fr",
    }

    r= requests.post(url, data = data)
    r = r.json()
    return r
