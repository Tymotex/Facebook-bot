#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import pprint
import random


def facebook_spam():
    os.chdir(main_directory)
    # type_element = browser.find_element_by_css_selector("div[aria-autocomplete]")
    # post_button_element2 = browser.find_elements_by_css_selector("button[type='submit']")
    # post_button_element = browser.find_elements_by_css_selector("span[class='']")
    # print(post_button_element[0].text + "\n" + post_button_element[1].text)
    # Spams random lines from a plaintext document (compliments or insults)

    # Following code logs into Facebook
    browser = webdriver.Chrome(executable_path=executable_path)
    browser.get("https://www.facebook.com/")
    email_element = browser.find_element_by_css_selector("input[type='email']")
    pass_element = browser.find_element_by_css_selector("input[type='password'")
    email_element.send_keys(login_details.get("Main email"))
    pass_element.send_keys(login_details.get("Main password"))
    pass_element.submit()

    while not quit:
        spam_amount = int(input("Enter how many entries you would like to spam the victim with (int): "))
        victim = input("Enter the name of your victim: ").title()
        # Navigates to the the person's messenger window and selects the typing field
        choice = input("Spam to messenger or to wall? (m/w) ")

        if choice == "w":
            victim_link = victims.get(victim)
        elif choice == "m":
            victim_link = victims.get(victim)[:24] + "/messages/t/" + victims.get(victim)[25:]
            print(victim_link)
        else:
            raise SystemExit
        browser.get(victim_link)

        spam_type_dict = {
            # New plaintext files can be added here!
            "1": "Insults.txt",
            "2": "Compliments.txt",
            "3": "Science pickup lines.txt",
            "4": "GachiList.txt"
        }
        pprint.pprint(spam_type_dict)
        spam_type = int(input("Enter the number ID for the kind of spam you'd like: "))
        spam_list = open(spam_type_dict.get(str(spam_type)), "r")
        print("Selected: " + spam_type_dict.get(str(spam_type)))
        list_of_spam = spam_list.readlines()
        # print("Number of spam entries in the plaintext file: ", len(list_of_spam))
        # Spam time!
        spam_counter = 0
        spam_sent = []
        while spam_counter < spam_amount:
            random_index = random.randint(0, len(list_of_spam) - 1)
            type_element = browser.find_element_by_css_selector("div[aria-autocomplete]")
            if list_of_spam[random_index] not in spam_sent:
                type_element.send_keys(list_of_spam[random_index])
                # time.sleep(1)
                type_element.send_keys(Keys.CONTROL, Keys.ENTER)
                # time.sleep(3)
                spam_counter += 1
            else:
                continue
        print("Facebook spam has completed!")
        again = input("Spam again? (y/n) ")
        if again == "y":
            spam_amount = int(input("Enter how many entries you would like to spam the victim with (int): "))
            spam_list.close()
            continue
        elif again == "n":
            spam_list.close()
            break
    print("Program execution finished")


victims = {
    "Tim": "https://www.facebook.com/tim.zhang.5030"
}
login_details = {
    "Main email": "",
    "Main password": "",
    "Bot email": "",
    "Bot password": ""
}
main_directory = "C:\\My Python Programs\\Facebook Spam"
executable_path = "C:\\Gecko\\chromedriver.exe"  # For Chrome
quit = False

facebook_spam()
