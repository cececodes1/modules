import text_utils as text_utils

def main():

    original_string = "hello world"
    print("Original String:", original_string)

    reversed_string = text_utils.reverse_string(original_string)
    print("Reversed String:", reversed_string)

    capitalized_string = text_utils.capitalize_string(original_string)
    print("Capitalized String:", capitalized_string)

main()