import whisper

model = whisper.load_model("small")
text = model.transcribe(r"G:\EC\classification\1.mp4")

print(text['text'])