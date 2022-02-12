


import art




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(art.logo)
end_of_game =False
while end_of_game==False  :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift=shift%26

    if direction == "decode":
        shift *= -1

    def ceaser(text,shift,new_direction):
        cipher = ""

        for letters in text:
            if letters in alphabet:
                a = alphabet.index(letters)

                new_a=a+shift
                new_letter = alphabet[new_a]
                cipher += new_letter
            else:
                cipher+=letters
        print(cipher)
    ceaser(text,shift,new_direction=direction)
    aka = input(str("do you want to continnue yes or no"))
    if aka == "yes":
        end_of_game = False
    else:
        end_of_game=True
        print("Thank you for using this")










