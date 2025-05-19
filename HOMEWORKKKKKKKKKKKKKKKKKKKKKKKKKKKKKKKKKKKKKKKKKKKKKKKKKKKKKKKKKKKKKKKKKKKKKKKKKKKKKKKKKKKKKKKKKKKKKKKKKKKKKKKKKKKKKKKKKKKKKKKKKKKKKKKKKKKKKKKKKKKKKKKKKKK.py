def reverse_items(l: list[int]) -> list[int]:
    return [int(str(x)[::-1]) for x in l]


if __name__ == "__main__":
    print(reverse_items([444, 222, 111]))