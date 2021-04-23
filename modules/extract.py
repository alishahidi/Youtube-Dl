from modules import loading

def details(youtube):
    print(loading.colored("\nDetails", "yellow"))
    print(loading.colored("--------------------++++++++++--------------------", "blue"))
    print("Title: ",youtube.title)
    print("Number of views: ",youtube.views)
    print("Ratings: ",youtube.rating)
    print("Length of video: ",round(youtube.length),"seconds")
    print("Description: ",youtube.description)

def extracStreams(streams):
    extractFull = []
    for a in streams:
        extractStreams = str(a).split(" ")
        del extractStreams[0]
        extractValuesOfStream = dict()
        for i in extractStreams:
            extractStep1 = i.split("\"")
            dictExtract = dict()
            if(extractStep1[0] == "itag="):
                extractValuesOfStream["itag"] = extractStep1[1]
            if(extractStep1[0] == "mime_type="):
                extractValuesOfStream["mime_type"] = extractStep1[1]
            if(extractStep1[0] == "res="):
                extractValuesOfStream["res"] = extractStep1[1]
            if(extractStep1[0] == "abr="):
                extractValuesOfStream["abr"] = extractStep1[1]
            if(extractStep1[0] == "progressive="):
                extractValuesOfStream["progressive"] = extractStep1[1]
        extractFull.append(extractValuesOfStream)
    return extractFull

def printStreams(youtube, type):
    if type=="audio":
        streams = youtube.streams.filter(only_audio=True)
    else:
        streams =youtube.streams.filter(only_video=True)
    extract = extracStreams(streams)
    numOfExtract = 0
    for i in extract:
        numOfI = 0
        iExtract = ""
        dicEx = i
        for a in i:
            addSplit = ""
            if numOfI < (len(i) - 1):
                addSplit = ","
            iExtract = iExtract + f"[{str(list(dicEx)[numOfI])}] : {str(list(dicEx.values())[numOfI]) + addSplit} "
            numOfI = numOfI + 1
        print(iExtract)
        numOfExtract = numOfExtract + 1
        if numOfExtract < len(extract) :
            print("-----------------")


def extracStream(stream):
    extractFull = dict()
    extractStream = str(stream).split(" ")
    del extractStream[0]
    for i in extractStream:
        extractStep1 = i.split("\"")
        if(extractStep1[0] == "mime_type="):
            extractFull["mime_type"] = extractStep1[1]
        if(extractStep1[0] == "type="):
            extractFull["type"] = extractStep1[1]
        if(extractStep1[0] == "progressive="):
            extractFull["progressive"] = extractStep1[1]
            
    return extractFull