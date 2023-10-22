from django.test import TestCase


class TestTypeContenant(TestCase):
    fixtures = ["initial_data_for_SQL_test_DB.json"]

    def setUp(cls):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_brands(self):
        response_get = self.client.get(
            "/contenant-type/",
        )
        data = {
            "contenant_types": [
                {"id": 1, "type_contenant": "glass"},
                {"id": 2, "type_contenant": "plastic"},
                {"id": 3, "type_contenant": "metal"},
            ]
        }

        self.assertEqual(response_get.data, data)
