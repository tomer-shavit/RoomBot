from bot import RoomBot


def main():
    id_list = [209462589, 207377648, 209194976, 20895126, 207838277, 20848857,
               315858548, 208309575, 315315523, 316413715]
    my_email = ""  # add your email
    my_password = ""  # add your password
    rb = RoomBot(id_list, my_email, my_password)
    rb.choose_library()


if __name__ == "__main__":
    main()
