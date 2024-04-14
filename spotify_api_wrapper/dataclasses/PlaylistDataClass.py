from .SimplifiedPlaylistObject import SimplifiedPlaylistObject

class PlaylistDataClass:
    def __init__(self, response):
        self.href = response.get('href')
        self.limit = response.get('limit')
        self.next = response.get('next')
        self.offset = response.get('offset')
        self.previous = response.get('previous')
        self.total = response.get('total')
        self.items = []
        if 'items' in response:
            for item in response['items']:
                playlist_item = SimplifiedPlaylistObject(item)
                self.items.append(playlist_item)
                
    def __str__(self):
        items_str = "\n".join([f"  {index + 1}. {item.name}" for index, item in enumerate(self.items)])
        return f"Playlist Data:\n"\
                f"  - Href: {self.href}\n"\
                f"  - Limit: {self.limit}\n"\
                f"  - Next: {self.next}\n"\
                f"  - Offset: {self.offset}\n"\
                f"  - Previous: {self.previous}\n"\
                f"  - Total: {self.total}\n"\
                f"  - Items:\n{items_str}"
                
    def __repr__(self):
        return f"PlaylistDataClass(href={self.href}, limit={self.limit}, next={self.next}, offset={self.offset}, previous={self.previous}, total={self.total}, items={self.items})"

    def __eq__(self, other):
        if not isinstance(other, PlaylistDataClass):
            return False
        return (self.href == other.href and
                self.limit == other.limit and
                self.next == other.next and
                self.offset == other.offset and
                self.previous == other.previous and
                self.total == other.total and
                self.items == other.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]