from selenium import webdriver

# 크롬 드라이버 경로 설정
driver_path = '크롬 드라이버 경로를 입력하세요'
driver = webdriver.Chrome(driver_path)

# URL 열기
driver.get('https://www.compuzone.co.kr/login/login.htm')

# id와 password 입력하기
id_input = driver.find_element_by_name('id')
password_input = driver.find_element_by_name('passwd')
id_input.send_keys('아이디를 입력하세요')
password_input.send_keys('패스워드를 입력하세요')

# 로그인 버튼 클릭
login_button = driver.find_element_by_class_name('btn_login')
login_button.click()

# 브라우저 종료
driver.quit()
