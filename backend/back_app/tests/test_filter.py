from django.test import TestCase
from back_app.tests.utilities.data import products, product_stock_indisponible

import logging

logger = logging.getLogger("jam")


class TestFilterProducts(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_filtered_products_no_filter(self):
        response_get = self.client.get(
            "/filter/",
        )

        self.assertEqual(response_get.status_code, 200)

        data = products

        self.assertEqual(response_get.data, data)

    def test_get_filtered_products_available_stock_false(self):
        params = {"availableStock": "false"}
        response_get = self.client.get("/filter/", params)

        self.assertEqual(response_get.status_code, 200)
        data = product_stock_indisponible

        self.assertEqual(response_get.data, data)
