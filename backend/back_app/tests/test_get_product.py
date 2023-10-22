from django.test import TestCase
from back_app.tests.utilities.data import product_1, products


class TestProduct(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_product(self):
        product_id = 1
        url = f"/product/{product_id}/"
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)
        data = product_1
        self.assertEqual(response_get.data, data)

    def test_get_products(self):
        response_get = self.client.get(
            "/product/",
        )
        self.assertEqual(response_get.status_code, 200)
        data = products

        self.assertEqual(response_get.data, data)
