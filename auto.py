import time
from selenium import webdriver
from get_text import get_text

def auto():
    # 웹드라이버 생성
    driver = webdriver.Chrome('C:/Users/bsm7878/Desktop/chromedriver_win32/chromedriver')
    driver.implicitly_wait(3)

    # url 접근
    driver.implicitly_wait(10)
    url = 'https://center-pf.kakao.com/_llBmK/messages/new/feed'
    driver.get(url)

    # 아이디 입력
    time.sleep(2)
    driver.find_element_by_id('id_email_2').send_keys('bsm7878@naver.com')
    driver.implicitly_wait(10)

    # 비번 입력
    time.sleep(2)
    driver.find_element_by_id('id_password_3').send_keys('')
    driver.implicitly_wait(10)

    # 로그인 버튼 클릭
    time.sleep(1)
    driver.find_element_by_class_name('submit').click()
    driver.implicitly_wait(10)

    # 닫기 버튼 클릭
    time.sleep(5)
    driver.find_element_by_class_name('link_close').click()
    driver.implicitly_wait(10)

    # 텍스트 입력
    time.sleep(5)
    driver.find_element_by_id('messageWrite').send_keys(get_text())
    driver.implicitly_wait(10)

    # 다음 클릭
    time.sleep(5)
    driver.find_element_by_class_name('btn_g2').click()
    driver.implicitly_wait(10)

    # 발송하기 클릭
    time.sleep(3)
    driver.find_element_by_class_name('btn_g2').click()
    driver.implicitly_wait(10)

    # 최종 확인
    time.sleep(3)
    driver.find_element_by_css_selector('.layer_body > .wrap_btn > .btn_g2').click()

    # 드라이버 종료
    driver.close()


if __name__ == "__main__":
    auto()