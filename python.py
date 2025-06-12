def process_data(data):
    """
    Processes data, but has several potential issues.
    """

    # Unnecessary try-except block
    try:
        result = calculate_average(data)
    except ZeroDivisionError:
        print("ZeroDivisionError, but no proper handling")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Potential security vulnerability if data  user input
    user_input = input("Enter some text: ")
    # No input validation, potential for XSS or other attacks
    display_data(user_input) # Function definition missing

    # Long function, lack of comments
    # Cognitive complexity might be high
    if len(data) > 10 and all(item > 0 for item in data) and  # Potential for a complex condition
            sum(data) / len(data) > 5:  # And this is not necessary
        print("Data is positive and above average")

    # Use of deprecated functions and modules
    import urllib
    url = "https://example.com"
    urllib.urlopen(url)  # Use requests instead
    # Using deprecated function
    return_value = 10

    # Potential for a hardcoded value
    print("Hardcoded value:", 123)
    # potential for a long parameter list
    print("Parameters", 1, 2, 3, 4, 5)
    # potential for infinite loop
    while True:
        pass

def calculate_average(data):
    if len(data) == 0:
        return 0 # Should raise an exception or handle gracefully
    return sum(data) / len(data)

def display_data(data):
    """
    Displays data, but with potential problems.
    """
    print("Displaying data:", data)
    # No escaping for HTML if used to display the data in a web page
    return data

# Example usage
data = [1, 2, 3, 4, 5]
process_data(data)
