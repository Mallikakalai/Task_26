import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ImdbSearch_page import IMDBSearchpage
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    time.sleep(2)
    driver.close()
    driver.quit()

def test_IMDBpage(driver):
    IMDBSearchpage_obj = IMDBSearchpage(driver)
    IMDBSearchpage_obj.open_page("https://www.imdb.com/search/name/")
    IMDBSearchpage_obj.click_expand()
    IMDBSearchpage_obj.search_inputs(
        name="Audrey",
        birthmin="14071990",
        birthmax="14072000",
        birthday="06-14",
        deathmin="2000",
        deathmax="2022",
        topic_select="Place of birth"
        )
    IMDBSearchpage_obj.gender_button()
    IMDBSearchpage_obj.credit_input(credit_text="Holiday")
    IMDBSearchpage_obj.seeresult()

