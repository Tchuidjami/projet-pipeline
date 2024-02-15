import assemblyai as aai

aai.settings.api_key = "5d154d75227e45edb2a466c178ea89e0"
transcript = aai.Transcriber().transcribe("test.mp3")

subtitles=transcript.export_subtitles_srt()

f=open("subtitles.srt","a")
f.write(subtitles)
f.close()




