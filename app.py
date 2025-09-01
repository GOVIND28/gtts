from flask import Flask, request, render_template
from gtts import gTTS
import os, random

app = Flask(__name__)

# Ensure static folder exists
os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            filename = f"static/output{random.randint(1,10000)}.mp3"
            gTTS(text=text, lang="en", slow=False).save(filename)
            audio_file = "/" + filename  # Pass to HTML
    return render_template("index.html", audio_file=audio_file)
