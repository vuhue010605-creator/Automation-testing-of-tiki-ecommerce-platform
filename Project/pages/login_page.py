from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.close_banner_btn = page.get_by_role("img", name="close-icon")
        self.account_btn = page.get_by_text("Tài khoản")
        self.phone_input = page.get_by_role("textbox", name="Số điện thoại")
        self.agree_terms_checkbox = page.locator("label.agree-terms .checkbox-fake")
        self.continue_btn = page.get_by_role("button", name="Tiếp Tục")
        self.password_input = page.get_by_role("textbox", name="Mật khẩu")
        self.login_btn = page.get_by_role("button", name="Đăng Nhập")
        self.error_message = page.locator(".error-mess, span.error, p.error, div[role='alert']")

    def navigate(self):
        self.page.goto("https://tiki.vn/", wait_until="domcontentloaded", timeout=60000)
        
        # Xử lý banner quảng cáo nếu có
        try:
            if self.close_banner_btn.is_visible(timeout=2000):
                self.close_banner_btn.click()
        except Exception:
            pass

        self.account_btn.click()
        self.phone_input.wait_for(state="visible", timeout=10000)

    def fill_phone_and_continue(self, phone: str):
        self.phone_input.clear()
        if phone:
            self.phone_input.fill(phone)
            
        try:
            if self.agree_terms_checkbox.is_visible(timeout=1000) and not self.agree_terms_checkbox.is_checked():
                self.agree_terms_checkbox.click()
        except Exception:
            pass

        if self.continue_btn.is_enabled():
            self.continue_btn.click(timeout=5000, force=True)

    def login_with_password(self, phone: str, password: str):
        self.fill_phone_and_continue(phone)
        
        try:
            self.password_input.wait_for(state="visible", timeout=5000)
            self.password_input.fill(password)
            if self.login_btn.is_enabled():
                self.login_btn.click(force=True)
        except Exception:
            pass
        

        
