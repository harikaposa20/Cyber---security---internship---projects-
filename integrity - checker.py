import hashlib
import os


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_hash(file_path, hash_value):
    with open('hash_records.txt', 'a') as file:
        file.write(f"{file_path}:{hash_value}\n")


def verify_file(file_path):
    current_hash = calculate_hash(file_path)

    if not os.path.exists('hash_records.txt'):
        print("No previous hash records found.")
        return

    with open('hash_records.txt', 'r') as file:
        records = file.readlines()

    for record in records:
        saved_file, saved_hash = record.strip().split(':')

        if saved_file == file_path:
            if saved_hash == current_hash:
                print("File integrity verified. No changes detected.")
            else:
                print("Warning! File has been modified.")
            return

    print("File record not found.")


if __name__ == '__main__':
    file_path = input("Enter file path: ")

    if os.path.exists(file_path):
        choice = input("1. Save Hash\n2. Verify File\nChoose option: ")

        if choice == '1':
            hash_value = calculate_hash(file_path)
            save_hash(file_path, hash_value)
            print("Hash saved successfully.")

        elif choice == '2':
            verify_file(file_path)

        else:
            print("Invalid option.")
    else:
        print("File does not exist.") 