from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class CathayBankAutomation(object):
    def __init__(self):
        self.option = Options()
        self.option.add_argument("window-size=1920,1080")
        self.option.add_argument("--start-maximized")
        self.option.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(service=Service(), options=self.option)
        self.wait = WebDriverWait(self.driver, 10)
    
    def __del__(self):
        self.driver.quit()

    def visitHomePage(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        # check page is loaded
        self.loginBtn_xpath='//*[@id="lblLoginText"]'
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.loginBtn_xpath)))
        except TimeoutException:
            print("Fail to load Home page")

    def takeScreenshot(self, filename="screenshot.png"):
        self.driver.get_screenshot_as_file(filename)

    def findCardMenu(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ga-menu-lv1][text()="產品介紹"]'))).click()
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cubre-o-menuLinkList__btn"]/div[@data-menul2-btn][text()="信用卡"]')))
        except TimeoutException:
            print("Fail xxxxx")
        cardList_xpath = '//div[@class="cubre-o-menuLinkList__btn"]/div[@data-menul2-btn][text()="信用卡"]/../following-sibling::div'
        cardList = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, cardList_xpath)))
        cardItems = cardList.find_elements(By.XPATH,'a')
        print("項目數量：", len(cardItems))

    def countDiscontinuedCard(self):
        cardIntro_xpath = '//a[@data-ga-menu-lv3="-"][text()="卡片介紹"]'
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, cardIntro_xpath))).click()
        except TimeoutException:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ga-menu-lv1][text()="產品介紹"]'))).click()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, cardIntro_xpath))).click()
        stopcardList = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//section[@data-anchor-block="blockname06"]/div/div[@class="cubre-o-block__component"]/div/div[@class="swiper-wrapper"]')))
        stoppedCards = stopcardList.find_elements(By.XPATH, '*')
        print("(停發)信用卡數量：", len(stoppedCards))


if __name__ == "__main__":
    try:
        automation = CathayBankAutomation()
        # Execute the automated testing flow
        automation.visitHomePage()
        automation.takeScreenshot("/Users/peiwenchen/Desktop/pytest/cathay_bank_home.png")
        automation.findCardMenu()
        automation.takeScreenshot("/Users/peiwenchen/Desktop/pytest/card_items.png")
        automation.countDiscontinuedCard()
        automation.takeScreenshot("/Users/peiwenchen/Desktop/pytest/stopped_cards.png")
    finally:
        automation = None
