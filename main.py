from flask import Flask, render_template, request
from api import *
app = Flask(__name__)

@app.route("/" , methods = ['GET' , 'POST'])
def hello_world():
    text = ""
    translatedText = ""
    if(request.method == 'POST'):
        text = request.form['textbox']
        translatedText = getTranslation(text)
        translatedText = translatedText['translatedText']
    return render_template('index.html' , translatedText = translatedText, origianlText = text)

if __name__ == "__main__":
    app.run(debug=True)
