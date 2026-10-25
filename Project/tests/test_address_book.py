import re
import pytest
from playwright.sync_api import Page, expect
from pages.address_book_page import AddrressBookPage


def test_address_create_success(logged_in_page):
    address_book_page = AddrressBookPage(logged_in_page)

    test_name = ""
    test_phone = ""
    test_address = ""
    
    new_address_card = address_book_page.address_items.filter(has_text=test_name).filter(has_text=test_phone).filter(has_text=test_address).first
    
    expect(new_address_card).to_be_visible()
    
    expect(new_address_card.locator(".name")).to_contain_text(test_name)
    expect(new_address_card.locator(".phone")).to_contain_text(test_phone)
    expect(new_address_card.locator(".address")).to_contain_text(test_address)

@pytest.mark.parametrize("name_input, test_case", [
    ("test", "invalid_word"),
    ("hue", "short_char"),
    ("vu hue@#$%", "special_char"),
    ("", "empty_name"),
    ("   ", "space_name")
])
def test_address_book_invalid_name(logged_in_page, name_input, test_case):
    address_book_page = AddrressBookPage(logged_in_page)
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_phone("0375956110")
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address("thoại ngọc hầu")
    address_book_page.click_add_name(name_input)
    address_book_page.click_update_btn()
    
    if test_case == "invalid_word":
        expect(address_book_page.error_message).to_have_text("Họ tên có chứa từ không phù hợp")
    elif test_case == "short_char":
        expect(address_book_page.error_message).to_have_text("Họ & Tên gồm 2 từ trở lên")
    elif test_case == "special_char":
        expect(address_book_page.error_message).to_have_text("Họ tên không bao gồm kí tự đặc biệt và số")
    elif test_case == "empty_name":
        expect(address_book_page.add_name_input).to_have_js_property("validationMessage", "Please fill out this field.")
    elif test_case == "space_name":
        expect(address_book_page.error_message).to_have_text("Vui lòng nhập họ tên")
    
@pytest.mark.parametrize("company_input , name_input", [
    ("", "gia bảo"),
    ("Công ty TNHH sữa@#$%^.123", "kem cốm"),
    ("hue", "hue vu"),
    ("vu hue vu hue vu hue vu hue vu hue vu hue vu hue vu", "cốm cốm")
])
def test_address_book_company_name(logged_in_page, company_input, name_input):
    address_book_page = AddrressBookPage(logged_in_page)
    
    test_name = name_input
    test_phone = "0375956110"
    test_address = "thoại ngọc hầu"
        
    
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_name(name_input)
    address_book_page.click_add_phone(test_phone)
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address(test_address)
    address_book_page.click_add_company(company_input)
    address_book_page.click_update_btn()
    
    new_address_card = address_book_page.address_items.filter(has_text=test_name).filter(has_text=test_phone).filter(has_text=test_address).first
    
    
    expect(new_address_card).to_be_visible()
        
    expect(new_address_card.locator(".name")).to_contain_text(test_name)
    expect(new_address_card.locator(".phone")).to_contain_text(test_phone)
    expect(new_address_card.locator(".address")).to_contain_text(test_address)
    
@pytest.mark.parametrize("phone_input, test_case", [
    ("", "empty_phone"),
    ("   ", "space_full"),
    ("hue123@#$", "special_char"),
    ("037595611", "short_num"),
    ("03759561100", "long_num")
])
def test_address_book_phone_input(logged_in_page, phone_input, test_case):
    address_book_page = AddrressBookPage(logged_in_page)
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_phone(phone_input)
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address("thoại ngọc hầu")
    address_book_page.click_add_name("mèo nhỏ")
    address_book_page.click_update_btn()
    
    if test_case == "empty_phone":
        expect(address_book_page.add_phone_input).to_have_js_property("validationMessage", "Please fill out this field.")
    elif test_case == "space_full":
        expect(address_book_page.error_message).to_have_text("Vui lòng nhập số điện thoại")
    elif test_case == "special_char":
        expect(address_book_page.error_message).to_have_text("Số điện thoại không đúng định dạng")
    elif test_case == "short_num":
        expect(address_book_page.error_message).to_have_text("Số điện thoại không đúng định dạng")
    elif test_case == "long_num":
        expect(address_book_page.error_message).to_have_text("Số điện thoại không đúng định dạng")
        
def test_address_book_invalid_province(logged_in_page, ):
    address_book_page = AddrressBookPage(logged_in_page)
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_phone("0375956110")
    address_book_page.click_select_province("")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address("thoại ngọc hầu")
    address_book_page.click_add_name("mèo nhỏ")
    address_book_page.click_update_btn()
    
    expect(address_book_page.province_select).to_have_js_property("validationMessage", "Please select an item in the list.")
    
