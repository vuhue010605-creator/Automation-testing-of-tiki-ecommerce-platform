import re
from playwright.sync_api import Page, expect


class AddrressBookPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_account_btn = page.locator(
            '[data-view-id="header_header_account_container"]'
        )
        self.account_info_link = page.get_by_role("link", name="Thông tin tài khoản")
        self.address_book_link = page.get_by_role("link", name="Sổ địa chỉ")
        self.new_address_link = page.get_by_role("link", name="Thêm địa chỉ mới")
        self.add_name_input = page.get_by_role("textbox", name="Nhập họ và tên")
        self.add_company_input = page.get_by_role("textbox", name="Nhập công ty")
        self.add_phone_input = page.get_by_role("textbox", name="Nhập số điện thoại")
        self.add_address_input = page.get_by_role("textbox", name="Nhập địa chỉ")

        self.province_select = page.get_by_role("combobox").first
        self.district_select = page.get_by_role("combobox").nth(1)
        self.commune_select = page.get_by_role("combobox").nth(2)

        self.update_button = page.get_by_role("button", name="Cập nhật")
        self.delete_button = page.get_by_role("button", name="Xóa")
        self.edit_link = page.get_by_role("link", name="Chỉnh sửa")

        self.home_radio = page.locator("label").filter(has_text="Nhà riêng / Chung cư")
        self.office_radio = page.locator("label").filter(has_text="Cơ quan / Công ty")
        self.default_checkbox = page.locator("label").filter(has_text="Đặt làm địa chỉ mặc định")

        self.error_message = page.locator(".error-message")
        self.address_items = page.locator(".inner .item")

    def open_account_menu(self):
        self.header_account_btn.click()

    def click_account_info(self):
        self.account_info_link.click()

    def click_address_book(self):
        self.address_book_link.click()

    def click_new_address(self):
        self.new_address_link.click()

    def click_add_name(self, name: str):
        self.add_name_input.click()
        self.add_name_input.fill(name)

    def click_add_company(self, company: str):
        self.add_company_input.click()
        self.add_company_input.fill(company)

    def click_add_phone(self, phone: str):
        self.add_phone_input.click()
        self.add_phone_input.fill(phone)

    def click_add_address(self, address: str):
        self.add_address_input.click()
        self.add_address_input.fill(address)

    def click_select_province(self, province: str):
        self.province_select.click()
        self.province_select.select_option(province)

    def click_select_district(self, district: str):
        self.district_select.click()
        self.district_select.select_option(district)

    def click_commune_select(self, city: str):
        self.commune_select.click()
        self.commune_select.select_option(city)

    def click_update_btn(self):
        self.update_button.click()

    def click_delete_btn(self):
        self.delete_button.click()

    def click_edit_address(self):
        self.edit_link.click()

    def click_home_apartment(self):
        self.home_radio.click()

    def click_agency_company(self):
        self.office_radio.click()

    def click_default_address(self):
        self.default_checkbox.click()

    def get_validation_message(self, locator) -> str:
        return locator.evaluate("element => element.validationMessage")

    def get_card_default_label_locator(self, card_locator):
        return card_locator.get_by_text("Địa chỉ mặc định")