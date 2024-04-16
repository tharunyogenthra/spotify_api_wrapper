class TrackDataClass:
    def __init__(self, data):
        self.href = data.get("href", None)
        self.limit = data.get("limit", None)
        self.next = data.get("next", None)
        self.offset = data.get("offset", None)
        self.previous = data.get("previous", None)
        self.total = data.get("total", None)
        self.items = [TrackItem(item) for item in data.get("items", [])]

    def __eq__(self, other):
        if not isinstance(other, TrackDataClass):
            return False
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'TrackDataClass: total={self.total}, items={self.items}'

    def __repr__(self):
        return f'TrackDataClass(href={self.href}, limit={self.limit}, next={self.next}, offset={self.offset}, previous={self.previous}, total={self.total}, items={self.items})'


class TrackItem:
    def __init__(self, data):
        self.added_at = data.get("added_at", None)
        self.added_by = data.get("added_by", {}).get("external_urls", {}).get("spotify", None)
        self.is_local = data.get("is_local", False)
        self.track = TrackInfo(data.get("track", {}))

    def __eq__(self, other):
        if not isinstance(other, TrackItem):
            return False
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'TrackItem: added_at={self.added_at}, added_by={self.added_by}, is_local={self.is_local}, track={self.track}'

    def __repr__(self):
        return f'TrackItem(added_at={self.added_at}, added_by={self.added_by}, is_local={self.is_local}, track={self.track})'


class TrackInfo:
    def __init__(self, data):
        self.album = Album(data.get("album", {}))
        self.artists = [Artist(artist) for artist in data.get("artists", [])]
        self.available_markets = data.get("available_markets", [])
        self.disc_number = data.get("disc_number", None)
        self.duration_ms = data.get("duration_ms", None)
        self.explicit = data.get("explicit", False)
        self.external_ids = data.get("external_ids", {})
        self.external_urls = data.get("external_urls", {})
        self.href = data.get("href", None)
        self.id = data.get("id", None)
        self.name = data.get("name", None)
        self.popularity = data.get("popularity", None)
        self.preview_url = data.get("preview_url", None)
        self.track_number = data.get("track_number", None)
        self.type = data.get("type", None)
        self.uri = data.get("uri", None)
        self.is_local = data.get("is_local", False)
        self.episode = data.get("episode", False)

    def __eq__(self, other):
        if not isinstance(other, TrackInfo):
            return False
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'TrackInfo: name={self.name}, artists={self.artists}, album={self.album}'

    def __repr__(self):
        return f'TrackInfo(album={self.album}, artists={self.artists}, available_markets={self.available_markets}, disc_number={self.disc_number}, duration_ms={self.duration_ms}, explicit={self.explicit}, external_ids={self.external_ids}, external_urls={self.external_urls}, href={self.href}, id={self.id}, name={self.name}, popularity={self.popularity}, preview_url={self.preview_url}, track_number={self.track_number}, type={self.type}, uri={self.uri}, is_local={self.is_local}, episode={self.episode})'


class Album:
    def __init__(self, data):
        self.album_type = data.get("album_type", None)
        self.total_tracks = data.get("total_tracks", None)
        self.available_markets = data.get("available_markets", [])
        self.external_urls = data.get("external_urls", {})
        self.href = data.get("href", None)
        self.id = data.get("id", None)
        self.images = data.get("images", [])
        self.name = data.get("name", None)
        self.release_date = data.get("release_date", None)
        self.release_date_precision = data.get("release_date_precision", None)
        self.artists = [Artist(artist) for artist in data.get("artists", [])]

    def __eq__(self, other):
        if not isinstance(other, Album):
            return False
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'Album: name={self.name}, artists={self.artists}, release_date={self.release_date}'

    def __repr__(self):
        return f'Album(album_type={self.album_type}, total_tracks={self.total_tracks}, available_markets={self.available_markets}, external_urls={self.external_urls}, href={self.href}, id={self.id}, images={self.images}, name={self.name}, release_date={self.release_date}, release_date_precision={self.release_date_precision}, artists={self.artists})'


class Artist:
    def __init__(self, data):
        self.external_urls = data.get("external_urls", {})
        self.href = data.get("href", None)
        self.id = data.get("id", None)
        self.name = data.get("name", None)
        self.type = data.get("type", None)
        self.uri = data.get("uri", None)

    def __eq__(self, other):
        if not isinstance(other, Artist):
            return False
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'Artist: name={self.name}, id={self.id}'

    def __repr__(self):
        return f'Artist(external_urls={self.external_urls}, href={self.href}, id={self.id}, name={self.name}, type={self.type}, uri={self.uri})'
