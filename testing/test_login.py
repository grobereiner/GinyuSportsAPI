import unittest

from server_API.user import User
from server_API.iniciar_servidor import app

class Testear(unittest.TestCase):
    def test_signup_success(self):
        self.assertEqual(User.signup(self, "ginyusportsapi@gmail.com", "pruebas", app.secret_key),
                         "Signup success, logged in")

    def test_signup_email_exists(self):
        self.assertEqual(User.signup(self, "ginyusportsapi@gmail.com", "pruebas", app.secret_key),
                         "Email already exists")

    def test_signup_email_not_valid(self):
        self.assertEqual(User.signup(self, "ginyusportsapi@gmail", "pruebas", app.secret_key),
                         "Email inválido")

    def test_login_success(self):
        self.assertEqual(User.login(self, "ginyusportsapi@gmail.com", "pruebas", app.secret_key),
                         "Login success")

    def test_login_failed(self):
        self.assertEqual(User.login(self, "ginyusportsapi@gmail.com", "noeslaclave", app.secret_key),
                         "Invalid login credentials")

    def test_signout(self):
        self.assertEqual(User.signout(self), "Signed out")


if __name__ == "__main__":
    unittest.main()
