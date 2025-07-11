from input import Input
from cost import Cost


def main() -> None:
    user_input = Input()
    input_str = user_input.get()
    s, c = input_str[0], float(input_str[1])

    cost = Cost(s, c)
    final_cost = cost.calculate()

    # Output the result
    print(final_cost)


if __name__ == "__main__":
    """
    Calls the Input class to get the input string,
    then calls the Cost class to calculate the cost
    given the input string.
    """
    main()
