from selenium import webdriver
import settings
# Author: Yassine Ahmed Ali


class CoronaCases:
    def __init__(self):
        op = webdriver.ChromeOptions()
        op.add_argument("headless")
        self.driver = webdriver.Chrome(options=op)
        self.driver.get(f"{settings.initial_address}{settings.country_name}")
        self.cases = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div/div[4]/div/span").text
        self.deaths = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div/div[5]/div/span").text
        self.recovered = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div/div[6]/div/span").text

class CommandLine:
    def __init__(self):
        self.running = True
        self.Main()
    def Main(self):
        # Gets the country name
        i = 0
        while self.running:
          
            if i % 3 == 0:
                settings.country_name = input(
                    "Insert the country's name: ").lower()
            user_input = input("> ")
            if user_input.lower() == "cases":
                print(f"Current cases: {CoronaCases().cases}")
                i += 1
            elif user_input.lower() == "deaths":
                print(f"Current deaths: {CoronaCases().deaths}")
                i += 1
            elif user_input.lower() == "recovered":
                print(f"Current recovered: {CoronaCases().recovered}")
                i += 1
            elif user_input.lower() == "quit":
                self.running = False
            else:
                print("Command not found..")


CommandLine()





