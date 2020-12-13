import unittest
from app.models import Rider


class RiderModelTest(unittest.TestCase):

    def setUp(self):
        self.new_rider = Rider(password='20302000b')

    def test_password_setter(self):
        self.assertTrue(self.new_rider.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_rider.password

    def test_password_verification(self):
        self.assertTrue(self.new_rider.verify_password('20302000b')) 
