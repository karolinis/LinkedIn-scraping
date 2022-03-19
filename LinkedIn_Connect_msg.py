import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def Log_in(driver, emailas, passwordas):

    driver.get('https://www.linkedin.com/talent/home')
    print('Logging in...')
    try:
        # wait refers to waiting for the element under to appear
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        # enter username/emails
        username = driver.find_element_by_id('username').send_keys(emailas)
    except:
        print('Login failed')
        driver.quit()
        exit()

    try:
        # enter password
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        password = driver.find_element_by_id('password').send_keys(passwordas)
        # click login
        log_in_button = driver.find_element_by_xpath('//*[@type="submit"]').click()
    except:
        print('Login failed')
        driver.quit()
        exit()

    # enter two authenticator
    code = str(input('Enter the code: '))

    try:
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="tel"]')))
        input_code = driver.find_element_by_xpath("//input[@type='tel']").send_keys(code)
        ok = driver.find_element_by_tag_name('button').click()
    except:
        print('Code not found, try again')
        code = int(input('Enter the code: '))
        input_code = driver.find_element_by_xpath("//input[@type='tel']").send_keys(code)
        ok = driver.find_element_by_tag_name('button').click()

    # mandatory button to click to access recruiter lite
    try:
        wait_click("//span[text()='Select Recruiter Lite contract']/../..")
    except:
        pass

def LinkedIn_filter(driver, prj_title, job_titles, locations, workplace_types, skills, companies, schools,
                               year_of_graduation, industries, keywords, seniority): #arguments can be inputs and passwords.

    #options
    driver.maximize_window()
    Log_in(driver)

    # click on project
    wait_click("//a[text()='Projects']")
    wait_click("//a[@href='/talent/create/get-started']")
    #enter project name
    wait_click("//input[@placeholder='Name (required)']")
    fill_name = driver.find_element_by_xpath("//input[@placeholder='Name (required)']").send_keys(prj_title)
    #create project
    wait_click("//span[text()='Create project']/..")
    # click on Talent pool
    time.sleep(1)
    wait_click("//div[text()='Talent pool']/..")

    #send inputs to search bar
    if len(job_titles) != 0:
        wait_click("//h2[text()='Job titles']/../../following-sibling::button")
        for title in job_titles.split(','):
            title = title.strip()
            fill_form = driver.find_element_by_xpath("//input[@placeholder='enter a job title or boolean…']").send_keys(title)
            try:
                wait_click('//div[@data-live-test-job-titles-typeahead-results]//child::div[1]')
            except:
                print(f'Job title {job_titles} not found, try again')


    # enter location
    if len(locations) != 0:
        wait_click("//h2[text()='Locations']/../../following-sibling::button")
        driver.execute_script("window.scrollTo(0, 500)")
        for location in locations.split(','):
            location = location.strip()
            fill_form = driver.find_element_by_xpath("//input[@placeholder='enter a location…']").send_keys(location)
            try:
                wait_click("//div[@data-live-test-result=0]")
            except:
                print(f'Location {location} not found, try again')

    if len(workplace_types) != 0:
        wait_click("//h2[text()='Workplace types']/../../following-sibling::button")
        for workplace in workplace_types.split(','):
            workplace = workplace.strip()
            try:
                wait_click(f"//a[contains(.,'{workplace}')]")
            except:
                print(f'Workplace type {workplace} not found, try again')

    if len(industries) != 0:
        wait_click("//h2[text()='Industries']/../../following-sibling::button")
        for industry in industries.split(','):
            fill_form = driver.find_element_by_xpath("//input[@placeholder='enter a industry…']").send_keys(industry)

            try:
                wait_click('//div[@data-live-test-result=0]')
            except:
                print(f'Industry {industry} not found, try again')

    if len(skills) != 0:
        wait_click("//h2[text()='Skills and Assessments']/../../following-sibling::button")
        for skill in skills.split(','):
            fill_form = driver.find_element_by_xpath("//input[@placeholder='enter a skill…']").send_keys(skill)
            try:
                wait_click('//div[@data-live-test-result=0]')
            except:
                print(f'Skill {skill} not found, try again')

    if len(companies) != 0:
        wait_click("//h2[text()='Companies']/../../following-sibling::button")
        for company in companies.split(','):
            company = company.strip()
            fill_form = driver.find_element_by_xpath("//input[@placeholder='enter a company or boolean…']").send_keys(company)
            try:
                wait_click('//div[@data-live-test-result=0]')
            except:
                print(f'Company {company} not found, try again')

    if len(keywords) != 0:
        wait_click("//h2[text()='Keywords']/../../following-sibling::button")
        form = driver.find_element_by_xpath("//textarea")
        fill_form = form.send_keys(keywords)
        enter = form.send_keys(Keys.ENTER)

    if len(schools) != 0:
        wait_click("//h2[text()='Schools']/../../following-sibling::button")
        for school in schools.split(','):
            school = school.strip()
            fill_form = driver.find_element_by_xpath("//input[@placeholder='enter a school…']").send_keys(school)
            try:
                wait_click('//div[@data-live-test-result=0]')
            except:
                print(f'School {school} not found, try again')

    if len(year_of_graduation) != 0:
        wait_click("//h2[text()='Year of graduation']/../../following-sibling::button")
        from_year, to_year = year_of_graduation.split('-')
        try:
            fill_form = driver.find_element_by_xpath("//form//input[@name='range-from']").send_keys(from_year)
            fill_form2 = driver.find_element_by_xpath("//form//input[@name='range-to']").send_keys(to_year)
        except:
            pass

    if len(seniority) != 0:
        wait_click("//h2[text()='Seniority']/../../following-sibling::button")
        for senior in seniority.split(','):
            senior = senior.strip()
            try:
                wait_click(f"//a[contains(.,'{senior}')]")
            except:
                print(f'Seniority type {senior} not found, try again')

    # advanced search
    wait_click("//footer/a")

    # scroll to top of page
    # click on search
    driver.execute_script("window.scrollTo(500, 0)")
    wait_click("//button[text()='Search']")
    time.sleep(5)

    profiles = pd.DataFrame(columns=['name', 'url'])

    #reaccurring function to scrape profiles and select next page until exhausted
    profiles = reac_next_page(driver,profiles)
    return profiles

