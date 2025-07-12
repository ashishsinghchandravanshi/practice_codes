ch = input("Enter a single character: ")


if len(ch) == 1 and ch.isalpha():
    # Convert to lowercase to handle both cases
    ch_lower = ch.lower()
    if ch_lower in ['a', 'e', 'i', 'o', 'u']:
        print("It is a Vowel.")
    else:
        print("It is a Consonant.")
else:
    print("Invalid input! Please enter a single alphabet character only.")
