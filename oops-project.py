class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
        
    def menu(self):
        user_input = input("""Welcome to chatbook ! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to login
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit\n""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
            
            
    def signup(self):
        email = input("enter your email: ")
        pwd = input("enter your password: ")
        self.username = email
        self.password = pwd
        print("Sign up successful !!")
        print("\n")
        self.menu()
        
    def login(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu.")
        else:
            uname = input("enter your email/username: ")
            pwd = input("enter your password: ")
            if self.username == uname and self.password == pwd:
                print("Login successful !!")
                self.logged = True
            else:
                print("invalid username or password !!")
        print("\n")
        self.menu()

            
obj = chatbook()
