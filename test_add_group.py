# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group

import unittest, time

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wb = WebDriver()
        self.wb.implicitly_wait(60)


    def logout(self, wb):
        wb.find_element_by_link_text("Logout").click()

    def create_group(self, wb, group):
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
        wb.find_element_by_link_text("group page").click()


    def login(self, wb, username, password):
        wb.get("http://localhost/addressbook/")
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(username)
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()


    def test_add_group(self):
        wb = self.wb
        self.login(wb, username="admin", password="secret")
        self.create_group(wb, Group(name="test", header="test11", footer="test22"))
        self.logout(wb)

    def test_add_empty_group(self):
        wb = self.wb
        self.login(wb, username="admin", password="secret")
        self.create_group(wb, Group(name="", header="", footer=""))
        self.logout(wb)

    def tearDown(self):
        self.wb.quit()


if __name__ == "__main__":
    unittest.main()
