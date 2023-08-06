from abc import abstractmethod

from PySide6.QtCore import QAbstractTableModel, QModelIndex
from PySide6.QtGui import Qt, QPixmap

from core.enum import SongIndex
from utils import aio
from utils.show import show_duration


class SongModel(QAbstractTableModel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.labels = ['', '歌曲', '歌手', '专辑', '时长']

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.labels[section]
        return super().headerData(section, orientation, role)

    def data(self, index, role=None):
        if role == Qt.ItemDataRole.DisplayRole:
            song = self.songs[index.row()]
            if index.column() != 0:
                if index.column() == 4:
                    return show_duration(song.__getattribute__(SongIndex(index.column()).name))
                return song.__getattribute__(SongIndex(index.column()).name)
            return index.row() + 1

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 5

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.songs)

    @property
    @abstractmethod
    def songs(self):
        pass


class SearchResultModel(SongModel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)

    @property
    def songs(self):
        return self._app.default_provider.result


class PlaylistSongsModel(SongModel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        self._pid = None
        self._songs = []
        aio.create(self.get_songs())

    @property
    def songs(self):
        return self._songs

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
        aio.create(self.get_songs())

    async def get_songs(self):
        if self._pid:
            songs = await self._app.default_provider.get_playlist_songs(self._pid)
            self._songs.clear()
            self._songs.extend(songs)
            self.layoutChanged.emit()


class AlbumSongsModel(SongModel):
    def __init__(self, app, *args, **kwargs):
        self._album_id = None
        self._songs = []
        super().__init__(app, *args, **kwargs)

    @property
    def songs(self):
        return self._songs

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
        self.get_songs()

    def get_songs(self):
        aio.create(self._get_songs())

    async def _get_songs(self):
        songs = await self._app.default_provider.get_album_songs(self._album_id)
        self._songs.clear()
        self._songs.extend(songs)
        self.layoutChanged.emit()


class AlbumModel(QAbstractTableModel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.labels = ['', '专辑', '歌手', '年份']
        self.albums = []
        self.cache = {}

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.labels[section]
        return super().headerData(section, orientation, role)

    def data(self, index, role=None):
        if role == Qt.ItemDataRole.DisplayRole:
            album = self.albums[index.row()]
            if index.column() == 1:
                return album.name
            elif index.column() == 2:
                return album.artist
            elif index.column() == 3:
                return album.date if album.date else ''

        elif role == Qt.ItemDataRole.DecorationRole:
            if index.column() == 0:
                a = QPixmap()
                if index.row() in self.cache:
                    a.loadFromData(self.cache[index.row()])
                else:
                    a.load(':/icons/default_album.png')
                a.scaledToHeight(64)
                return a

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 4

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.albums)

    def search_albums(self, kw):
        aio.create(self._search_album(kw))

    async def _search_album(self, kw):
        albums = await self._app.default_provider.get_albums(kw)
        self.albums.clear()
        self.albums.extend(albums)
        self.layoutChanged.emit()
        for i, al in enumerate(albums):
            aio.create(self._get_album_image(i, al.id))

    async def _get_album_image(self, i, aid):
        img = await self._app.default_provider.get_album_image(aid, 64)
        self.cache[i] = img
        self.layoutChanged.emit()
