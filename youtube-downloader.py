from pytube import YouTube, Playlist
import re
import sys
import time
import progressbar

bar = progressbar.ProgressBar(max_value=100)
def show_progress_bar(stream, _chunk, bytes_remaining):
    current = int(((stream.filesize - bytes_remaining)/stream.filesize) * 100  )
    try: 
        # updates the progress bar                                   
        bar.update(current)
    except: 
        # progress bar dont reach 100% so a little trick to make it 100    
        bar.update(current)

y_url = input("Enter YouTube video URL: ")

# yt = YouTube(y_url,  on_progress_callback=show_progress_bar)
# title = yt.title
# print()
# print(type(title))
# print("----------------------------------------------------------------------------------------")

# # for stream in yt.streams.filter(progressive=True):
# #     size = "(" + str(round(stream.filesize/1000000, 2)) + "MB)"
# #     print(stream, size)
# print()

# # itag = int(input("Enter 'itag' of choised video: "))
# # bar.update(0)
# # yt.streams.get_by_itag(itag).download()

# caption = yt.captions['en']
# srt_file_name = re.sub(r"[^a-zA-Z0-9]+", ' ', title)  + ".srt"
# srt_file = open(srt_file_name, "w", encoding="utf-8")
# srt_file.write(caption.generate_srt_captions())
# srt_file.close()

def downloadVideo(url):
    yt = YouTube(url,  on_progress_callback=show_progress_bar)
    title = yt.title
    print()
    print(title)
    print("----------------------------------------------------------------------------------------")

    for stream in yt.streams.filter(progressive=True):
        size = "(" + str(round(stream.filesize/1000000, 2)) + "MB)"
        print(stream, size)
    bar.update(0)
    # yt.streams.get_by_itag(18).download()
    # print()
    # caption = yt.captions['en']
    # srt_file_name = re.sub(r"[^a-zA-Z0-9]+", ' ', title)  + ".srt"
    # srt_file = open(srt_file_name, "w", encoding="utf-8")
    # srt_file.write(caption.generate_srt_captions())
    # srt_file.close()

p = Playlist(y_url)
playlist_urls = list(p.video_urls)
print(len(playlist_urls))
for playlist_url in playlist_urls[27:28]:
    downloadVideo(playlist_url)
