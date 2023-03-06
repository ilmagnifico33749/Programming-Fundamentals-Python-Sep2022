# from song import Song
from project.song import Song


class Album:
    def __init__(self, name: str, *songs):

        self.name = name
        self.published = False
        self.songs = list(*songs)

    def add_song(self, song: Song):
        if song.single is True:
            return f"Cannot add {song.name}. It's a single"

        if self.published is True:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        try:
            searched_song = next(filter(lambda s: s.name == song_name, self.songs))
            if self.published is True:
                return f"Cannot remove songs. Album is published."
            self.songs.remove(searched_song)
            return f"Removed song {song_name} from album {self.name}."
        except StopIteration:
            return f"Song is not in the album."

    def publish(self):
        if self.published is True:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        # all_songs = '\n== '.join(current_song.get_info() for current_song in self.songs)
        #
        # return f"Album {self.name}" \
        #        f"\n== {all_songs}"
        result = [f"Album {self.name}"]
        [result.append(f"== {s.get_info()}") for s in self.songs]

        return "\n".join(result)

#