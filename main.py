from Main_menu import main_menu


def main():
    try:
        main_menu()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting the program. Hope to see you again soon!")
    except Exception as error:
        print(f"Unexpected error: {error}")
        print("The program will now exit.")


if __name__ == "__main__":
    main()