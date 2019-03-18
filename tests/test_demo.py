import pytest

from app.demo import f

@pytest.fixture
def mock_g_fixture(monkeypatch):
    def mock_g():
        return "tout fonctionne"

    monkeypatch.setattr('app.demo.g', mock_g)
    
def test_f_is_ok(mock_g_fixture):
    assert f() == 'tout fonctionne'

def test_f_is_still_ok(mock_g_fixture):
    r = f()

    assert r == "tout fonctionne"
    

