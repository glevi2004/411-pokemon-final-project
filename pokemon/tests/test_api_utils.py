# tests/test_api.py

import pytest
from requests.exceptions import HTTPError

from pokemon.api import PokemonAPI


class DummyResponse:
    """Minimal stand-in for requests.Response"""
    def __init__(self, data, status_code=200):
        self._data = data
        self.status_code = status_code

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise HTTPError(f"Status code: {self.status_code}")

    def json(self):
        return self._data


@pytest.fixture
def api():
    return PokemonAPI()


def test__make_request_success(monkeypatch, api):
    dummy = {"foo": "bar"}
    # patch session.get to return our dummy 200-response
    monkeypatch.setattr(api.session, "get", lambda url: DummyResponse(dummy, 200))

    result = api._make_request("pokemon/42")
    assert result == dummy


def test__make_request_raises_on_http_error(monkeypatch, api):
    # patch session.get to return a 404
    monkeypatch.setattr(api.session, "get", lambda url: DummyResponse(None, 404))

    with pytest.raises(HTTPError):
        api._make_request("pokemon/not-found")


def test_get_pokemon_delegates_to__make_request(monkeypatch, api):
    # intercept _make_request so no network is needed
    monkeypatch.setattr(api, "_make_request", lambda endpoint: {"name": "pikachu"})
    data = api.get_pokemon("pikachu")
    assert data == {"name": "pikachu"}


def test_get_evolution_chain_delegates_to__make_request(monkeypatch, api):
    monkeypatch.setattr(api, "_make_request", lambda endpoint: {"chain": [1,2,3]})
    data = api.get_evolution_chain(7)
    assert data == {"chain": [1,2,3]}


def test_search_pokemon_not_implemented(api):
    # currently search_pokemon is a stub (pass), so it returns None
    assert api.search_pokemon("pika") is None
