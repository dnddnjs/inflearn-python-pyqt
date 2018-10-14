import pytube
import os
import subprocess


yt = pytube.YouTube("https://www.youtube.com/watch?v=aJOTlE1K90k")
videos = yt.streams.all()

# print("videos", videos)

for i in range(len(videos)):
	print(i, ' , ', videos[i])

cNum = int(input("다운 받을 화질은?"))

down_dir = "./"

videos[cNum].download(down_dir)

newFileName = input("변환할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i', 
	os.path.join(down_dir, oriFileName),
	os.path.join(down_dir, newFileName)])

print("complete")