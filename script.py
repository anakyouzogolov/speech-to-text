import speech_recognition as sp_r

# speech audio file
file_name = "speech.wav"

# initialize the recognizer
rec = sp_r.Recognizer()

# open the audio file (speech)
with sp_r.AudioFile(file_name) as my_audio:

    # get audio data (load audio to memory)
    audio_data = rec.record(my_audio)

    # convert from speech (audio) to text
    text = rec.recognize_google(audio_data)
    # print(text)

    with open("text.txt", "w") as text_file:
        text_file.write(text)