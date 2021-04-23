from modules import loading
 
def safeReplaceString(string):
    keepcharacters = ['/']
    string = "".join([c for c in string if c.isalpha() or c.isdigit() or c==' ' or c in keepcharacters]).rstrip()
    string = string.replace("/", "-")
    return string

def video_to_mp3(file_name, outname, dirOut = "result"):
    outname = safeReplaceString(outname)
    if loading.os.name == "nt":
        audio = loading.AudioSegment.from_file(file_name)
        audio.export(dirOut+"/"+outname+".mp3", format="mp3")
    elif loading.os.name == "posix":
        file, extension = loading.os.path.splitext(file_name)
        loading.os.system('ffmpeg -i \"{file}{ext}\" \"{file}.wav\"'.format(file=file, ext=extension))
        loading.os.system('lame \"{file}.wav\" \"{outname}\"'.format(file=file, outname = dirOut+"/"+outname+".mp3"))
        loading.os.remove('{}.wav'.format(file))  # Deletes the .wav file
    return True;

def merge_video_audio(video, audio, outname, dirOut = "result"):
    outname = safeReplaceString(outname)
    if loading.os.name == "nt":
        input_video = loading.ffmpeg.input(video)
        input_audio = loading.ffmpeg.input(audio)
        loading.ffmpeg.concat(input_video, input_audio, v=1, a=1).output(dirOut+"/"+outname+".mp4").run()
    elif loading.os.name == "posix":
        cmd = f'ffmpeg -i \"{video}\" -i \"{audio}\" -c:v copy -c:a aac \"{dirOut+"/"+outname+".mp4"}\"'
        loading.subprocess.call(cmd, shell=True)
    return True;