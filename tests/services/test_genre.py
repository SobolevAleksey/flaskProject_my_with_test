from unittest.mock import MagicMock
import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService
from setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    action = Genre(id=1, name='action')
    comedy = Genre(id=2, name='comedy')
    horror = Genre(id=3, name='horror')

    genre_dao.get_one = MagicMock(return_value=action)
    genre_dao.get_all = MagicMock(return_value=[action, comedy, horror])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "name": "drama"
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id != None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "id": 3,
            "name": "drama"
        }
        self.genre_service.update(genre_d)
        
    def test_partially_update(self):
        genre_d = {
            "id": 3
        }
        self.genre_service.partially_update(genre_d)
