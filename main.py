from bot import RoomBot


def main():
    id_list = ["209462589", "207377648", "209194976", "20895126", "207838277",
               "20848857", "315858548", "208309575", "315315523", "316413715"]
    my_email = input("Enter your email address: \n")  # add your email
    my_password = input("Enter your password: \n")  # add your password
    rb = RoomBot(id_list, my_email, my_password, 12)
    rb.run()


if __name__ == "__main__":
    main()
