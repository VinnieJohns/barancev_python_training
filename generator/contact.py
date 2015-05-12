__author__ = 'VinnieJohns'
from model.contact import Contact
from fixture import support
import random
import string
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # ' sign and double-spaces are replaced to avoid known failures
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).replace("  ", " ")


testdata = [
    Contact(fname=random.choice(["", random_string("fname", 10)]),
            midname=random.choice(["", random_string("mname", 15)]),
            lname=random.choice(["", random_string("lname", 20)]),
            nickname=random.choice(["", random_string("nickname", 10)]),
            title=random.choice(["", random_string("title", 10)]),
            company=random.choice(["", random_string("company", 25)]),
            address=random.choice(["", random_string("address", 30)]),
            home_tel=random.choice(["", random_string("home_tel", 10)]),
            mobile_tel=random.choice(["", random_string("mobile_tel", 10)]),
            work_tel=random.choice(["", random_string("work_tel", 10)]),
            fax=random.choice(["", random_string("fax", 10)]),
            email_2=random.choice(["", random_string("email2", 5)]),
            email_3=random.choice(["", random_string("email3", 5)]),
            homepage=random.choice(["", random_string("homepage", 5)]),
            birth_date_day=random.randrange(0, 32),
            birth_date_month=random.choice(["-", random.choice(support.months_list)]),
            birth_date_year=random.choice(["", random.randrange(1898, 2015)]),
            anniversary_date_day=random.randrange(0, 32),
            anniversary_date_month=random.choice(["-", random.choice(support.months_list)]),
            anniversary_date_year=random.choice(["", random.randrange(1898, 2015)]),
            secondary_address=random.choice(["", random_string("secaddress", 30)]),
            secondary_home_phone=random.choice(["", random_string("phone2", 10)]),
            notes=random.choice(["", random_string("notes", 100)]))
    for i in range(n)
    ] + [Contact(fname="", lname="")]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))