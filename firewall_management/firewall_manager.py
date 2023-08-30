import subprocess

# Function to add a rule


def add_rule(rule):
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp',
                    '--dport', str(rule['port']), '-j', 'DROP'])

# Function to remove a rule


def remove_rule(rule):
    subprocess.call(['iptables', '-D', 'INPUT', '-p', 'tcp',
                    '--dport', str(rule['port']), '-j', 'DROP'])

# Function to list all rules


def list_rules():
    subprocess.call(['iptables', '-L'])


if __name__ == "__main__":
    while True:
        print("1. Add Rule")
        print("2. Remove Rule")
        print("3. List Rules")
        print("4. Exit")
        print("="*40)
        choice = input("Enter your choice: ")

        if choice == '1':
            port = int(input("Enter the port to block: "))
            rule = {'port': port}
            add_rule(rule)
            print(f"Rule added to block port {port}")
        elif choice == '2':
            port = int(input("Enter the port to unblock: "))
            rule = {'port': port}
            remove_rule(rule)
            print(f"Rule removed to unblock port {port}")
        elif choice == '3':
            list_rules()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
