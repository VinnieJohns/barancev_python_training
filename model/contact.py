__author__ = 'VinnieJohns'


class Contact:
    def __init__(self, fname, midname, lname, nickname, title, company, address, home_tel, mobile_tel, work_tel,
                 fax, email, email_2, email_3, homepage, birth_date_day, birth_date_month, birth_date_year,
                 anniversary_date_day, anniversary_date_month, anniversary_date_year, secondary_address,
                 secondary_home_phone, notes):
        self.fname = fname
        self.midname = midname
        self.lname = lname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birth_date_day = birth_date_day
        self.birth_date_month = birth_date_month
        self.birth_date_year = birth_date_year
        self.anniversary_date_day = anniversary_date_day
        self.anniversary_date_month = anniversary_date_month
        self.anniversary_date_year = anniversary_date_year
        self.secondary_address = secondary_address
        self.secondary_home_phone = secondary_home_phone
        self.notes = notes