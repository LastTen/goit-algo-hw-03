import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generate a set of unique random numbers
    """
    # Validation of input data
    if min >= 1 and max <= 1000 and quantity >= min and quantity <= max:
        numbers = []

        # Fill the numbers with random unique numbers
        while len(numbers) < quantity:
            number = random.randint(min, max)
            if number not in numbers:
                numbers.append(number)
        return numbers
    # returns an error if the data is invalid
    else:
        return "Error: invalid input"


if __name__ == "__main__":
    print(get_numbers_ticket(1, 20, 5))
    print(get_numbers_ticket(20, 1, 1))
    print(get_numbers_ticket(1, 20, 0))
