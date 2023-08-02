import unittest

from reg_exps import (
    find_emails,
    validate_date_format,
    extract_email_parts,
    validate_phone_number,
    split_sentences,
)


class TestFunctions(unittest.TestCase):
    def test_find_emails(self):
        text = "Contact us at test@gmail.com or info@example.org / contacts@ukr.net"
        expected_result = ["test@gmail.com", "info@example.org", "contacts@ukr.net"]
        result = find_emails(text)
        self.assertEqual(result, expected_result)

    def test_validate_date_format(self):
        valid_date = "12/31/2022"
        invalid_date = "12-31-2022"
        self.assertTrue(validate_date_format(valid_date))
        self.assertFalse(validate_date_format(invalid_date))

    def test_extract_email_parts(self):
        email = "info@example.com"
        expected_name = "info"
        expected_domain = "example.com"
        name, domain = extract_email_parts(email)
        assert name == expected_name
        assert domain == expected_domain

    def test_validate_phone_number(self):
        valid_number = "+380501234567"
        invalid_number = "1234567890"
        self.assertTrue(validate_phone_number(valid_number))
        self.assertFalse(validate_phone_number(invalid_number))

    def test_split_sentences(self):
        text = (
            "This is sentence one. And; this is sentence two? Finally, sentence three!"
        )
        expected_result = [
            "This is sentence one.",
            "And; this is sentence two?",
            "Finally, sentence three!",
        ]
        result = split_sentences(text)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