def test_address_book_invalid_district(logged_in_page, ):
    address_book_page = AddrressBookPage(logged_in_page)
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_phone("0375956110")
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address("thoại ngọc hầu")
    address_book_page.click_add_name("mèo nhỏ")
    address_book_page.click_update_btn()
    
    expect(address_book_page.district_select).to_have_js_property("validationMessage", "Please select an item in the list.")
    
def test_address_book_invalid_commune(logged_in_page, ):
    address_book_page = AddrressBookPage(logged_in_page)
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_phone("0375956110")
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("")
    address_book_page.click_add_address("thoại ngọc hầu")
    address_book_page.click_add_name("mèo nhỏ")
    address_book_page.click_update_btn()
    
    expect(address_book_page.commune_select).to_have_js_property("validationMessage", "Please select an item in the list.")
    
@pytest.mark.parametrize("address_input, test_case", [
    ("", "empty_address"),
    ("@#$%", "special_char"),
    ("hi", "short_char")
])
def test_address_book_address_input(logged_in_page, address_input, test_case):
    address_book_page = AddrressBookPage(logged_in_page)
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_phone("0375956110")
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address(address_input)
    address_book_page.click_add_name("mèo nhỏ")
    address_book_page.click_update_btn()
    
    if test_case == "empty_address":
        expect(address_book_page.add_address_input).to_have_js_property("validationMessage", "Please fill out this field.")
    elif test_case == "short_char":
        expect(address_book_page.error_message).to_have_text("Địa chỉ giao hàng không hợp lệ (Địa chỉ phải chứa ít nhất 2 từ)")
    elif test_case == "special_char":
        expect(address_book_page.error_message).to_have_text("Địa chỉ giao hàng không hợp lệ (Địa chỉ không nên chứa các kí tự đặc biệt)")
    
def test_address_book_home_apartment(logged_in_page):
    address_book_page = AddrressBookPage(logged_in_page)
    
    test_name = "mèo nhỏ"
    test_phone = "0375956110"
    test_address = "luỹ bán bích"
    
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_name(test_name)
    address_book_page.click_add_phone(test_phone)
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address(test_address)
    address_book_page.click_home_apartment()
    address_book_page.click_update_btn()
    
    new_address_card = address_book_page.address_items.filter(has_text=test_name).filter(has_text=test_phone).filter(has_text=test_address).first
    
    expect(new_address_card).to_be_visible()
    
    
    expect(new_address_card.locator(".name")).to_contain_text(test_name)
    expect(new_address_card.locator(".phone")).to_contain_text(test_phone)
    expect(new_address_card.locator(".address")).to_contain_text(test_address)
    
def test_address_book_agency_company(logged_in_page):
    address_book_page = AddrressBookPage(logged_in_page)
    
    test_name = "mèo lớn"
    test_phone = "0375956110"
    test_address = "luỹ bán bích"
    
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_name(test_name)
    address_book_page.click_add_phone(test_phone)
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address(test_address)
    address_book_page.click_agency_company()
    address_book_page.click_update_btn()
    
    new_address_card = address_book_page.address_items.filter(has_text=test_name).filter(has_text=test_phone).filter(has_text=test_address).first
    
    expect(new_address_card).to_be_visible()
    
    
    expect(new_address_card.locator(".name")).to_contain_text(test_name)
    expect(new_address_card.locator(".phone")).to_contain_text(test_phone)
    expect(new_address_card.locator(".address")).to_contain_text(test_address)
    
def test_address_book_default_address(logged_in_page):
    address_book_page = AddrressBookPage(logged_in_page)
    
    test_name = "mèo lớn"
    test_phone = "0375956110"
    test_address = "luỹ bán bích"
    
    address_book_page.open_account_menu()
    address_book_page.click_account_info()
    address_book_page.click_address_book()
    address_book_page.click_new_address()
    address_book_page.click_add_name(test_name)
    address_book_page.click_add_phone(test_phone)
    address_book_page.click_select_province("294")
    address_book_page.click_select_district("501")
    address_book_page.click_commune_select("10616")
    address_book_page.click_add_address(test_address)
    address_book_page.click_agency_company()
    address_book_page.click_default_address()
    address_book_page.click_update_btn()
    
    new_address_card = address_book_page.address_items.filter(has_text=test_name).filter(has_text=test_phone).filter(has_text=test_address).first
    
    expect(new_address_card).to_be_visible()
    
    
    expect(new_address_card.locator(".name")).to_contain_text(test_name)
    expect(new_address_card.locator(".phone")).to_contain_text(test_phone)
    expect(new_address_card.locator(".address")).to_contain_text(test_address)
    
    # expect(new_address_card.locator(".checkbox-fake")).to_contain_text("Địa chỉ mặc định")
    default_label = address_book_page.get_card_default_label_locator(new_address_card)
    expect(default_label).to_be_visible()      