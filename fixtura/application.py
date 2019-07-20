from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from fixtura.session import SessionHelper
import os


class Application:
    def __init__(self):
        self.wb = WebDriver()
        self.wb.implicitly_wait(60)
        self.session=SessionHelper(self)

    def open_home_page(self):
        wb = self.wb
        wb.get("http://localhost/addressbook/")

    def return_home_page(self):
        wb = self.wb
        wb.find_element_by_link_text("home").click()

    def return_to_groups_page(self):
        wb = self.wb
        wb.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wb = self.wb
        self.open_groups_page()
        wb.find_element_by_link_text("groups").click()
        # init group creations
        wb.find_element_by_name("new").click()
        # fill group form
        wb.find_element_by_name("group_name").click()
        wb.find_element_by_name("group_name").clear()
        wb.find_element_by_name("group_name").send_keys(group.name)
        wb.find_element_by_name("group_header").click()
        wb.find_element_by_name("group_header").clear()
        wb.find_element_by_name("group_header").send_keys(group.header)
        wb.find_element_by_name("group_footer").click()
        wb.find_element_by_name("group_footer").clear()
        wb.find_element_by_name("group_footer").send_keys(group.footer)
        #submit group creation
        wb.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wb = self.wb
        wb.find_element_by_link_text("groups").click()



    def add_new_contact(self, contact):
        wb = self.wb
        self.open_create_contacts_page()
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
        image = os.path.abspath('rr.jpg')

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
        wb.find_element_by_name("mobile").send_keys(contact.mobile)
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

        # wb.find_element_by_name("new_group").click()
        # wb.find_element_by_name("theform").click()
        wb.find_element_by_name("phone2").click()
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys(contact.phone2)
        wb.find_element_by_name("notes").click()
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys(contact.notes)
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def open_create_contacts_page(self):
        wb = self.wb
        wb.find_element_by_link_text("add new").click()

    def destroy(self):
        wb = self.wb
        self.wb.quit()


