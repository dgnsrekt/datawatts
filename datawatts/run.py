import pafy
import vlc
import time
import multiprocessing

from datawatts import datassette
from datawatts import watts
from datawatts import menu


wattsurl = next(watts.get_url())[1]
dataurl = next(datassette.get_url())
dataname = dataurl[0].split(':')[1].strip()
dataurl = dataurl[1]

video = pafy.new(wattsurl)
best = video.getbest()
wattsurl = best.url


def playurl(url, volume=90):
    instance = vlc.Instance('--input-repeat=-1 --novideo --quiet')

    # Define VLC player
    player = instance.media_player_new()

    # Define VLC media
    media = instance.media_new(url)

    # Set player media
    player.set_media(media)

    player.audio_set_volume(volume)
    # Play the media
    try:
        player.play()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


def main():

    p1 = multiprocessing.Process(target=playurl, args=(dataurl, 45))
    p2 = multiprocessing.Process(target=playurl, args=(wattsurl, 70))

    try:
        p1.start()
        p2.start()
        menu.main_menu(dataname=dataname)
    except KeyboardInterrupt:
        pass
    finally:
        p1.join()
        p2.join()


if __name__ == '__main__':
    main()
