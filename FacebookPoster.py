#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import shelve
import random


def facebook_post_quote(quote_category):
    os.chdir(main_directory)
    # Following code logs into Facebook
    browser = webdriver.Chrome(executable_path=executable_path)
    browser.get("https://www.facebook.com/")
    email_element = browser.find_element_by_css_selector("input[type='email']")
    pass_element = browser.find_element_by_css_selector("input[type='password'")
    email_element.send_keys(login_details.get("Bot email"))
    pass_element.send_keys(login_details.get("Bot password"))
    pass_element.submit()

    quote_list_directory = quotes_directory + "\\" + quote_category.title() + "_Quotes.txt"
    text_file = open(quote_list_directory)
    lines = text_file.readlines()
    random_index = random.randrange(0, len(lines) - 1)

    browser.get("https://www.facebook.com/AutoSchedule/")
    type_element = browser.find_element_by_css_selector("div[aria-autocomplete]")
    type_element.send_keys(lines[random_index])
    type_element.send_keys(Keys.CONTROL, Keys.ENTER)

    time.sleep(10)  # Allow time for posting to finish
    print("Program execution finished")



login_details = {
    "Main email": "",
    "Main password": "",
    "Bot email": "",
    "Bot password": ""
}
main_directory = "C:\\My Python Programs\\Facebook Spam"
quotes_directory = "C:\\Users\\Tim\\Desktop\\Brainy Quotes"
executable_path = "C:\\Gecko\\chromedriver.exe"  # For Chrome

selected_quote = input("Enter the category of quotes you would like: ")
facebook_post_quote(selected_quote.title())





"""
if not os.path.exists(quotes_directory + "\\" + "QuotesLog.dat"):
    print("Creating new storage")
    shelf_file = shelve.open(quotes_directory + "\\" + "QuotesLog")
else:
    print("Storage already exists")
    shelf_file = shelve.open(quotes_directory + "\\" + "QuotesLog")
"""
