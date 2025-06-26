import pytest

import data

import sender_stand_request

def get_data_kits(name):
    kit_body = data.kit_body.copy()
    kit_body['name'] = name
    return kit_body

def get_login_token(token):
    user_headers = data.auth_header.copy()
    user_headers['Authorization'] = 'Bearer {}'.format(token)
    return user_headers

@pytest.mark.parametrize("kit_name",[
    "A",
    "A" * 511,
    '"№%@",',
    " A Aaa ",
    "123"
])
def test_kit_name_length_positive_asserts(kit_name):
    user_token = sender_stand_request.authentication(data.user_body)
    headers = get_login_token(user_token.json())
    body_req = get_data_kits(kit_name)
    res = sender_stand_request.create_kit(headers, body_req)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name

@pytest.mark.parametrize("kit_name",[
    "",
    "A" * 512,
    123
])
def test_kit_name_length_negative_asserts(kit_name):
    user_token = sender_stand_request.authentication(data.user_body)
    headers = get_login_token(user_token.json())
    body_req = get_data_kits(kit_name)
    res = sender_stand_request.create_kit(headers, body_req)
    assert res.status_code == 400

def test_kit_name_without_name():
    user_token = sender_stand_request.authentication(data.user_body)
    headers = get_login_token(user_token.json())
    body_req = get_data_kits("")
    body_req.pop("name")
    res = sender_stand_request.create_kit(headers, body_req)
    assert res.status_code == 400
