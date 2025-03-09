import time
from driver import *
import csv
import os
import queue
import threading
Header = ["urls"]
Header_2 = ["Jobs Urls"]
Header_3 = ["Job Title", "Base Pay", "Salaries Submitted",
            "Confidence Level", "Updated Date", "Country", "Experience Level",
            "Average pay per year", "Range pay per year"]
def writing_csv(row):
    fp = 'compines.csv'
    with open(fp, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if os.path.getsize(fp) == 0:
            writer.writerow(Header)
        writer.writerow(row)

def writing_csv_2(row):
    fp = 'jobs.csv'
    with open(fp, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if os.path.getsize(fp) == 0:
            writer.writerow(Header_2)
        writer.writerow(row)

def writing_csv_3(row):
    fp = 'data.csv'
    with open(fp, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if os.path.getsize(fp) == 0:
            writer.writerow(Header_3)
        writer.writerow(row)
# def start_browser():
#     """Starts undetected Chrome browser."""
#     options = uc.ChromeOptions()
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     driver = uc.Chrome(options=options)
#     driver.set_page_load_timeout(30)
#     return driver
#
#
# driver = start_browser()
class Glassdoor(Selenium):

    def login(self):
        self.get('https://www.glassdoor.co.uk/Salary/SelfEmployed-com-Director-Salaries-E5529631_D_KO17,25.htm')
        try:
            time.sleep(15)
            self.wait.until(EC.presence_of_element_located((By.XPATH, '(//button[@class="button_Button__BWBls button-base_Button__YPLQY"])[1]')))
            sign_in_button = self.find_element(By.XPATH, '(//button[@class="button_Button__BWBls button-base_Button__YPLQY"])[1]')
            time.sleep(2)
            sign_in_button.click()
            time.sleep(10)
            print("Clicked on Sign-In button.")
        except Exception as e:
            print("Error clicking Sign-In button:", e)

        # time.sleep(2)

        # Enter credentials
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'sign in')]")))
            email_input = self.find_element(By.XPATH, "//input[@type='email']")
            email_input.send_keys("qanfat70@gmail.com")  # Replace with your email
            email_input.send_keys(Keys.RETURN)

            time.sleep(2)

            password_input = self.find_element(By.XPATH, "//input[@type='password']")
            password_input.send_keys("Musabinnaveed2$")  # Replace with your password
            password_input.send_keys(Keys.RETURN)
            print("Logged in successfully.")
            time.sleep(5)
        except Exception as e:
            print("Error entering credentials:", e)

    def changing_country(self):
        select_coun = self.find_element(By.XPATH, "(//div[@type='button'])[1]")
        time.sleep(2)
        select_coun.click()

    def crawling(self):
        while True:
            i = 1
            try:
               for i in range(1,5):
                    urls_compines = self.href(By.XPATH, f'(//a[@datatype="Salaries"])[{i}]')
                    print(urls_compines)
                    i = i+1
                    row = [urls_compines]
                    writing_csv(row)
            except:
                pass
            next_page = self.find_element(By.XPATH, '(//button[@class="pagination_ListItemButton__se7rv'
                                                    ' pagination_Chevron__9Eauq"])[2]')
            next_page.click()
            # time.sleep(2)

    def filters(self):
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="Job function"]')))
        job_fun_elm = self.find_element(By.XPATH, '//button[@class="accordion-item_Button__JhFIY"]')
        job_fun_elm.click()
        time.sleep(3)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '(//label[@class="checkbox-base_CheckboxContainer__Lz_M0"])[1]')))
        for i in range(1, 4):
            time.sleep(3)
            box_to_click = self.find_element(By.XPATH, f'(//label[@class="checkbox-base_CheckboxContainer__Lz_M0"])[{i}]')
            box_to_click.click()
            i = +1
        time.sleep(2)
        size_elm = self.find_element(By.XPATH, '(//span[@class="radio_LabelText__4WFWR"])[1]/..//input')
        size_elm.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        size_elm.click()
        time.sleep(3)
        print("done")
        self.crawling()

    def scroll_down(self):
        """Scrolls to the bottom of the page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def crawler_2(self):
        print("stated")
        while True:
            try:
                i = 1
                while True:
                    jobs_elm = self.href(By.XPATH, f'(//td[@class="salarylist_table-element___3Va_"'
                                                   f']//*[@class="salarylist_job-title-link__MXnPX"])[{i}]')
                    job_title = self.text(By.XPATH, f'(//td[@class="salarylist_table-element___3Va_"]//a)[{i}]')
                    print(i,jobs_elm)
                    i = i+1
                    row2 = [jobs_elm, job_title]
                    writing_csv_2(row2)
            except:
                pass
            job_btn = self.find_element(By.XPATH, '(//button[@class="pagination_ListItemButton__se7rv'
                                                   ' pagination_Chevron__9Eauq"])[2]')
            job_btn.click()

    def _scraping(self):
        i = 1
        while True:
            try:
                if i == 8:
                    break
                exp_elm = self.find_element(By.XPATH, '(//div[@type="button"])[2]')
                exp_elm.click()
                print('clicked')
                time.sleep(2)
                exp_button = self.find_element(By.XPATH, f'(//li[@class='
                                                         f'"data-select_SelectItem__tVKZp"])[{i}]')
                exp_button.click()
                time.sleep(1.5)
                i = i + 1
            except:
                print('error')
            try:
                exp_text_elm = self.find_element(By.XPATH, '(//span[@class="filter-chip_FilterChipText__HQdHz"])[2]').text
            except:
                exp_text_elm = 'N/A'
            try:
                base_pay_element = self.find_element(By.XPATH, '(//div[@class="hero_TotalPayLayout__X55hl hero_PayRange__nKzVj"])[1]').text
            except:
                base_pay_element = "N/A"
            try:
                salaries_submitted_element = self.find_element(By.XPATH, '//span[@data-test="salaries-submitted"]').text
            except:
                salaries_submitted_element = "N/A"
            try:
                confidence_element = self.find_element(By.XPATH, '//span[@class="confidence_ConfidenceLabel__M4wsy"]').text
            except:
                confidence_element = "N/A"
            try:
                updated_date_element = self.find_element(By.XPATH, "//span[contains(@data-test, 'last-updated')]").text
            except:
                updated_date_element = "N/A"
            try:
                contry_elm = self.find_element(By.XPATH, '(//span[@class="filter-chip_FilterChipText__HQdHz"])[1]').text
            except:
                contry_elm = "N/A"
            try:
                average_element = self.find_element(By.XPATH, '(//span[@class="hero_AdditionalPayFont__C2brS"])[1]').text
            except:
                average_element = "N/A"
            try:
                range_element = self.find_element(By.XPATH, '(//span[@class="hero_AdditionalPayFont__C2brS"])[2]').text
            except:
                range_element = "N/A"

            row = ["N/A",base_pay_element, salaries_submitted_element, confidence_element,
                   updated_date_element, contry_elm, exp_text_elm,average_element, range_element]
            print(row)
            writing_csv_3(row)

    def open_web(self):
        self.get("https://www.glassdoor.co.uk/Reviews/index.htm")
        time.sleep(60)
        self.login()
        self.filters()

    q = queue.Queue()
    with open('compines.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            link1 = row["urls"]
            if link1:  # Ensure the link is not empty
                q.put(link1)

    def open_links(self):
        # open compaines links
        """
        open links
        :return:
        """
        chrome_options = Options()
        chrome_options.add_argument("--head")  # Run in headless mode
        while not self.q.empty():
            links = self.q.get()
            if isinstance(links, str):
                print(f"Opening {links}")
                try:
                    self.get(links)
                    time.sleep(5)
                    self.crawler_2()
                except ExceptionGroup:
                    print(f"Failed to open {links}")
            self.q.task_done()
            time.sleep(1)

        # try:
        #     self.login()
        # except:
        #     pass
        #
        # time.sleep(60)
        # self.filters()

    q1 = queue.Queue()
    with open('jobs.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            link = row["Jobs Urls"]
            if link:  # Ensure the link is not empty
                q1.put(link)

    def open_links_2(self):
        # job links
        """
        open links
        :return:
        """
        chrome_options = Options()
        chrome_options.add_argument("--head")  # Run in headless mode
        while not self.q1.empty():
            links = self.q1.get()
            if isinstance(links, str):
                print(f"Opening {links}")
                try:
                    self.get(links)
                    time.sleep(5)
                    self._scraping()
                except ExceptionGroup:
                    print(f"Failed to open {links}")
            self.q.task_done()
            time.sleep(1)

        # try:
        #     self.login()
        # except:
        #     pass
        #
        # time.sleep(60)
        # self.filters()