from django.test import TestCase

class TestPrices(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_brands(self):
        response_get = self.client.get(
            "/prices-min-max/",
        )
        self.assertEqual(response_get.status_code, 200)

        data = {'price__min': '2', 'price__max': '7'}

        self.assertEqual(response_get.data, data)
