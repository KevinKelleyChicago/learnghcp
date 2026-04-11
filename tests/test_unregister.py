from src.app import activities


def test_unregister_success_removes_participant(client):
    activity_name = "Chess Club"
    participant = activities[activity_name]["participants"][0]

    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": participant},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {participant} from {activity_name}"
    }
    assert participant not in activities[activity_name]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Unknown%20Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_missing_participant_returns_404(client):
    response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": "ghost@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found in this activity"}
