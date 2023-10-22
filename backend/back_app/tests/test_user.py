from django.test import TestCase
import logging

logger = logging.getLogger("jam")


class TestUser(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_user(self):
        response_post = self.client.post(
            "/login/",
            data={
                "email": "admin@admin.com",
                "password": "adminlovejam",
            },
        )
        logger.error(response_post.data)
        self.assertEqual(response_post.status_code, 200)

    def test_inscription_user(self):
        response_post = self.client.post(
            "/inscription/",
            data={
                "email": "arc_cris@yahoo.com",
                "password": "crislovejam",
            },
        )

        self.assertEqual(response_post.status_code, 200)

    def test_creating_existing_user(self):
        response_post = self.client.post(
            "/inscription/",
            data={
                "email": "admin@admin.com",
                "password": "adminlovejam",
            },
        )

        self.assertEqual(response_post.status_code, 403)

    def test_getting_unexisting_user(self):
        response_post = self.client.post(
            "/login/",
            data={
                "email": "admin_test@admin.com",
                "password": "adminlovejam",
            },
        )

        self.assertEqual(response_post.status_code, 404)

    def test_getting_user_with_wrong_password(self):
        response_post = self.client.post(
            "/login/",
            data={
                "email": "admin@admin.com",
                "password": "admindoesnotlovejam",
            },
        )

        self.assertEqual(response_post.status_code, 401)
