import json
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

app.run(host="0.0.0.0", port=3000)
