from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=YOrAY6td1p8&list=PLisfUdjySbZX2C5InwAspuFcqFp-UErxc&index=19")
stream = yt.streams.get_highest_resolution()
stream.download('/Users/christiangrier/Desktop/DE_Projects/cod-stats')