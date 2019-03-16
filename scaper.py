from selenium import webdriver
import time
import codecs
def get_name(drive):
    elem = drive.find_element_by_class_name("boxList").find_element_by_tag_name("strong")
    return elem.text
def get_name_test():
    # Should return 'Visibility'
    url="http://www.mto.gov.on.ca/english/handbook/motorcycles/section4-2-0.shtml"
    executable_path="chrome/chromedriver"
    driver=webdriver.Chrome(executable_path=executable_path)
    driver.get(url)
    time.sleep(1)
    print(get_name(driver))
    driver.close()
#get_name_test()
def get_page_source(drive, index):
    html = drive.page_source
    name = get_name(drive)
    file_object = codecs.open(str(index) + ") " + name + ".html", "w", "utf-8")
    file_object.write(html)
def get_page_source_test():
	# Do not forget to delete file before running the main loop
    index = 100
    url="http://www.mto.gov.on.ca/english/handbook/motorcycles/section4-2-4.shtml"
    executable_path="chrome/chromedriver"
    driver=webdriver.Chrome(executable_path=executable_path)
    driver.get(url)
    time.sleep(1)
    get_page_source(driver,index)
    driver.close()
#get_page_source_test()

def scrape_motorocycle_handbook():
	# If stopped because of an error need to change 2 lines below
    index = 0
    url = "http://www.mto.gov.on.ca/english/handbook/motorcycles/index.shtml"
    executable_path = "chrome/chromedriver"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get(url)
    time.sleep(2)
    get_page_source(driver, index)
    while True:
        # Will throw an error in the end, because there would be no "Next" button
        index+=1
        driver.find_element_by_class_name("next_handbook").find_element_by_tag_name("img").click()
        time.sleep(2)
        get_page_source(driver,index)
scrape_motorocycle_handbook()