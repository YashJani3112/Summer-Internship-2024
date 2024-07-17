def caesar_cipher(text, shift, mode):
  """
  Encrypts or decrypts text using Caesar Cipher algorithm.

  Args:
      text: The text to encrypt or decrypt.
      shift: The shift value (positive for encryption, negative for decryption).
      mode: "encrypt" or "decrypt".

  Returns:
      The encrypted or decrypted text.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''
  for char in text:
    if not char.isalpha():
      # Keep non-alphabetic characters unchanged
      result += char
      continue
    new_index = (alphabet.find(char) + shift) % 26
    new_char = alphabet[new_index]
    # Swap between upper and lowercase if necessary
    if char.isupper() and new_char.islower():
      result += new_char.upper()
    elif char.islower() and new_char.isupper():
      result += new_char.lower()
    else:
      result += new_char
  return result

def main():
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      text = input("Enter message to encrypt: ")
      shift = int(input("Enter shift value (positive integer): "))
      encrypted_text = caesar_cipher(text, shift, "encrypt")
      print("Encrypted message:", encrypted_text)
    elif choice == '2':
      text = input("Enter message to decrypt: ")
      shift = int(input("Enter shift value (negative integer): "))
      decrypted_text = caesar_cipher(text, shift, "decrypt")
      print("Decrypted message:", decrypted_text)
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
