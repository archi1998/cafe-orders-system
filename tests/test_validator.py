# tests/test_validator.py
from src.validator import is_valid_email
from unittest.mock import patch

def test_is_valid_email():
    with patch('src.validator.re.match') as mock_match:
        mock_match.return_value = True
        assert is_valid_email("test@example.com") == True
