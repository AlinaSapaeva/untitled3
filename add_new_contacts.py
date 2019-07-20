# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import os
import unittest
from contact import Contact

from selenium.webdriver.support.select import Select


class add_new_contacts(unittest.TestCase):
    def setUp(self):
        self.wb = WebDriver()
        self.wb.implicitly_wait(60)

    def logout(self, wb):
        wb.find_element_by_link_text("Logout").click()

    def return_home_page(self, wb):
        wb.find_element_by_link_text("home").click()

    def add_new_contact(self, wb, contact):
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(contact.firstname)
        wb.find_element_by_name("middlename").click()
        wb.find_element_by_name("middlename").clear()
        wb.find_element_by_name("middlename").send_keys(contact.middlename)
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(contact.lastname)
        wb.find_element_by_name("nickname").click()
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys(contact.nickname)
        image=os.path.abspath('rr.jpg')

        wb.find_element_by_xpath("//input[@type='file']").clear()

        wb.find_element_by_xpath("//input[@type='file']").send_keys(image)


        wb.find_element_by_name("title").click()
        wb.find_element_by_name("title").clear()
        wb.find_element_by_name("title").send_keys(contact.title)
        wb.find_element_by_name("company").click()
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys(contact.company)
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(contact.address)
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys(contact.home)
        wb.find_element_by_name("mobile").click()
        wb.find_element_by_name("mobile").clear()
        wb.find_element_by_name("mobile").send_keys(contact.mobile )
        wb.find_element_by_name("work").click()
        wb.find_element_by_name("work").clear()
        wb.find_element_by_name("work").send_keys(contact.work)
        wb.find_element_by_name("fax").click()
        wb.find_element_by_name("fax").clear()
        wb.find_element_by_name("fax").send_keys(contact.fax)
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys(contact.email)
        wb.find_element_by_name("email2").click()
        wb.find_element_by_name("email2").clear()
        wb.find_element_by_name("email2").send_keys(contact.email2)
        wb.find_element_by_name("email3").click()
        wb.find_element_by_name("email3").clear()
        wb.find_element_by_name("email3").send_keys(contact.email3)
        wb.find_element_by_name("homepage").click()
        wb.find_element_by_name("homepage").clear()
        wb.find_element_by_name("homepage").send_keys(contact.homepage)
        wb.find_element_by_name("bday").click()
        Select(wb.find_element_by_name("bday")).select_by_visible_text(contact.bday)

        wb.find_element_by_name("bmonth").click()
        Select(wb.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)

        wb.find_element_by_name("byear").click()
        wb.find_element_by_name("byear").clear()
        wb.find_element_by_name("byear").send_keys(contact.byear)
        wb.find_element_by_name("aday").click()
        Select(wb.find_element_by_name("aday")).select_by_visible_text(contact.aday)

        wb.find_element_by_name("amonth").click()
        Select(wb.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)

        wb.find_element_by_name("ayear").click()
        wb.find_element_by_name("ayear").clear()
        wb.find_element_by_name("ayear").send_keys(contact.ayear)
        wb.find_element_by_name("address2").click()
        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys(contact.address2)

       #wb.find_element_by_name("new_group").click()
       #wb.find_element_by_name("theform").click()
        wb.find_element_by_name("phone2").click()
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys(contact.phone2)
        wb.find_element_by_name("notes").click()
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys(contact.notes)
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_create_contacts_page(self, wb):
        wb.find_element_by_link_text("add new").click()

    def login(self,  wb, username, password):
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(username)
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password )
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wb):
        wb.get("http://localhost/addressbook/")

    
    def test_add_new_contact(self):
        wb = self.wb
        self.open_home_page(wb)
        self.login(wb, username="admin", password="secret")
        self.open_create_contacts_page(wb)
        self.add_new_contact(wb,Contact(firstname="Alina", middlename="Maratovna",lastname="Sapaeva", nickname="hhh",title="gsdhfg",
company="ggygg", address="gyfhg", home="frrg", mobile="9030620645",  work="gfgdghyfyu", fax="ggfgf", email="gyfgf",   email2="gdtr",
email3="nbjhg", homepage="ggfdghb",bday="12", bmonth="March", byear="1994", aday="17", amonth="May", ayear="2000", address2="gffgjf",
phone2 ="fygfsdf",  notes="hgk")  )
        self.return_home_page(wb)
        self.logout(wb)

    def test_add_empty_contact(self):
        wb = self.wb
        self.open_home_page(wb)
        self.login(wb, username="admin", password="secret")
        self.open_create_contacts_page(wb)
        self.add_new_contact(wb,Contact(firstname="", middlename="",lastname="", nickname="",title="",
company="", address="", home="", mobile="",  work="", fax="", email="",   email2="",
email3="", homepage="",bday="-", bmonth="-", byear="-", aday="-", amonth="-", ayear="-", address2="",
phone2 ="",  notes="")  )
        self.return_home_page(wb)
        self.logout(wb)

    def tearDown(self):
        self.wb.quit()


if __name__ == "__main__":
    unittest.main()
