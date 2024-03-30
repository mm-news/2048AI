from classes import Field

field = Field(4)

while True:
    field.add_new()
    for i in field.grld:
        print(i)
    reply = input("Enter a direction: ")
    match reply:
        case "0":
            field.move(0)
        case "1":
            field.move(1)
        case "2":
            field.move(2)
        case "3":
            field.move(3)
        case _:
            break
    print()
