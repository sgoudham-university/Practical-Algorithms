from stack import Stack

url_stack = Stack(100)
url_stack.push("home.html")


def main():
    while True:
        user_input = input(
            f"\nYou are currently on {url_stack.peek()}. \nEnter the url you wish to visit next (or 'q' to quit, 'b' to go back to previous url): ")
        if user_input.lower().strip() == "q":
            break
        elif user_input.lower().strip() == "b":
            if url_stack.peek() == "home.html":
                print("Operation Denied, No Previous Webpage")
            else:
                url_stack.pop()
        else:
            url_stack.push(user_input)


if __name__ == "__main__":
    main()
