import unittest
from login_system import log_event


class TestLogEvent(unittest.TestCase):

    def test_success_logs_info(self):
        log_event("john", "success")

        with open("login_system.log", "r") as f:
            content = f.read()

        self.assertIn("Login event - Username: john, Status: success", content)

    def test_expired_logs_warning(self):
        log_event("john", "expired")

        with open("login_system.log", "r") as f:
            content = f.read()

        self.assertIn("Login event - Username: john, Status: expired", content)

    def test_failed_logs_error(self):
        log_event("john", "failed")

        with open("login_system.log", "r") as f:
            content = f.read()

        self.assertIn("Login event - Username: john, Status: failed", content)


if __name__ == "__main__":
    unittest.main()