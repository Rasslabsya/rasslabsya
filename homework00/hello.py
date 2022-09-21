def get_greeting(name: str) -> str:
    return "hello, " + name  + "!"

if __name__ == "__main__":
    message = get_greeting('DANYA')
    print(message)
