from django.test import TestCase
import logging

logger = logging.getLogger("jam")


class TestCategory(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_categories(self):
        response_get = self.client.get(
            "/category/",
        )
        self.assertEqual(response_get.status_code, 200)
        data = {
            "categories": [
                {"id": 1, "category": "Preserves"},
                {"id": 2, "category": "Jellies"},
                {"id": 3, "category": "Jams"},
            ]
        }
        self.assertEqual(response_get.data, data)
