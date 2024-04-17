import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize the phone number for Ukrainian format
    """
    # get int fron user string
    clear_number = re.findall(r"\d+", phone_number)
    join_number = "".join(clear_number)

    # Check if valid phone number
    if len(join_number) >= 9 and len(join_number) <= 13:
        # get phone number
        remove_code = join_number[len(join_number) - 9 : len(join_number)]
        # get ukr international code
        int_code_ukr = "+380"
        return f"{int_code_ukr}{remove_code}"
    # if invalid phone number return None
    else:
        return None


if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\",
        "44 123 4565",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
