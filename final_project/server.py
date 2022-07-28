from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    english_text = translator.english_to_french(text_to_translate)
    return str(english_text)

@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    french_text = translator.french_to_english(text_to_translate)
    return str(french_text)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
