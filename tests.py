import unittest

from music import Song, Playlist
from monsters import Monster, Troll, Dungeon


class SongTests(unittest.TestCase):
    def test_time_format_too_short(self):
        with self.assertRaises(ValueError):
            Song(time='00:00')

    def test_time_format_too_long(self):
        with self.assertRaises(ValueError):
            Song(time='00:00:00:00')

    def test_time_math(self):
        song = Song(time='00:03:30')
        self.assertEqual(song.total_seconds, 210)

    def test_time_string(self):
        song = Song(
            title="Bullet with Butterfly Wings",
            artist="Smashing Pumpkins"
        )
        self.assertEqual(
            str(song),
            "Bullet with Butterfly Wings by Smashing Pumpkins"
        )

    def test_time_int(self):
        song = Song(time='00:00:10')
        self.assertEqual(int(song), 10)

    def test_time_add(self):
        song1 = Song(time='00:00:10')
        song2 = Song(time='00:01:00')
        print(song1.total_seconds)
        self.assertEqual(song1+song2, 70)

    def test_time_update(self):
        song1 = Song(time='00:00:10')
        self.assertEqual(song1.total_seconds, 10)
        song1.total_seconds = '00:00:30'
        self.assertEqual(song1.total_seconds, 30)


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.song1 = Song(
            title="Bullet with Butterfly Wings",
            artist="Smashing Pumpkins",
            time='00:04:17'
        )
        self.song2 = Song(
            title="Song 2",
            artist="Blur",
            time="00:02:01"
        )
        self.song3 = Song(
            title="Creep",
            artist="Radiohead",
            time="00:03:58"
        )
        self.playlist = Playlist(
            [self.song1, self.song2, self.song3]
        )

    def test_playlist_length(self):
        self.assertEqual(len(self.playlist), 3)

    def test_play_time(self):
        self.assertEqual(self.playlist.play_time, 616)

    def test_play_next_song(self):
        self.playlist.play_next_song()
        self.assertLess(self.playlist.play_time, 616)

    def test_play_next_song_when_empty(self):
        playlist2 = Playlist()
        with self.assertRaises(IndexError):
            playlist2.play_next_song()


class MonsterTests(unittest.TestCase):
    def test_monster_getitem(self):
        monster = Monster(left_hand="axe")
        self.assertEqual(monster['left_hand'], 'axe')

    def test_monster_getitem_bad_key(self):
        monster = Monster(left_hand="axe")
        with self.assertRaises(KeyError):
            monster['left_foot']


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.monster1 = Monster()
        self.monster2 = Monster(sound='Urk!')
        self.troll1 = Troll()
        self.troll2 = Troll(sound="That's just your opinion.")
        self.horde = [self.monster1, self.monster2, self.troll1, self.troll2]

    def test_dungeon_iteration(self):
        dungeon = Dungeon(monsters=self.horde)
        self.assertSetEqual(
            {m.sound for m in dungeon},
            {m.sound for m in self.horde}
        )
