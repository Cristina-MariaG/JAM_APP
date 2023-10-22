from django.test import TestCase


class TestBrand(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_brands(self):
        response_get = self.client.get(
            "/brand/",
        )
        data = {
            "brand_list": [
                {"id": 1, "brand": "jam 1 producter"},
                {"id": 2, "brand": "jam 2 producter"},
            ]
        }
        self.assertEqual(response_get.data, data)
