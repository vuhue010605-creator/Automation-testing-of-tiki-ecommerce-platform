import json
import os
import re
from playwright.sync_api import Page, expect

from pages.profile_page import ProfilePage

def test_profile_update_invalid_name(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_full_name("cbvbcvbcvbcvbc")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text("Họ & Tên gồm 2 từ trở lên")
    
def test_profile_empty_name(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_full_name("")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text("Họ & Tên không được để trống")
    
def test_profile_special_characters_name(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_full_name("@#$%&*!@#123")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text("Họ tên không bao gồm kí tự đặc biệt và số")
    
def test_profile_inappropriate_characters_name(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_full_name("test test")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text("Họ tên có chứa từ không phù hợp")
    
def test_profile_long_character_name(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_full_name("Ngày xưa lúc thơ bé ta thường nhìn mưa hát Và khi cơn mưa như nặng hạt lại có bóng nước chợt tan Mẹ bảo ta rằng bong bóng mưa")
    profile_page.save_changes() 
    
    expect(profile_page.error_message).to_have_text('Độ dài tối đa cho "họ tên" là 64 kí tự') 

def test_profile_short_characters_nickname(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_nickname("hi")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text('Nickname hợp lệ từ 3-20 kí tự, chỉ bao gồm chữ, số, “_” và “.”')
    
def test_profile_long_characters_nickname(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_nickname("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text('Nickname hợp lệ từ 3-20 kí tự, chỉ bao gồm chữ, số, “_” và “.”')

def test_profile_special_characters_nickname(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_nickname("hiiiiiii@#$")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text('Nickname hợp lệ từ 3-20 kí tự, chỉ bao gồm chữ, số, “_” và “.”')               

def test_profile_inappropriate_characters_nickname(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_nickname("test")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text("Nickname có chứa từ không phù hợp")
    
def test_profile_nickname_already_exists(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.fill_nickname("hue")
    profile_page.save_changes()
    
    expect(profile_page.error_message).to_have_text("Nickname đã được sử dụng")

# Test FAIL - Bug
def test_profile_birth_word(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.select_day("0")
    profile_page.select_month("0")
    profile_page.select_year("0")
    
    profile_page.save_changes()
    expect(profile_page.error_message).to_have_text("Ngày sinh không hợp lệ")
    
def test_profile_birth_number(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.select_day("1")
    profile_page.select_month("1")
    profile_page.select_year("2026")
    
    profile_page.save_changes()
    expect(profile_page.success_message).to_have_text("Cập nhật thông tin thành công")
   





def test_profile_gender_nickname(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.select_gender("Nữ")
    profile_page.save_changes()
    
    expect(profile_page.success_message).to_have_text("Cập nhật thông tin thành công")
    
def test_profile_country_nickname(logged_in_page):
    profile_page = ProfilePage(logged_in_page)
    profile_page.open_account_menu()
    profile_page.click_account_info()
    profile_page.select_country("Việt Nam")
    profile_page.save_changes()
    expect(profile_page.success_message).to_have_text("Quốc tịch đã được cập nhật")
