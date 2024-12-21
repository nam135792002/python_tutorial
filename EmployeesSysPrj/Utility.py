def check_input_is_integer(msg, start, end) -> int:
    while True:
        try:
            int_input = int(input(msg))
            if int_input < start or int_input > end:
                print("Invalid input! Try again.")
            else:
                return int_input
        except ValueError:
            print("Invalid input! Try again.")
