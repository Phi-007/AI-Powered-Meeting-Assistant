# to install OpenAI Whisper ----> pip install git+https://github.com/openai/whisper.git



# ...... BEGINING WITH WHISPER:

import whisper

model = whisper.load_model("base") # Load the Whisper model
result = model.transcribe("audio_example.mp3") # Transcribe the audio file
print(result["text"]) # Output the transcription




# .......... Integrating Whisper into Applications:

from flask import Flask, request
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    audio_file = request.files["audio"]
    result = model.transcribe(audio_file)
    return {"transcription": result["text"]}

if __name__ == "__main__":
    app.run(debug=True)