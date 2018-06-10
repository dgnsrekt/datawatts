import pafy
import vlc
import time
import multiprocessing
import threading

import datassette
import watts

wattsurl = next(watts.get_url())[1]
dataurl = next(datassette.get_url())[1]

print(wattsurl)
print(dataurl)

video = pafy.new(wattsurl)
best = video.getbest()
wattsurl = best.url


def playurl(url, volume=90):
    instance = vlc.Instance('--input-repeat=-1 --novideo')

    # Define VLC player
    player = instance.media_player_new()

    # Define VLC media
    media = instance.media_new(url)

    # Set player media
    player.set_media(media)

    player.audio_set_volume(volume)
    # Play the media
    player.play()
    while True:
        time.sleep(1)


p1 = multiprocessing.Process(target=playurl, args=(dataurl, 45))
p2 = multiprocessing.Process(target=playurl, args=(wattsurl, 70))

# p1 = threading.Thread(target=playurl, args=(dataurl, 40))
# p2 = threading.Thread(target=playurl, args=(wattsurl, 80))

p1.start()
p2.start()

p1.join()
p2.join()