#wait for the xpath to load on the website and click on it. Only for SOLO elements
def wait_click(xpath):
    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        locate_location = driver.find_element_by_xpath(
            xpath).click()
    except:
        pass


def reac_next_page(driver,profiles):
    #wait for profiles to appear
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//article[@class='profile-list-item hp-core-temp ']//article//div[@class='artdeco-entity-lockup__title ember-view']/a")))
    # get all profiles and append their links to a list
    try:
        all_profiles = driver.find_elements_by_xpath(
        "//article[@class='profile-list-item hp-core-temp ']//article//div[@class='artdeco-entity-lockup__title ember-view']/a")
    except:
        pass
    for profile in all_profiles: #add profiles to dataframe
        profiles = profiles.append({'name': profile.text, 'url': profile.get_attribute('href')}, ignore_index=True)
    try: #check if next page exists
        next_page = driver.find_element_by_xpath("//a[contains(.,'Go to next page')]").click()
        reac_next_page(driver,profiles)
    except: #if not, return dataframe & create file
        profiles.to_excel(f'{prj_title}_all_contacts.xlsx', index=False)

def advanced_filter(profiles, message):
    urls = profiles['url'].tolist()
    # chrome options --headless
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    wanted_candidates = pd.DataFrame(columns=['name', 'url'])
    time.sleep(2)
    for profile in range(len(urls)):
        first_name = profiles.iloc[profile, 0].split(' ')[0]
        driver.get(urls[profile])
        # wait for page to load

        try: #try to locate accomplishments, not everyone has them in profile
            time.sleep(0.5)
            wait = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, "//ul//div[text()='English']/following-sibling::div")))
            # look if the person has English level at full working proficiency or professional working proficiency

            try:
                english_proficiency = driver.find_element_by_xpath(
                    "//ul//div[text() = 'English']/following-sibling::div[contains(., 'Professional working proficiency')]").text

            except:
                try:
                    english_proficiency = driver.find_element_by_xpath(
                        "//ul//div[text() = 'English']/following-sibling::div[contains(., 'Full professional proficiency')]").text

                except:
                    try:
                        english_proficiency = driver.find_element_by_xpath(
                            "//ul//div[text() = 'English']/following-sibling::div[contains(., 'Native / Bilingual proficiency')]").text

                    except:
                        english_proficiency = ''
        except:
            print(f'Accomplishments not found in profile for {profiles.iloc[profile, 0]}')
            english_proficiency = 'NA'

        if english_proficiency == 'Full professional proficiency' or english_proficiency == 'Professional working proficiency' or english_proficiency == 'Native or bilingual proficiency':
            # check for college (filter out)

            try:
                wait = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//h2[text()='Education']/../..//following-sibling::ul[contains(.,'Kolegija')]")))
                time.sleep(0.5)
                college = driver.find_elements_by_xpath(
                    "//h2[text()='Education']/../..//following-sibling::ul[contains(.,'Kolegija')]")
            except:
                try:
                    wait = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "//h2[text()='Education']/../..//following-sibling::ul[contains(.,'College')]")))
                    time.sleep(0.5)
                    college = driver.find_elements_by_xpath(
                    "//h2[text()='Education']/../..//following-sibling::ul[contains(.,'College')]")
                except:
                    college = []

            if len(college) == 0:
                print('Wanted candidate: {}'.format(profiles.iloc[profile,0]))
                #wait for the profile link to load, then save it in a file
                #with this link we will have a database of wanted candidates
                #we will use it to connect with them via predefined notes

                wait = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//h3[text()='Personal Information']//..//a")))
                public_profile = driver.find_element_by_xpath("//h3[text()='Personal Information']//..//a").get_attribute('href')
                driver.get(public_profile)
                try:
                    wait = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@class='pvs-profile-actions ']//span[contains(.,'Connect')]")))
                    #connect with the candidate
                    connect = driver.find_element_by_xpath("//div[@class='pvs-profile-actions ']//span[contains(.,'Connect')]").click()
                    wait = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Add a note')]")))
                    #add a note
                    add_note = driver.find_element_by_xpath("//span[contains(.,'Add a note')]").click()
                    wait = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//textarea")))
                    #write the note
                    note = driver.find_element_by_xpath("//textarea")
                    #################

                    note.send_keys(message)

                    wait = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Send now']")))
                    #send the note
                    send_note = driver.find_element_by_xpath("//button[@aria-label='Send now']").click()
                except: #not sure if i should implement sending message for those who do not want to connect
                    try:
                        wait = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "(//button[@aria-label='More actions'])[2]")))
                        #press MORE
                        connect = driver.find_element_by_xpath("(//button[@aria-label='More actions'])[2]").click()

                        wait = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, f"//span[contains(.,'Invite {profiles.iloc[profile,0]} to connect')]")))
                        #press Connect
                        connect = driver.find_element_by_xpath(f"//span[contains(.,'Invite {profiles.iloc[profile,0]} to connect')]").click()

                        wait = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "(//button[contains(.,'Connect')])[1]")))
                        #press Message
                        connect = driver.find_element_by_xpath("(//button[contains(.,'Connect')])[1]").click()

                        #add a note
                        wait = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Add a note')]")))
                        add_note = driver.find_element_by_xpath("//button[contains(.,'Add a note')]").click()

                        #write the message
                        wait = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//textarea")))
                        note = driver.find_element_by_xpath("//textarea").send_keys(message)

                        wait = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Send')]")))
                        #send the message
                        send_note = driver.find_element_by_xpath("//button[contains(.,'Send')]").click()
                    except:
                        pass


                wanted_candidates.loc[len(wanted_candidates)] = [profiles['name'][profile], public_profile]

    wanted_candidates.to_excel(f'{prj_title}_wanted_candidates.xlsx', index=False)
    return wanted_candidates

if __name__ == '__main__':
    emailas = input('Enter your email: ')
    passwordas = input('Enter your password: ')
    prj_title = input('Enter project title: ')
    job_titles = input('Enter job titles: (leave empty & enter if not needed) ')
    locations = input('Enter location: (leave empty & enter if not needed) ')
    workplace_types = input('Enter workplace types: (leave empty & enter if not needed) ')
    skills = input('Enter skills: (separate by comma) ')
    companies = input('Enter companies: (separate by comma) ')
    schools = input('Enter schools: (separate by comma) ')
    year_of_graduation = input('Enter year of graduation: (Ex: 2008-2012) ')
    industries = input('Enter industries: (separate by comma) ')
    keywords = input('Enter keywords: (separate by comma) ')
    seniority = input('Enter seniority: (leave empty & enter if not needed) ')

    message = input('''Enter message:''')
    #open chrome
    driver = webdriver.Chrome()

    #all names & urls of profiles
    profiles = LinkedIn_filter(driver, prj_title, job_titles, locations, workplace_types, skills, companies, schools,
                               year_of_graduation, industries, keywords, seniority)

    wanted_candidates = advanced_filter(pd.read_excel(f'{prj_title}_all_contacts.xlsx'), message)

    driver.quit()