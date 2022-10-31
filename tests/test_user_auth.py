import pytest, allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Autorization")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_method(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)
        self.auth_sid = self.get_cookie(response=response1, cookie_name="auth_sid")
        self.token = self.get_header(response=response1, header_name="x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response=response1, name="user_id")

    @allure.description("This test successfully autorise user by email and password")
    def test_auth_user(self):
        response2 = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response=response2,
            name="user_id",
            expected_value=self.user_id_from_auth_method,
            error_message="User id from auth method is not equal id form check method"
        )

    @allure.description("This test check autorization status w/o sending auth cooke or token")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token}
            )
        elif condition == "no_token":
            response2 = MyRequests.get(
                "/user/auth",
                headers={"auth_sid": self.auth_sid}
            )

        Assertions.assert_json_value_by_name(
            response=response2,
            name="user_id",
            expected_value=0,
            error_message=f"User is authorized with condition {condition}"
        )
