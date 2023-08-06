import logging

from PySide6.QtWidgets import QTabWidget

from foru.ui.albumlist import AlbumListWidget
from foru.ui.models import SearchResultModel, AlbumModel
from foru.ui.songlist import SongListWidget
from foru.utils import aio

logger = logging.getLogger('foru.ui.searchtab')


class SearchTab(QTabWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.setObjectName('searchTab')

        self.song_model = SearchResultModel(app)
        self.search_tab = SongListWidget(app, self.song_model, self)
        self.addTab(self.search_tab, '歌曲')

        self.album_model = AlbumModel(app)
        self.album_tab = AlbumListWidget(app, self.album_model)
        self.addTab(self.album_tab, '专辑')

        self.currentChanged.connect(lambda: self.search(self.parent().parent().search_bar.text()))

    def search(self, kw):
        if kw:
            if self.currentIndex() == 0:
                aio.create(self._search_songs(kw))
            elif self.currentIndex() == 1:
                self.album_model.search_albums(kw)

    async def _search_songs(self, kw):
        if self._app.default_provider:
            songs = await self._app.default_provider.search_songs(kw)
            if songs:
                self.song_model.layoutChanged.emit()
