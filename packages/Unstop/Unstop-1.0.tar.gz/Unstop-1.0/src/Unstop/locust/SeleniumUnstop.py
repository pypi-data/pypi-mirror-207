# # import csv
# import random
# # from time import sleep
# from locust import HttpUser, SequentialTaskSet, task, constant_pacing
# from locust_plugins.csvreader import CSVReader
# # import os
# # import re
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("C:\\msedgedriver.exe")
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#
#
# def roleMember():
#     driver.implicitly_wait(10)
#     try:
#         a = driver.find_element(By.XPATH, "//span[contains(text(),'is answering this question.')]")
#         assert a.text == a.text
#     except:
#         print("Team Member answering the question Hint text message not displayed")
#
#     answered_text = driver.find_element(By.XPATH, "//span[contains(text(),'Answered')]")
#     if answered_text.is_displayed():
#         driver.find_element(By.XPATH,
#                             "/html/body/div/main/app-play-panel/section[1]/div/app-quiz/app-play/div/div/div[2]/div[1]/app-quiz-current-card/div/div[2]/div[2]/button[2]").click()
#
#     driver.find_element(By.XPATH,
#                         "/html/body/div/main/app-play-panel/section[1]/div/app-quiz/app-play/div/div/div[1]/app-header-nav/div/div/div[3]/div/a[2]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH,
#                         "/html/body/div/main/app-play-panel/section[1]/div/app-quiz/app-play/div/div/div[2]/app-quiz-status/div/div/div[3]/button").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH,
#                         "/html/body/div/main/app-play-panel/section[1]/div/app-quiz/app-play/div/div/div[2]/app-quiz-status/div[3]/div/button[2]").click()
#
#
# def rolePlayer():
#     Total_questions = driver.find_elements(By.XPATH, "//div[@class='wrapper']/span")
#
#     for question in Total_questions:
#         print(question.text)
#
#         option = random.randint(1, 5)
#
#         if driver.find_element(By.XPATH, "//span[@class='navigation_btn ng-star-inserted active']"):
#             driver.find_element(By.XPATH, "//div[@class='answers']/div/div/div[1]/div/label[option]").click()
#             driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
#         else:
#             print("not found")
