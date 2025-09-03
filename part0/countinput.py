def countchars:
    exclude = {' ', '.', '!', ','}
    count = 0
    for ch in st:
        if ch not in exclude:
            count += 1
    return count


def main():
    user_input = input("Enter a string: ")
    result = countchars(user_input)
    print(result)

