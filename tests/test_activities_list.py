def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == 9


def test_get_activities_items_have_expected_fields(client):
    response = client.get("/activities")
    payload = response.json()

    chess = payload["Chess Club"]
    assert set(chess.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(chess["participants"], list)
