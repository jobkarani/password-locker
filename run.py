from user import User
from credentials import Credential

def create_user(username, password, email):
    '''
    function to create a new user.
    Args:
       username: New user username.
        password : New user password.
        email : New user email.
    '''
    new_user = User(username, password, email)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    User.save_user(user)

def delete_user(user):
    '''
    function to delete a user
    '''
    User.delete_user(user)

def find_user(username):
    '''
    method that takes in a name and returns a username that matches that name.
    '''
    return User.find_by_username(username)

def check_existing_user(email):
    '''
    method that checks if a user exists from the user list.
    '''
    return User.user_exists(email)

def create_user_info(social_media, profile, password):
    '''
    function to delete user credentials
    '''
    new_user_info = Credential(social_media, profile, password)
    return new_user_info

def save_user_info(info):
    '''
    function to save user info
    '''
    return Credential.save_credential(info)

def display_users_info(username):
    '''
    function to display user info
    '''
    return Credential.display_credential()


def display_all_users():
    '''
    function to display all users
    '''
    return User.display_users()

def generated_password():
    '''
    generates  a random password for users
    '''
    random_password = Credential.generate_password()
    return random_password



def main():
    print("Hey welcome to Password Locker.What is your name?")
    username = input()
    print(f"Hey {username}. what would you like to do :)")
    print("\n")

    while True:
        print("Use these short codes to choose an option:\n cn - Create an account \n ds - Display available users \n lg - Login to your account \n ex - Exit password locker")
        print("\n")

        option = input()

        if option == 'cn':
            print("~" * 15)
            print("Create an account")
            print("~" * 15)

            print("Enter your username")
            username = input()
            print("*" * 8)

            print("Enter your email")
            email = input()
            print("*" * 8)

            print("Enter your password")
            password = input()
            print("*" * 8)

            save_user(create_user(username, password, email))
            print("*" * 8)

            print(f"{username}, your account has been successfully created. You may proceed to login.")

        elif option == 'ds':
            if display_all_users():
                print("This is the list of users:")
                print("~" * 15)

                for user in display_all_users():
                    print(f"Username: {user.username}")
                    print(f"Email: {user.email}")

            else:
                print("\n")
                print("Ooooopps....You dont have any saved users yet!!!")
                print("\n")

        elif option == 'lg':
            print("~" * 15)
            print("Login")
            print("~" * 15)

            print("Enter your username")
            username = input()
            print("*" * 8)

            print("Enter your password")
            password = input()
            print("*" * 8)

            print("\n")

            authentification = check_existing_user(email)

            if authentification:
                print(f"Hey {email}, welcome back to password locker.")
                print("\n")

                while True:
                    print("*" * 15)
                    print("What would you like to do: \n 1 - Add information to your account \n 2 - Show your account details \n 3 - Terminate")
                    print("*" * 15)

                    option = int(input())

                    if option == 1:
                        print("~" * 15)
                        print("Add information to your account")
                        print("~" * 15)

                        print("*" * 8)
                        print("Enter the social media you want:")
                        social_media = input()

                        print("*" * 8)
                        print(f"What is your {social_media} account profile?")
                        profile = input()

                        while True:
                            print("*" * 15)
                            print("What would you like to do: \n 1 - Create your own password \n 2 - Use a randomly generated password \n 3 - Terminate")
                            print("*" * 15)
                            
                            option = int(input())

                            if option == 1:
                                print("~" * 8)
                                print("Enter a password of your choice")
                                password = input()
                                break

                            elif option == 2:
                                print("~" * 8)
                                password = generated_password()
                                break
                            
                            elif option == 3:
                                break

                            else:
                                print("~" * 8)
                                print("Ooops! Wrong input.Try again :)")
                                print("~" * 8)
                        
                        save_user_info(create_user_info(social_media, profile, password))
                        print(f"Hey {username}, your information has been updated succesfully. \n Username: {username} \n Password: {password}")
                        print("\n")

                    elif option == 2:
                        if display_users_info(username):
                            print("Enter a username")
                            print("~" * 8)

                            for new_user_info in display_users_info(username):
                                print(f"Social media:{new_user_info.social_media} \n Account: {new_user_info.profile} \n Password: {new_user_info.password}")
                        else:
                            print("No information for the given username")
                            
                    elif option == 3:
                        break

            else:
                print("Oooops....we can't find this user.You can try again")

        else:
            print("Bye :)")
            break

if __name__ == '__main__':
    main()