import whisper

# code qui permet d extraire la video en audio
#ffmpeg -i smart.mp4 -vn -ar 44100 -ac 2 -ab 320 smart.wav 

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("test_compress.wav")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detecte la langue parlee
_,probs = model.detect_language(mel)
print(f"la langue identifiee est: {max(probs, key=probs.get)}")


