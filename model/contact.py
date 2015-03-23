__author__ = 'VinnieJohns'


class Contact:
    def __init__(self, fname=None, midname=None, lname=None, nickname=None, title=None, company=None, address=None,
                 home_tel=None, mobile_tel=None, work_tel=None, fax=None, email=None, email_2=None, email_3=None,
                 homepage=None, birth_date_day=None, birth_date_month=None, birth_date_year=None,
                 anniversary_date_day=None, anniversary_date_month=None, anniversary_date_year=None,
                 secondary_address=None, secondary_home_phone=None, notes=None):
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