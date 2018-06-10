import feedparser
from random import shuffle


def get_random_playlist():
    url = 'https://www.musicforprogramming.net/rss.php'

    d = feedparser.parse(url)

    videos = []
    for e in d['entries']:
        title = e['title']
        id = e['links'][1]['href']
        duration = e['itunes_duration']
        videos.append((title, id, duration))

    shuffle(videos)

    return videos


def get_url():
    plist = get_random_playlist()
    for u in plist:
        yield u


if __name__ == '__main__':
    print(next(get_url()))
