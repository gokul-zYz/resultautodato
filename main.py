import os
from selenium import webdriver
from discord_webhook import DiscordWebhook,DiscordEmbed
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

def cord(result,colr):
  webhookurl="https://discord.com/api/webhooks/1035595915894984855/qhPVZeypFgsNwvNvAn3mwExKrvyRCv6r2ODMl2HM4ZD7JpBG7Lsccr7mc9DaCP7hbkCY"
  webhook=DiscordWebhook(url=webhookurl)
  embed=DiscordEmbed(title="RESULT-:",description=result,color=colr)
  webhook.add_embed(embed)
  webhook.execute()

def result():
  
   driver.get("http://exam.pondiuni.edu.in/results/")
   driver.find_element(By.XPATH, '//*[@id="reg_no"]').send_keys("19tH0426")
   driver.find_element(By.XPATH, '//*[@id="exam"]').send_keys("seventh")
   driver.find_element(By.XPATH, '//*[@id="print_app_form"]/span').click()
   
   
   time.sleep(1)
   try: 
    driver.switch_to.alert.accept()
    cord("NOT YET CAME","ED4245")
   
   except:
     cord("CAME ","57F287")
     
   result()
  
    
result()
driver.close()

