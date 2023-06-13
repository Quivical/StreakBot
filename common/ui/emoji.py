def convert_num_to_emoji(number):

    num_emoji = {
        "0": ":zero:",
        "1": ":one:",
        "2": ":two:",
        "3": ":three:",
        "4": ":four:",
        "5": ":five:",
        "6": ":six:",
        "7": ":seven:",
        "8": ":eight:",
        "9": ":nine:"
    }

    numbers = str(number)
    string = ""
    for n in numbers:
        string += num_emoji[n]
    return string
