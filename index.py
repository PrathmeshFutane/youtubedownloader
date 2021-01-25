import pytube
url = input("Enter or paste the url here: ")

youtube = pytube.YouTube(url)

streams = youtube.streams.all()
for i in streams:
	print(i)



itag = input('Enter the itag number from above: ')
video = youtube.streams.get_by_itag(itag)

print("1. C:/video")
print("2. D:/video")
print("3. E:/video")
print("4. F:/video")
path = int(input("Enter number from above path: "))
if path == 1:
	path = "C:/video"
elif path == 2:
	path = "D:/video"
elif path == 3:
	path = "E:/video"
elif path == 4:
	path = "F:/video"


video.download(path)
print('done')

# https://youtu.be/EP4dWtN2Wlo
