def colors():
    all_colors = ["white", "red", "blue", "white", "purple", "red", "black", "white", "black"]

    # 1 - print every color
    count = 0
    for color in all_colors:
        print(color)

        if color == "white" or "black":
            count += 1


    print("The result is " + count)

    # fn calls
colors()