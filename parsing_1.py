import time
from selenium import webdriver
from CurrentPageSoup import CurrentPageSoup
from CurrentPageSplit import CurrentPageSplit

driver = webdriver.Firefox(executable_path='/Users/mitmac/Desktop/Dmitry/Python/Parse/Firefox/geckodriver')
driver.get('https://pub.fsa.gov.ru/ral')

#  Обозначим кнопку
input('Подождите загрузки страницы и нажмите Enter ')
button = driver.find_element_by_xpath("/html/body/fgis-root/div/fgis-ral/fgis-ral-table-view/div/div/div[3]/fgis-table-paging/div/div[2]/div[2]/div/span[3]")
input('Выставьте все необходимые настройки фильтра и нажмите Enter ')

total = driver.find_element_by_xpath("/html/body/fgis-root/div/fgis-ral/fgis-ral-table-view/div/div/div[3]/fgis-table-paging/div/div[1]/div[2]").text
data = total.split()
n = int(data[-1])
input('Найдено записей: ' + str(n) + '. Нажмите Enter, чтобы начать запись данных')

for i in range(0, round(n // 10 + 1)):

    #  Получим дату с этой страницы и образуем лист со всеми данными
    code_html = CurrentPageSoup(driver)

    # Теперь необходимо правильно поделить список на несколько частей и сохранить его
    final = CurrentPageSplit(code_html)

    # Перейдем на следующую страницу и повторим наши шаги
    button.click()

    # Подождем загрузки страницы
    time.sleep(4)

input('Программа выполнена. Нажмите Enter ')

driver.quit()
