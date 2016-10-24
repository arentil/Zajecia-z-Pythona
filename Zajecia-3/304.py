while True:
    reply = input("Wpisz tekst:")
    if reply == "stop":
        break
    try:
        x = int(reply)
    except ValueError:
        print("To nie jest liczba!")
    else:
        print(x, x**3)