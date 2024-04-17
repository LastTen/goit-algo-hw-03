from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Returns the number of days from today
    """
    # Format check
    try:
        # get date from user
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        return e  # return error message

    # get current date
    today = datetime.today()

    return int((today - date).days)


if __name__ == "__main__":
    print(get_days_from_today("2024-02-01"))
    print(get_days_from_today("2024-01"))
