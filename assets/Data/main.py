from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import json


def get_data():
    print("Starting to Get data")
    data = []
    url = "https://www.google.com/maps/search/restaurants/@8.768232,76.7720407,11z/data=!4m2!2m1!6e5?entry=ttu"
    driver = webdriver.Chrome()
    driver.get(url)
    print("Reached Site!")
    counter = 0
    print("Starting to scroll")
    while counter != 10:
        driver.execute_script('document.querySelector("#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd").scrollBy(0, 40000)')
        counter += 1
        time.sleep(1)

    restaurants = driver.find_elements(By.CSS_SELECTOR, "div.bfdHYd.Ppzolf.OFBs3e")
    print("Getting Details and add them to the dic")
    for restaurant in restaurants:
        name = restaurant.find_element(By.CSS_SELECTOR, "div.lI9IFe > div.y7PRA > div > div > div.UaQhfb.fontBodyMedium > div.NrDZNb > div.qBF1Pd.fontHeadlineSmall")
        img = restaurant.find_element(By.CSS_SELECTOR, "div.lI9IFe > div.SpFAAb > div > div.p0Hhde.FQ2IWe > img")
        try:
            rating = restaurant.find_element(By.CSS_SELECTOR, "div.lI9IFe > div.y7PRA > div > div > div.UaQhfb.fontBodyMedium > div:nth-child(3) > div > span.e4rVHe.fontBodyMedium > span > span.MW4etd").text
        except:
            rating = "No Review"
        details = {"name": name.text, "img": img.get_attribute("src"), "rating": rating}
        data.append(details)
    print("Got all the data, Sending them to create json")
    make_json(data)

def make_json(data):
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
        print("Dumped the info")



if "__main__" == __name__:
    get_data()