import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_success(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login_with_password("0375956110", "Vuhue162005")


def test_login_full_space_phone(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.fill_phone_and_continue("")
    
    expect(login_page.error_message).to_have_text("Số điện thoại không được để trống")
    
def test_login_special_characters_phone(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.fill_phone_and_continue("@#$%&*123.")
    expect(login_page.error_message).to_have_text("Số điện thoại không được để trống")
    
def test_login_format_phone(page:Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.fill_phone_and_continue("01234567")
    expect(login_page.error_message).to_have_text("Số điện thoại không đúng định dạng.")    

def test_login_wrong_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login_with_password("0375956110", "Vuhue16200")
    expect(login_page.error_message).to_have_text("Thông tin đăng nhập không đúng")    
    
def test_login_empty_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login_with_password("0375956110", "")
    expect(login_page.error_message).to_have_text("Mật khẩu không được để trống")
    
    
    

    
    
