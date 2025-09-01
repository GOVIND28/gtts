from flask import Flask, request, render_template
from gtts import gTTS
import os
import random,shutil

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def index():
    audio_file=None
    if request.method=="POST":
        text=request.form.get("text")
        if text:
            shutil.rmtree("static"),os.makedirs("static",exist_ok=True)
            filename=f"static/output{random.random()}.mp3"
            gTTS(text=text,lang="en",slow=False).save(filename)
            audio_file="/"+ filename
    return render_template("index.html",audio_file=audio_file)

if __name__== "__main__":
    os.makedirs("static",exist_ok=True)
    app.run(debug=True,port=4000)
    
