from django.test import TestCase

import logging

logger = logging.getLogger("jam")


class TestCheckoutSessionProducts(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_login_user(self):
        response_login_user = self.client.post(
            "/login/",
            data={
                "email": "admin@admin.com",
                "password": "adminlovejam",
            },
        )

        self.assertEqual(response_login_user.status_code, 200)
        return response_login_user.data["token"]

    def test_refresh_token_generate(self):
        token = self.test_login_user()
        response_post_token = self.client.post(
            "/refresh-token/",
            data={"refresh_token": token["refresh_token"]},
        )

        self.assertEqual(response_post_token.status_code, 200)
        self.assertIn("token", response_post_token.data)
        self.assertIn("refresh_token", response_post_token.data["token"])
        self.assertIn("access_token", response_post_token.data["token"])
