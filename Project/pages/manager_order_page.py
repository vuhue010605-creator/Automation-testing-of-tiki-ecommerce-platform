
import re
from playwright.sync_api import Page, expect

class ManagerOrderPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_account_btn = page.locator('[data-view-id="header_header_account_container"]')
        self.manager_order_link = page.get_by_role("link", name="Đơn hàng của tôi") 
        self.search_order_by_code_input = page.get_by_role("searchbox", name="Tìm đơn hàng theo Mã đơn hàng") 
        self.waiting_for_payment_click = page.get_by_text("Chờ thanh toán") 
        self.processing_order_click = page.get_by_text("Đang xử lý")
        self.transport_order_click = page.get_by_text("Đang vận chuyển")
        self.delivered_order_click = page.get_by_text("Đã giao")
        self.cancel_order_click = page.get_by_text("Đã huỷ")
        self.all_order_click = page.get_by_text("Tất cả đơn")
        self.order_cards = page.locator(".infinite-scroll-component > div")
        self.product_names = page.locator(".product-name")
        self.seller_names = page.locator(".store span")
        self.empty_message = page.get_by_text("Chưa có đơn hàng")
        self.search_order_btn = page.get_by_text("Tìm đơn hàng")


    def click_search_order_btn(self):
        self.search_order_btn.click()
            
    def open_account_menu(self):
        self.header_account_btn.click()
        
    def click_manager_order(self):
        self.manager_order_link.click()
        
    def click_all_order(self):
        self.all_order_click.click()
    def click_search_order(self, order: str):
        self.search_order_by_code_input.click()
        self.search_order_by_code_input.fill(order)
        
    def click_wait_by_order(self):
        self.waiting_for_payment_click.click()
        
    def click_processing_order(self):
        self.processing_order_click.click()
        
    def click_transport_order(self):
        self.transport_order_click.click()
        
    def click_delivered_order(self):
        self.delivered_order_click.click()
        
    def click_cancel_order(self):
        self.cancel_order_click.click()
        
      