import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# caminho para o chromedriver
driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# o array targets são os destinatários que receberão as mensagens. colocar aspas duplas dentro das aspas simples
while True:
    targets = ['"Victor Miranda"']
    # mensagem que será enviada
    str_message = "Selenium test"
    # envia para todos os destinatarios
    for target in targets:

        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()

        message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

        message.send_keys(str_message)

        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()
    time.sleep(1)

driver.close()
