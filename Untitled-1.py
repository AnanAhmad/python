def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not has_valid_length(s):
        return False
    if not starts_with_letters(s):
        return False
    if not valid_number_position(s):
        return False
    if contains_invalid_characters(s):
        return False
    return True
def has_valid_length(s):
     return 6>= len(s)>=2 
def starts_with_letters(s):
    return s[0:2].isalpha()
def valid_number_position(s):
    for i, char in enumerate(s):
        if char.isdigit():
            # Check if the first digit is zero
            if char == '0' and i == len(s) - 1:
                return False
            # Ensure no digits are in the middle
            if not s[i:].isdigit():
                return False
            break
    return True
def contains_invalid_characters(s):
    """Check for invalid characters (no punctuation or spaces allowed)."""
    return not s.isalnum()
if __name__ == "__main__":
    main()