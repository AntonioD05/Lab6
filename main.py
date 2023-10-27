def encoder(password):
    encoded = ''
    for idx in range(len(password)):
        if int(password[idx]) > 7:
            encoded += str(((int(password[idx]) + 3) % 10))
        else:
            encoded += str(int(password[idx]) + 3)
    return encoded




Condition = True

while Condition:
    print("Menu\n""-------------\n""1. Encode\n""2. Decode\n""3. Quit\n"" ")
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        print(encoder(password))
    if option == 2:
        pass
    if option == 3:
        Condition = False
