from abc import abstractmethod, ABC
from typing import List, Union

from core.models import Song, Playlist, Album


class BaseProvider(ABC):
    def __init__(self):
        self._name: str = ''
        self._playlists: List[Playlist] = []
        self._result: List[Song] = []

    @abstractmethod
    def init(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def search_songs(self, query) -> None:
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def result(self) -> List[Song]:
        return self._result

    @abstractmethod
    def get_playlists(self):
        pass

    @abstractmethod
    def add_playlist(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def put_playlist(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def delete_playlist(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def get_album_image(self, *args, **kwargs) -> Union[None, bytes]:
        pass

    @property
    def playlists(self):
        return self._playlists

    @abstractmethod
    def add_to_playlist(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def delete_from_playlist(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def get_albums(self, *args, **kwargs) -> List[Album]:
        pass

    @abstractmethod
    def get_playlist_songs(self, *args, **kwargs) -> List[Song]:
        pass

    @abstractmethod
    def get_album_songs(self, *args, **kwargs) -> List[Song]:
        pass

    @abstractmethod
    def get_album_info(self, *args, **kwargs) -> Album:
        pass

    def __repr__(self):
        return self._name
