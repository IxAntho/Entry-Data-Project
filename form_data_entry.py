from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

form_url = "https://forms.gle/FaDjpPdVaP68pWCc9"


class FormDataEntry:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def type_values(self, links, prices, addresses):
        self.driver.get(form_url)
        for i in range(len(links)):
            try:
                time.sleep(4)
                input_list = self.driver.find_elements(By.CSS_SELECTOR, value="div.Xb9hP > input.whsOnd.zHQkBf")
                submit_bttn = self.driver.find_element(By.XPATH,
                                                       value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')

                input_list[0].send_keys(addresses[i])
                input_list[1].send_keys(prices[i])
                input_list[2].send_keys(links[i])
                submit_bttn.click()
                time.sleep(2)
                another_response_bttn = self.driver.find_element(By.CSS_SELECTOR,
                                                                 value="body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a")
                another_response_bttn.click()
                time.sleep(2)

                print(i)
            except NoSuchElementException:
                print("One element hasn't been found")

        print("Success!")
