import unittest
from unittest.mock import patch
from login_system import log_event

class TestLogEvent(unittest.TestCase):

    @patch("login_system.logging.getLogger")
    def test_success_logs_info(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value

        log_event("john", "success")

        mock_logger.info.assert_called_once_with(
            "Login event - Username: john, Status: success"
        )

    @patch("login_system.logging.getLogger")
    def test_expired_logs_warning(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value

        log_event("john", "expired")

        mock_logger.warning.assert_called_once_with(
            "Login event - Username: john, Status: expired"
        )

    @patch("login_system.logging.getLogger")
    def test_failed_logs_error(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value

        log_event("john", "failed")

        mock_logger.error.assert_called_once_with(
            "Login event - Username: john, Status: failed"
        )

if __name__ == "__main__":
    unittest.main()