alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ask=input("type 'encode' to encrupt and 'decode' to decrypt \n")
text=input("enter the text\n").lower()
shift=int(input("enter the key pairs to shift\n"))


def encrypt(plain_text,shift_key):
    encode=""
    for letter in plain_text:
        position=alphabet.index(letter) #e
        new_position=position+shift_key #+5
        encode+=alphabet[new_position]
        #encode=encode+alphabet[new_position]
    print(f"the encoded string is {encode}")


def decrypt(plain_text,shift_key):
    decode=""
    for letter in plain_text:
        position=alphabet.index(letter) #e
        new_position=position-shift_key #+5
        decode+=alphabet[new_position]
        #encode=encode+alphabet[new_position]
    print(f"the encoded string is {decode}")


if ask == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif ask == "decode":
  decrypt(plain_text=text, shift_key=shift)
        
