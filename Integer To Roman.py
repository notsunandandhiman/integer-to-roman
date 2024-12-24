def int_to_roman(num):
    # Define a list of tuples containing Roman numerals and their corresponding integer values
    val = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    roman_numeral = ''
    
    # Iterate over the values and build the Roman numeral
    for (integer, roman) in val:
        while num >= integer:
            roman_numeral += roman
            num -= integer
            
    return roman_numeral

# Example usage
if __name__ == "__main__":
    # Input from the user
    try:
        number = int(input("Enter an integer (1-3999): "))
        if 1 <= number <= 3999:
            print(f"The Roman numeral for {number} is: {int_to_roman(number)}")
        else:
            print("Please enter a number between 1 and 3999.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")