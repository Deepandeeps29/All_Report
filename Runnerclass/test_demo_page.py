import pytest
from Resources.test_Register_Page import RegisterPage
from Resources.Login import SignupPage
from Resources.Button_Page import Button_Page
# from Resources.CheckBox_Page import Check_Page
# from Resources.Radio_Button import RadioButton
import time

@pytest.mark.usefixtures("driver_init")
class TestDemo:
    def test_register_page(self):
        page = RegisterPage(self.driver)
        page.load()
        page.UI()
        page.Register_Page()
        time.sleep(2)

    # def test_signup_page(self):
        page = SignupPage(self.driver)
        page.Signup_Page()
        time.sleep(2)

    # def test_button_page(self):
        page = Button_Page(self.driver)
        page.click_buttons()
        time.sleep(2)

    # def test_checkbox_page(self):
        page = Check_Page(self.driver)
        page.Check_Box()
        time.sleep(2)

    # def test_radio_page(self):
        page = RadioButton(self.driver)
        page.Radio_Button()
        time.sleep(2)
