import sender_stand_request
def test_create_order():
    response_create_order = sender_stand_request.post_new_order()
    track = response_create_order.json()["track"]
    response_get_order = sender_stand_request.get_track_order(track)
    assert response_get_order.status_code == 200

