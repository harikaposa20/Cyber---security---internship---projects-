from cryptography.fernet import Fernet


# Generate and save encryption key

def generate_key():
    key = Fernet.generate_key()

    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

    print("Encryption key generated and saved.")


# Load encryption key

def load_key():
    return open('secret.key', 'rb').read()


# Encrypt file

def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print("File encrypted successfully.")


# Decrypt file

def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    output_file = file_name.replace('.encrypted', '.decrypted')

    with open(output_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print("File decrypted successfully.")


if __name__ == '__main__':
    print("Advanced Encryption Tool")

    choice = input("1. Generate Key\n2. Encrypt File\n3. Decrypt File\nChoose option: ")

    if choice == '1':
        generate_key()

    elif choice == '2':
        file_name = input("Enter file name to encrypt: ")
        encrypt_file(file_name)

    elif choice == '3':
        file_name = input("Enter encrypted file name: ")
        decrypt_file(file_name)

    else:
        print("Invalid option.")