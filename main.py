def encoder(password):  # antonio diaz
    encoded = ''
    for idx in range(len(password)):
        if int(password[idx]) > 7:
            encoded += str(((int(password[idx]) + 3) % 10))
        else:
            encoded += str(int(password[idx]) + 3)
    print(encoded)
    return encoded

def decode(password):
    decoded_password = []
    for i in range(len(password)):
        result = int(password[i])
        result = (result - 3) % 10
        decoded_password.append(str(result))
    decoded_pass = ''.join(decoded_password)
    return decoded_pass


Condition = True

while Condition:
    print("Menu\n""-------------\n""1. Encode\n""2. Decode\n""3. Quit\n"" ")
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encoder(password)
        print("Your password has been encoded and stored!")

    if option == 2:
        decoded_pass = decode(encoded_password)
        print(f"The encoded password is {encoded_password} and the original password is {decoded_pass}.")

    if option == 3:
        Condition = False
