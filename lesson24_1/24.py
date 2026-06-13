import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("test_search")
logger.setLevel(logging.INFO)

if not logger.handlers:
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)

    file = logging.FileHandler("test_search.log", encoding="utf-8")
    file.setFormatter(fmt)
    logger.addHandler(file)


@pytest.fixture(scope="class")
def session():
    s = requests.Session()
    resp = s.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))
    assert resp.status_code == 200
    token = resp.json()["access_token"]
    s.headers.update({"Authorization": "Bearer " + token})
    logger.info("Залогінились, токен отримано")
    yield s
    s.close()


class TestCarsSearch:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 10),
        ("year", 5),
        ("engine_volume", 3),
        ("brand", 7),
        ("price", 25),
        (None, 15),
    ])
    def test_search(self, session, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"Запит /cars з параметрами {params}")
        resp = session.get(f"{BASE_URL}/cars", params=params)

        assert resp.status_code == 200
        cars = resp.json()
        assert isinstance(cars, list)
        assert len(cars) > 0

        if limit:
            assert len(cars) <= limit

        if sort_by:
            values = [car[sort_by] for car in cars]
            assert values == sorted(values)

        logger.info(f"OK: повернулось {len(cars)} авто")