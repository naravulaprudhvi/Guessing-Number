from app import app


def test_home_page():
    client = app.test_client()
    assert client.get("/").status_code == 200


def test_add_item():
    client = app.test_client()
    client.post("/add", data={"text": "Buy milk"})
    assert b"Buy milk" in client.get("/").data


def test_health():
    assert app.test_client().get("/health").get_json()["status"] == "ok"
