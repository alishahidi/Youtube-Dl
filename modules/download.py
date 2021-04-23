from modules import loading
    

def download(youtube, stream, typeSelected):
        ysExtract = loading.extract.extracStream(stream)
        progressive = ysExtract["progressive"]
        typeStram = ysExtract["type"]
        if typeStram == "audio" and typeSelected == "audio":
            convert = loading.inputPlus("Do you want convert to mp3? (y => yes, n => no)")
            if convert == "y":
                print("Download Audio File")
                print("\n")
                audio = stream.download(output_path= "temp", filename = "temp_audio_"+youtube.title)
                print("Convert Audio to mp3")
                print("\n")
                loading.media.video_to_mp3(audio, youtube.title)
                print("Delete Audio File")
                if loading.os.path.exists(audio):
                    loading.os.remove(audio)
            else:
                stream.download(output_path= "media", filename = youtube.title)
            print(loading.colored("Task Finish", "green"))
        else:
            if str(progressive) == "True":
                stream.download(output_path= "media", filename = youtube.title)
                print(loading.colored("Task Finish", "green"))
            else:
                print("Download Audio File")
                print("\n")
                audioTemp = youtube.streams.get_audio_only().download(output_path= "temp", filename = "temp_audio_"+youtube.title)
                print("\n")
                print("Download Video File")
                videoTemp = stream.download(output_path= "temp", filename = "temp_video_"+youtube.title)
                print("Merge audio with video")
                loading.media.merge_video_audio(videoTemp, audioTemp, youtube.title)
                if loading.os.path.exists(audioTemp):
                    loading.os.remove(audioTemp)
                if loading.os.path.exists(videoTemp):
                    loading.os.remove(videoTemp)
                print("Delete temp files")
                print(loading.colored("Task Finish", "green"))