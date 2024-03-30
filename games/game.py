from classes import Field

field = Field(4)

while True:
    field.add_new()
    for i in field.grld:
        for j in i:
            print(f"{j:<4}", end=" ")
        print()
        print()
    reply = input("Enter a direction: ")
    match reply:
        case "w":
            field.move(0)
        case "s":
            field.move(1)
        case "a":
            field.move(2)
        case "d":
            field.move(3)
        case "":
            pass
        case _:
            break
    print()
