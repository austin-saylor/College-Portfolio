def answer(a: int, b: int) -> str:
    ans = []
    if a > b:
        ans.append(b)
        ans.append(a)
    else:
        ans.append(a)
        ans.append(b)

    answer_str = str(ans[0]) + " " + str(ans[1])

    return answer_str


def main() -> None:
    line = input()
    a, b = line.split()
    ans = answer(int(a), int(b))
    print(ans)


if __name__ == "__main__":
    main()
