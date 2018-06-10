import pafy
from random import choice, shuffle

PLAYLIST_1 = 'https://www.youtube.com/playlist?list=PLZAtFo0XVBCOTAy97oNgerQiJSVYI88kr'
PLAYLIST_2 = 'https://www.youtube.com/playlist?list=PLj1znwVSZWW7y5pLGREMRVhWM91rcXVTG'
# PLAYLIST_3 = 'https://www.youtube.com/playlist?list=PLj1znwVSZWW5Q0jC7M8QCbQLYz8gWr6gv'
PLAYLIST_4 = 'https://www.youtube.com/playlist?list=PLDrE8eovyz8D9b__-MLQVoLISi8u4s_79'
PLAYLIST_5 = 'https://www.youtube.com/playlist?list=PLDrE8eovyz8CRHQPzWM2kJljSu8R9pYX1'
PLAYLIST_6 = 'https://www.youtube.com/playlist?list=PLDrE8eovyz8CrUeYQ4dCInNAi7OVr3k3c'
PLAYLIST_7 = 'https://www.youtube.com/playlist?list=PLDrE8eovyz8DOyGk9qRYp_USlVFl6Axlf'
PLAYLIST_8 = 'https://www.youtube.com/playlist?list=PLDrE8eovyz8DQHrs2BXdVIYgRdRMVsjOb'


def get_random_playlist():
    PLAYLIST = choice([PLAYLIST_1, PLAYLIST_2, PLAYLIST_4,
                       PLAYLIST_5, PLAYLIST_6, PLAYLIST_7, PLAYLIST_8])

    playlist = pafy.get_playlist(PLAYLIST)
    videos = []
    for link in playlist['items']:
        title = link['playlist_meta']['title']
        id = link['playlist_meta']['encrypted_id']
        id = f'https://www.youtube.com/watch?v={id}'
        duration = link['playlist_meta']['duration']
        videos.append((title, id, duration))

    shuffle(videos)

    return videos


def get_url():
    plist = get_random_playlist()
    for u in plist:
        yield u


if __name__ == '__main__':
    print(next(get_url()))
