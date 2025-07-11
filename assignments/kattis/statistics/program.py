from results import Results


class Program:
    def run(self) -> None:
        """
        Run the program.
        """
        case_num = 1
        while True:
            try:
                case = list(map(int, input().split()))
                if not case:  # Handle empty input line
                    continue
                results = Results(case, case_num)
                result = results.get()
                print(result)
                case_num += 1
            except EOFError:
                break
            except ValueError:
                break
