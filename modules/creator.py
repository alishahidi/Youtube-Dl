from modules import loading


def Youtube(link):
    return loading.YouTube(link, on_progress_callback=loading.on_progress)

def Stream(youtube, itag):
    return youtube.streams.get_by_itag(itag)