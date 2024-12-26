def check_input_is_integer(msg, start=None, end=None) -> int:
    while True:
        try:
            int_input = int(input(msg))
            if start is not None and end is not None and (int_input < start or int_input > end):
                print("Invalid input! Try again.")
            else:
                return int_input
        except ValueError:
            print("Invalid input! Try again.")
