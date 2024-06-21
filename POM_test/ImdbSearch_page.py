from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDBSearchpage:
    def __init__(self, driver):
        self.driver = driver
        self.expand = (By.CSS_SELECTOR, "button[data-testid='adv-search-expand-all']")
        self.name_input=(By.CSS_SELECTOR,"input[name='name-text-input']")
        self.birth_start=(By.CSS_SELECTOR,"input[name='birth-date-start-input']")
        self.birth_end=(By.CSS_SELECTOR,"input[name='birth-date-end-input']")
        self.birthday_input=(By.CSS_SELECTOR,"input[name='birthday-input']")
        self.topic_text=(By.CSS_SELECTOR,"input[name='within-topic-input']")
        self.death_start=(By.CSS_SELECTOR,"input[name='death-date-start-input']")
        self.death_end=(By.CSS_SELECTOR,"input[name='death-date-end-input']")
        self.topic_dropdown=(By.ID,"within-topic-dropdown-id")
        self.adult_input=(By.CSS_SELECTOR,"input[id='include-adult-names']")
        self.gender_female_button=(By.CSS_SELECTOR,"button[data-testid='test-chip-id-FEMALE']")
        self.credit_dropdown=(By.CSS_SELECTOR,"input[data-testid='autosuggest-input-test-id-filmography']")
        self.search_button=(By.CSS_SELECTOR,"button[data-testid='adv-search-get-results']")
    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_expand(self):
        self.driver.execute_script("window.scrollTo(500, 500);")
        self.expand_click=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.expand))
        actions = ActionChains(self.driver)
        actions.click(self.expand_click)
        actions.perform()

    def search_inputs(self, name, birthmin, birthmax, birthday, deathmin, deathmax, topic_select):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_input)).send_keys(name)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birth_start)).send_keys(birthmin)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birth_end)).send_keys(birthmax)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birthday_input)).send_keys(birthday)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_start)).send_keys(deathmin)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.death_end)).send_keys(deathmax)
        Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.topic_dropdown))).select_by_visible_text(topic_select)

    def gender_button(self):
        gender_female_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='test-chip-id-FEMALE']")
        actions = ActionChains(self.driver)
        actions.click(gender_female_button)
        actions.perform()


    def credit_input(self, credit_text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.credit_dropdown)).send_keys(credit_text)
        actions = ActionChains(self.driver)
        actions.pause(2)
        actions.send_keys(Keys.DOWN)
        actions.pause(2)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def seeresult(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_button)).click()






