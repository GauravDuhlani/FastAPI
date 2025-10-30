from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user, test_todo):
    response = client.get("/user/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["User Details"]["username"] == "coding with test"
    assert response.json()["User Details"]["email"] == "codingwithtest@gmail.com"
    assert response.json()["User Details"]["first_name"] == "Coding"
    assert response.json()["User Details"]["last_name"] == "Test"
    assert response.json()["User Details"]["role"] == "admin"
    assert response.json()["User Details"]["phone_number"] == "(111)-111-1111"
    assert response.json()["User Details"]["is_active"] == True
    assert response.json()["User Details"]["id"] == 1

    assert response.json()["Todos"][0]["title"] == "Learn to code!"
    assert response.json()["Todos"][0]["description"] == "Need to learn everyday"
    assert response.json()["Todos"][0]["priority"] == 5
    assert response.json()["Todos"][0]["complete"] == False
    assert response.json()["Todos"][0]["owner_id"] == 1


def test_change_password_success(test_user):
    user_verification = {
        "password": "testpassword",
        "new_password": "newtestpassword",
    }
    response = client.put("/user/change-password", json=user_verification)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    user_verification = {
        "password": "wrongpassword",
        "new_password": "newtestpassword",
    }
    response = client.put("/user/change-password", json=user_verification)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Error on password change!"


def test_change_phone_number_success(test_user):
    response = client.put("/user/update-phone-number/2222222222")
    assert response.status_code == status.HTTP_204_NO_CONTENT
