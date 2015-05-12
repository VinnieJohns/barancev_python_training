__author__ = 'VinnieJohns'
import random
import string


def random_string(prefix, maxlen):
    # ' sign and double-spaces are replaced to avoid known failures
    symbols = string.ascii_letters + string.digits + string.punctuation.replace("'", "") + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).replace("  ", " ")

months_list = ["January", "February", "March",
               "April", "May", "June",
               "July", "August", "September",
               "October", "November", "December"]
