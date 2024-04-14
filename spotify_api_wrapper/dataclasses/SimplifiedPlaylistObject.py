
class SimplifiedPlaylistObject:
    def __init__(self, item):
        self.collaborative = item.get('collaborative')
        self.description = item.get('description')
        self.external_urls = item.get('external_urls')
        self.id = item.get('id')
        self.images = item.get('images')
        self.name = item.get('name')
        self.owner = item.get('owner')
        self.public = item.get('public')
        self.snapshot_id = item.get('snapshot_id')
        self.tracks = item.get('tracks')
        self.type = item.get('type')
        self.uri = item.get('uri')
    
    def __str__(self):
        return f"Playlist Object:\n"\
               f"  - Collaborative: {self.collaborative}\n"\
               f"  - Description: {self.description}\n"\
               f"  - External URLs: {self.external_urls}\n"\
               f"  - ID: {self.id}\n"\
               f"  - Images: {self.images}\n"\
               f"  - Name: {self.name}\n"\
               f"  - Owner: {self.owner}\n"\
               f"  - Public: {self.public}\n"\
               f"  - Snapshot ID: {self.snapshot_id}\n"\
               f"  - Tracks: {self.tracks}\n"\
               f"  - Type: {self.type}\n"\
               f"  - URI: {self.uri}"

    def __repr__(self):
        return f"SimplifiedPlaylistObject(collaborative={self.collaborative}, description={self.description}, external_urls={self.external_urls}, id={self.id}, images={self.images}, name={self.name}, owner={self.owner}, public={self.public}, snapshot_id={self.snapshot_id}, tracks={self.tracks}, type={self.type}, uri={self.uri})"

    def __eq__(self, other):
        if not isinstance(other, SimplifiedPlaylistObject):
            return False
        return (self.collaborative == other.collaborative and
                self.description == other.description and
                self.external_urls == other.external_urls and
                self.id == other.id and
                self.images == other.images and
                self.name == other.name and
                self.owner == other.owner and
                self.public == other.public and
                self.snapshot_id == other.snapshot_id and
                self.tracks == other.tracks and
                self.type == other.type and
                self.uri == other.uri)


    def __len__(self):
        return len(self.tracks)

    def __getitem__(self, index):
        return self.tracks[index]