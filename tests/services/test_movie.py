from unittest.mock import MagicMock
import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    one = Movie(id=1, title='123', description="321")
    two = Movie(id=2, title='456', description="654")
    three = Movie(id=3, title='789', description="987")

    movie_dao.get_one = MagicMock(return_value=one)
    movie_dao.get_all = MagicMock(return_value=[one, two, three])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    movie_dao.partially_update = MagicMock()
    return movie_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "789",
            "description": "987"
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def test_delete(self):
        self.movier_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "789",
            "description": "987"
        }
        self.movie_service.update(movie_d)
        
    def test_partially_update(self):
        movie_d = movie_d = {
            "id": 3,
            "title": "789",
            "description": "987"
        }
        self.movie_service.partially_update(movie_d)
