import re


def find_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(pattern, text, re.IGNORECASE)
    return emails


def validate_date_format(date_str):
    pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|1\d|2\d|3[01])/\d{4}$"
    return bool(re.match(pattern, date_str))


def extract_email_parts(email):
    pattern = r"^([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})$"
    match = re.match(pattern, email)
    if match:
        name = match.group(1)
        domain = match.group(2)
        return name, domain
    else:
        return None, None


def validate_phone_number(phone_number):
    # pattern only for Ukrainian phone numbers
    pattern = r"^(\+?380|0)\d{9}$"
    return bool(re.match(pattern, phone_number))


def split_sentences(text):
    pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
    sentences = re.split(pattern, text)
    return sentences
