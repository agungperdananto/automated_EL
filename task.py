import local_settings as settings
from selenium import webdriver


driver = webdriver.Chrome()


def login(username, password):
    driver.get(settings.LOGIN_URL)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_css_selector('.btn.btn-primary').click()

    if driver.find_elements_by_css_selector('.userpicture.defaultuserpic'):
        return
    else:
        raise ('LOGIN FAILED')


def define_forum(course, week):
    driver.get(settings.COURSE_URL.format(course, week))
    forum_element = driver.find_elements_by_css_selector('.activity.forum.modtype_forum')[week]
    forum_id = forum_element.get_attribute('id')[7:]
    return forum_id


def create_forum(course, week):
    forum_id = define_forum(course, week)
    for forum_count in range(8):
        driver.get(settings.FORUM_URL.format(forum_id))
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Tambah topik diskusi baru')]")
        buttons[0].click()
        driver.find_element_by_id('id_subject').send_keys('forum', '3-'+str(forum_count))
        driver.find_element_by_id('id_messageeditable').send_keys(settings.FORUM_QUESTIONS[forum_count])
        driver.find_element_by_id('id_submitbutton').click()


def create_forum_per_week(courses, week):
    for course in courses:
        create_forum(course, week)


def coment_in_forum_per_week(courses, week, comment):
    for course in courses:
        create_forum_coments(course, week, comment)


def create_forum_coments(course, week, message):
    forum_id = define_forum(course, week)
    driver.get(settings.FORUM_URL.format(forum_id))
    element_text = "//*[contains(text(), 'forum{}')]".format(week)
    forum_url_elements = driver.find_elements_by_xpath(element_text)
    forum_urls = [forum_url_element.get_attribute('href') for forum_url_element in forum_url_elements]
    for forum_url in forum_urls:
        driver.get(forum_url)
        reply_urls = driver.find_elements_by_xpath("//*[contains(text(), 'Tanggapi')]")
        reply_url = reply_urls[0].get_attribute('href')
        driver.get(reply_url)
        driver.find_element_by_id('id_messageeditable').send_keys(message)
        driver.find_element_by_id('id_submitbutton').click()
