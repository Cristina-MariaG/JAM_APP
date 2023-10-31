from django.test import TestCase
from back_app.tests.utilities.data import products, product_stock_indisponible

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
        return response_login_user.data["token"]["access_token"]

    def test_create_checkout_session_and_order(self):
        checkout_data = {
            "cart": [
                {
                    "id": 1,
                    "name": "cerises",
                    "description": "confiture à la cerises",
                    "image": "cerises.jpeg",
                    "price": "2",
                    "selectedQuantity": 1,
                }
            ],
            "total": 2,
        }
        checkout_data["accessToken"] = self.test_login_user()

        response_create_checkout_session = self.client.post(
            "/create-checkout-session/",
            data=checkout_data,
            content_type="application/json",
        )

        order_id = response_create_checkout_session.data["order_id"]

        self.assertEqual(response_create_checkout_session.status_code, 200)
        self.assertEqual(order_id, 1)
        return order_id

    def test_create_checkout_and_order_and_checkout_success_put(self):
        order_id = self.test_create_checkout_session_and_order()

        params = {"order_id": order_id}
        response_put_order = self.client.put(
            "/edit-order/",
            params,
            content_type="application/json",
        )

        self.assertEqual(response_put_order.status_code, 200)
        self.assertEqual(response_put_order.data, {"status": "ok"})

    def test_edit_order_that_not_exist(self):
        params = {"order_id": -1}
        response_put_order = self.client.put(
            "/edit-order/",
            params,
            content_type="application/json",
        )

        self.assertEqual(response_put_order.status_code, 406)

    def test_delete_order_that_not_exist(self):
        order_id = 1
        url = f"/delete-order/{order_id}/"

        response_delete_order = self.client.delete(url)

        self.assertEqual(response_delete_order.status_code, 406)

    def test_delete_order_that_exist(self):
        order_id = self.test_create_checkout_session_and_order()
        url = f"/delete-order/{order_id}/"

        response_delete_order = self.client.delete(url)

        self.assertEqual(response_delete_order.status_code, 200)
