from pytube import Youtube

link = 'https://www.youtube.com/watch?v=1c4OQKnl7DQ'
yt = Youtube(link)

stream = yt.streams.get_highest_resolution()
stream.download()

print("Download complete")
