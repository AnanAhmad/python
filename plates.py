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
    firstnum = None
    for c in s:
        if c.isdigit():
            firstnum = c
            break
    if firstnum == None:
        return True
    if int(firstnum) == 0:
        return False
    index = s.index(firstnum)
    position = len(s) - index
    for c in s[-position:]:
        if not c.isdigit():
            return False
    return True
def contains_invalid_characters(s):
    """Check for invalid characters (no punctuation or spaces allowed)."""
    return not s.isalnum()
if __name__ == "__main__":
    main()
