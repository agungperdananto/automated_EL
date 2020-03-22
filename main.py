from selenium import webdriver
from settings import (
    COURSE_IDS,
    COURSE_URL,
    FORUM_QUESTIONS,
    FORUM_URL,
    LOGIN_URL,
    PASSWORD,
    USERNAME)

driver = webdriver.Chrome()


def login(username, password):
    driver.get(LOGIN_URL)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_css_selector('.btn.btn-primary').click()

    if driver.find_elements_by_css_selector('.userpicture.defaultuserpic'):
        print('LOGIN SUCCESS')
    else:
        print('FAILED LOGIN')


def filling_forum(FORUM_QUESTIONS, course, week):
    driver.get(COURSE_URL.format(course, 3))
    forum_element = driver.find_elements_by_css_selector('.activity.forum.modtype_forum')[3]
    forum_id = forum_element.get_attribute('id')[7:]
    for forum_count in range(8):
        driver.get(FORUM_URL.format(forum_id))
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Tambah topik diskusi baru')]")
        buttons[0].click()
        driver.find_element_by_id('id_subject').send_keys('forum', '3-'+str(forum_count))
        driver.find_element_by_id('id_messageeditable').send_keys(FORUM_QUESTIONS[forum_count])
        driver.find_element_by_id('id_submitbutton').click()


def all_course_task(courses, week):
    for course in courses:
        filling_forum(FORUM_QUESTIONS, course, week)


login(USERNAME, PASSWORD)
all_course_task(COURSE_IDS, 3)
