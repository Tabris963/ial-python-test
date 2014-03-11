from django.test import TestCase
import json

class SchoolTest(TestCase):

    def test_enroll(self):
        resp = self.client.post(
            "/enroll",
            '{"first_name":"Riccardo","last_name":"Zenere"}',
            content_type='application/json'
            )
        self.assertEqual(resp.status_code, 200)

    def test_search(self):
        resp = self.client.post(
            "/enroll",
            '{"first_name":"Riccardo","last_name":"Zenere"}',
            content_type='application/json'
            )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/enroll')
        self.assertEqual(resp.status_code,200)
        content = json.loads(resp.content)
        self.assertEqual(content[0]['first_name'], 'Riccardo')
        self.assertEqual(content[0]['last_name'], 'Zenere')
