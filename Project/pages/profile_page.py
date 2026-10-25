import re
from playwright.sync_api import Page, expect


class ProfilePage:
    def __init__(self, page: Page):
        self.page = page  # Sửa lỗi gán self.page = Page

        # Locators (Đặt tên theo quy chuẩn: thành phần + loại element)
        self.header_account_btn = page.locator(
            '[data-view-id="header_header_account_container"]'
        )
        self.account_info_link = page.get_by_role("link", name="Thông tin tài khoản")
        self.full_name_input = page.get_by_role(
            "searchbox", name="Thêm họ tên"
        )  # Sửa searchbox thành textbox
        self.nickname_input = page.get_by_role("searchbox", name="Thêm nickname")
        self.save_btn = page.get_by_role("button", name="Lưu thay đổi")
        self.edit_avatar_btn = page.locator(".avatar-view .edit")
        self.update_picture_menu_item = page.locator(
            ".menu-item", has_text="Cập nhật ảnh đại diện"
        )

        # Sửa lỗi get_by_role với chuỗi text dài (dùng get_by_text thay thế)
        self.choose_image_area = page.get_by_text(
            "Nhấn để chọn hoặc kéo thả hình ảnh vào khung này."
        )
        self.file_input = page.locator('input[type="file"]')

        # Dropdown ngày tháng năm sinh
        self.day_select = page.locator("select[name='day']")
        self.month_select = page.locator("select[name='month']")
        self.year_select = page.locator("select[name='year']")

        self.country_select = page.locator('input[name=nationality]')
        
        self.error_message = page.locator("div.message.error")
        self.success_message = page.locator('div[type="success"]')
        

    # Actions / Methods
    
    def open_account_menu(self):
        self.header_account_btn.click()

    def click_account_info(self):
        self.account_info_link.click()

    def fill_full_name(self, name: str):
        self.full_name_input.click()
        self.full_name_input.fill(name)

    def fill_nickname(self, nickname: str):
        self.nickname_input.click()
        self.nickname_input.fill(nickname)

    def save_changes(self):
        self.save_btn.click()

    def click_edit_avatar(self):
        self.edit_avatar_btn.click()

    def select_update_picture(self):
        self.update_picture_menu_item.click()

    def click_choose_image(self):
        self.choose_image_area.click()

    def upload_avatar(self, file_path: str):
        # Cho phép truyền đường dẫn linh hoạt thay vì fix cứng trong code
        self.file_input.set_input_files(file_path)

    def select_gender(self, gender_text):
        self.page.locator("label").filter(has_text=gender_text).click()

    def select_country(self, country_name):
        self.country_select.click()
        self.page.locator("div.item").filter(has_text=country_name).click()

    def select_day(self, day: str):
        self.day_select.select_option(day)

    def select_month(self, month: str):
        self.month_select.select_option(month)

    def select_year(self, year: str):
        self.year_select.select_option(year)
