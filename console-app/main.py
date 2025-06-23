def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def process_user_input():
    user_input = input("Écrivez un truc ici : ")
    print(user_input if not is_palindrome(user_input) else "Bien dit !", end="\n")


def process_console():
    print("Bonjour !", end="\n")
    try:
        while True:
            process_user_input()
    except (KeyboardInterrupt, EOFError):
        print("\nAu revoir !", end="\n")


def main():
    process_console()


if __name__ == "__main__":
    main()
