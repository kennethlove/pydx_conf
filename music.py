from collections import deque
from functools import reduce
from operator import add, attrgetter


class Song:
    title = None
    artist = None

    def __init__(self, title=None, artist=None, time='00:00:00'):
        self.title = title
        self.artist = artist
        self.time = time
        # self.total_seconds = self.__set_total_seconds(time)
        self.__total_seconds = 0
        self.total_seconds = time

    @property
    def total_seconds(self):
        return self.__total_seconds

    @total_seconds.setter
    def total_seconds(self, time):
        if time.count(':') != 2:
            raise ValueError(
                "'time' argument should only be hours:minutes:seconds."
            )
        seconds, minutes, hours = map(int, time.split(':')[::-1])
        seconds += minutes * 60
        seconds += hours * 3600
        self.__total_seconds = seconds

    def __str__(self):
        return "{} by {}".format(self.title, self.artist)

    def __int__(self):
        return self.total_seconds

    def __add__(self, other):
        return self.total_seconds + other

    def __radd__(self, other):
        return self.total_seconds + other


class Playlist(deque):
    @property
    def play_time(self):
        return reduce(add, map(attrgetter('total_seconds'), self))

    def play_next_song(self):
        self.current_song = self.popleft()
        print("Currently playing: {}".format(self.current_song))


if __name__ == '__main__':
    test_song = Song('Test Song', 'Test Artist', '00:03:30')
    print(test_song.total_seconds)

    playlist = Playlist()
    playlist.extend([test_song, test_song])
    print(playlist.play_time)

    playlist.play_next_song()
    print(playlist.play_time)
