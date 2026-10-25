import re
from playwright.sync_api import Page, expect
from pages.manager_order_page import ManagerOrderPage

def test_manager_order_by_code_in_all_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_all_order()
    manager_order_page.click_search_order("6566667544")
    manager_order_page.click_search_order_btn()   
    
    expect(manager_order_page.order_cards.first).to_be_visible()

def test_manager_order_by_code_no_exits_in_all_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_all_order()
    manager_order_page.click_search_order("248653452875")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_in_all_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_all_order()
    manager_order_page.click_search_order("tiki trading")
    manager_order_page.click_search_order_btn() 
    
    expect(manager_order_page.order_cards.first).to_be_visible()
    expect(manager_order_page.seller_names.first).to_contain_text("tiki trading", ignore_case=True)
    
def test_manager_order_by_seller_name_no_exits_in_all_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_all_order()
    manager_order_page.click_search_order("casrlan")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_in_all_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_all_order()
    manager_order_page.click_search_order("nước mắm")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.order_cards.first).to_be_visible()
    expect(manager_order_page.product_names.first).to_contain_text("nước mắm", ignore_case=True)
    
def test_manager_order_by_product_name_no_exits_in_all_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_all_order()
    manager_order_page.click_search_order("phấn phủ")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_in_wait_payment(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_wait_by_order()
    manager_order_page.click_search_order("6566667544")
    manager_order_page.click_search_order_btn()   
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_no_exits_in_wait_payment(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_wait_by_order()
    manager_order_page.click_search_order("248653452875")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_in_wait_payment(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_wait_by_order()
    manager_order_page.click_search_order("tiki trading")
    manager_order_page.click_search_order_btn() 
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_no_exits_in_wait_payment(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_wait_by_order()
    manager_order_page.click_search_order("casrlan")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_in_wait_payment(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_wait_by_order()
    manager_order_page.click_search_order("nước mắm")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_no_exits_in_wait_payment(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_wait_by_order()
    manager_order_page.click_search_order("phấn phủ")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_in_processing_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_processing_order()
    manager_order_page.click_search_order("6566667544")
    manager_order_page.click_search_order_btn()   
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_no_exits_in_processing_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_processing_order()
    manager_order_page.click_search_order("248653452875")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_in_processing_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_processing_order()
    manager_order_page.click_search_order("tiki trading")
    manager_order_page.click_search_order_btn() 
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_no_exits_in_processing_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_processing_order()
    manager_order_page.click_search_order("casrlan")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_in_processing_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_processing_order()
    manager_order_page.click_search_order("nước mắm")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_no_exits_in_processing_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_processing_order()
    manager_order_page.click_search_order("phấn phủ")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()

def test_manager_order_by_code_in_transport_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_transport_order()
    manager_order_page.click_search_order("6566667544")
    manager_order_page.click_search_order_btn()   
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_no_exits_in_transport_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_transport_order()
    manager_order_page.click_search_order("248653452875")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_in_transport_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_transport_order()
    manager_order_page.click_search_order("tiki trading")
    manager_order_page.click_search_order_btn() 
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_no_exits_in_transport_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_transport_order()
    manager_order_page.click_search_order("casrlan")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_in_transport_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_transport_order()
    manager_order_page.click_search_order("nước mắm")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_no_exits_in_transport_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_transport_order()
    manager_order_page.click_search_order("phấn phủ")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_in_delivered_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_delivered_order()
    manager_order_page.click_search_order("6566667544")
    manager_order_page.click_search_order_btn()   
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_no_exits_in_delivered_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_delivered_order()
    manager_order_page.click_search_order("248653452875")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_in_delivered_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_delivered_order()
    manager_order_page.click_search_order("tiki trading")
    manager_order_page.click_search_order_btn() 
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_no_exits_in_delivered_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_delivered_order()
    manager_order_page.click_search_order("casrlan")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_in_delivered_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_delivered_order()
    manager_order_page.click_search_order("nước mắm")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_no_exits_in_delivered_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_delivered_order()
    manager_order_page.click_search_order("phấn phủ")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_code_in_cancel_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_cancel_order()
    manager_order_page.click_search_order("6566667544")
    manager_order_page.click_search_order_btn()   
    
    expect(manager_order_page.order_cards.first).to_be_visible()

def test_manager_order_by_code_no_exits_in_cancel_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_cancel_order()
    manager_order_page.click_search_order("248653452875")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_seller_name_in_cancel_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_cancel_order()
    manager_order_page.click_search_order("tiki trading")
    manager_order_page.click_search_order_btn() 
    
    expect(manager_order_page.order_cards.first).to_be_visible()
    expect(manager_order_page.seller_names.first).to_contain_text("tiki trading", ignore_case=True)
    
def test_manager_order_by_seller_name_no_exits_in_cancel_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_cancel_order()
    manager_order_page.click_search_order("casrlan")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()
    
def test_manager_order_by_product_name_in_cancel_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_cancel_order()
    manager_order_page.click_search_order("nước mắm")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.order_cards.first).to_be_visible()
    expect(manager_order_page.product_names.first).to_contain_text("nước mắm", ignore_case=True)
    
def test_manager_order_by_product_name_no_exits_in_cancel_order(logged_in_page):
    manager_order_page = ManagerOrderPage(logged_in_page)
    
    manager_order_page.open_account_menu()
    manager_order_page.click_manager_order()
    manager_order_page.click_cancel_order()
    manager_order_page.click_search_order("phấn phủ")
    manager_order_page.click_search_order_btn()
    
    expect(manager_order_page.empty_message).to_be_visible()