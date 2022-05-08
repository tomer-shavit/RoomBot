from bot import RoomBot
from datetime import date


def main():
    id_list = ["209462589", "207377648", "209194976", "20895126", "207838277",
               "20848857", "315858548", "208309575", "315315523", "316413715",
               "318911088", "318323540"]
    my_email = input("Enter your email address: \n")  # add your email
    my_password = input("Enter your password: \n")  # add your password

    # Obtaining desired date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    day = int(d1[0:2]) + 6

    # Creating and running the bot
    rb = RoomBot(id_list, my_email, my_password, day)
    rb.run()


if __name__ == "__main__":
    main()
