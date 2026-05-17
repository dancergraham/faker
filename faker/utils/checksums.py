from typing import List, Union

ChecksumValue = Union[int, str]


def _digits_of(number: ChecksumValue) -> List[int]:
    return [int(digit) for digit in str(number)]


def luhn_checksum(number: ChecksumValue) -> int:
    digits = _digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    checksum = sum(odd_digits) + sum(sum(_digits_of(digit * 2)) for digit in even_digits)

    return checksum % 10


def calculate_luhn(partial_number: ChecksumValue) -> int:
    """
    Generates the Checksum using Luhn's algorithm
    """
    check_digit = luhn_checksum(f"{partial_number}0")
    return check_digit if check_digit == 0 else 10 - check_digit
