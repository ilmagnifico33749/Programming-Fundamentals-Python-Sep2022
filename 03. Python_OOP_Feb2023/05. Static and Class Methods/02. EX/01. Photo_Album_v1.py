import math


class PhotoAlbum:
    max_photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for page in range(self.pages)]
        # self.photos = [[] for _ in self.pages]
        self.max_photos_per_page = 4

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count/PhotoAlbum.max_photos_per_page))

    def add_photo(self, label: str):
        if sum([len(sublist) for sublist in self.photos]) == (self.pages * self.max_photos_per_page):
            return f"No more free slots"
        for photo_page in range(len(self.photos)):
            current_photo_page = self.photos[photo_page]
            if len(current_photo_page) < 4:
                current_photo_page.append(label)
                return f"{label} photo added successfully on page {photo_page+1} slot {len(current_photo_page)}"

    def display(self):
        result = "-----------"
        photos_repr = [["[]" for photo in album_page] for album_page in self.photos]

        for pages in photos_repr:
            result += f"\n{' '.join(pages)}\n"
            result += "-----------"

        return result


# ###################################################################
# Test_Code_1:
album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
# -------------------------------------------------------------------
# baby photo added successfully on page 1 slot 1
# first grade photo added successfully on page 1 slot 2
# eight grade photo added successfully on page 1 slot 3
# party with friends photo added successfully on page 1 slot 4
# [['baby', 'first grade', 'eight grade', 'party with friends'], []]
# prom photo added successfully on page 2 slot 1
# wedding photo added successfully on page 2 slot 2
# -----------
# [] [] [] []
# -----------
# [] []
# -----------
# ###################################################################
