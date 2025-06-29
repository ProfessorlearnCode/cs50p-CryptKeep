from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dictionary = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as encrypted_file:
            encrypted_file.write(self.key)

    def loading_key(self, path):
        with open(path, 'rb') as decrypted_file:
            self.key = decrypted_file.read()

    def create_password_file(self, path, init_value= None):
        self.password_file = path

        if init_value is not None:
            for key, value in init_value.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path ,'r') as f:
            for line in f:
              site, encrypted = line.split(":", 1)
              self.password_dictionary[site]= Fernet(self.key).decrypt(encrypted.encode()).decode()


    def add_password(self, site, password):
        self.password_dictionary[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")


    def get_password(self,site):
        return self.password_dictionary[site]


def main():
    password = {
        "email" : "1234567",
        "Facebook" : "Meta1234",
        "Youtube" : "CS50_",
        "Instagram" : "Professor"

    }

    pm = PasswordManager()

    print(""" What do you want to do?
        1. Create a new key
        2. Load an existing key
        3. Create a new password
        4. Load existing password
        5. Add a new password
        6. Get a password
        q. Quit
        """)
    done = False
    while not done:
        choice = input("Enter choice: ")
        match choice:
            case "1":
                path = input("Enter Path: ")
                pm.create_key(path)

            case "2":
                path = input("Enter Path: ")
                pm.loading_key(path)

            case "3":
                path = input("Enter Path: ")
                pm.create_password_file(path, password)

            case "4":
                path = input("Enter Path: ")
                pm.load_password_file(path)

            case "5":
                site = input("Enter Site: ")
                password = input("Enter Password: ")
                pm.add_password(site, password)

            case "6":
                site = input("Site: ")
                print(f"Site: {site}\nPassword: {pm.get_password(site)}")

            case "q":
                done = True
                print("Bye")

            case _:
                print("Invalid Choice")



if __name__ == "__main__":
    main()
