9import socket


# Port Scanner

def port_scanner(target, start_port, end_port):
    print(f"\nScanning ports on {target}...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        sock.close()


# Brute Force Simulator

def brute_force_simulator(password_list, correct_password):
    print("\nStarting brute force simulation...")

    for password in password_list:
        print(f"Trying password: {password}")

        if password == correct_password:
            print(f"Password found: {password}")
            return

    print("Password not found.")


if __name__ == '__main__':
    print("Penetration Testing Toolkit")

    choice = input("1. Port Scanner\n2. Brute Force Simulator\nChoose option: ")

    if choice == '1':
        target = input("Enter target IP/domain: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        port_scanner(target, start_port, end_port)

    elif choice == '2':
        passwords = ['admin', '123456', 'password', 'root123']
        correct_password = 'root123'

        brute_force_simulator(passwords, correct_password)

    else:
        print("Invalid option.")