from pytube import YouTube

# where to save
SAVE_PATH = "D:/Youtube Coding Videos"  # to_do

# link of the video to be downloaded
# opening the file
link = open('download_links.txt', 'r')

for i in link:
    try:

        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(i)
        yt.title

        print(i)
        print(yt.title)
    except:

        # to handle exception
        print("Connection Error")

        # filters out all the files with "mp4" extension
    mp4files = yt.streams.filter(file_extension='mp4')

    # get the video with the extension and
    # resolution passed in the get() function
    d_video = yt.streams.get_highest_resolution()

    try:
#
#        # downloading the video
        d_video.download(SAVE_PATH)
    except:
        print("Some Error!")

print('Task Completed!')