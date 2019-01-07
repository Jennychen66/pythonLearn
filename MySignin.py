#how to import chrome driver and open the url for you to test: http://chromedriver.chromium.org/getting-started

# I met the error when it is saying : can't find module selenium :
# go to this pycharm's terminal console , run command pip3 install selenium
# After successful installed
# go to python console, run command : from selenium import webdriver , if it is successful , then perfect
# stackoverflow : https://stackoverflow.com/questions/31147660/importerror-no-module-named-selenium


# CSS locator : https://saucelabs.com/resources/articles/selenium-tips-css-selectors
# https://selenium-python.readthedocs.io/locating-elements.html 
# https://www.testingexcellence.com/css-selectors-selenium-webdriver/

# how to stop the drop drow menu close automatically when click on the outside of the window : https://zhuanlan.zhihu.com/p/39947469

from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\JennyChen\ADAS\chromedriver.exe')


#url = "https://inside.dell.com/groups/chinacoe/projects/social-clubs/content?filterID=contentstatus[published]~objecttype~objecttype[event]~event[upcoming]&query=yoga&sortKey=contentstatus[published]~subjectAsc&sortOrder=1"

url = "https://inside.dell.com/groups/chinacoe/projects/social-clubs/content";
driver.get(url);
filterTab = driver.find_element_by_css_selector('span.j-filter-btn-inner.j-ui-elem');
filterTab.click();
time.sleep(10);
filterInputId = driver.find_element_by_css_selector('input#tag-filter-input');
filterAriaId = filterInputId.get_attribute('aria-owns');
finalFilterAria = "div#" + filterAriaId +".j-pop.js-pop.j-autocomplete.popover";
tagSelector = driver.find_element_by_css_selector(finalFilterAria)
tagSelector.find_element_by_css_selector('#popular-tags > li:nth-child(1)').click()
#select = Select(tagSelector)
#select.select_by_visible_text('yoga')
#selenium.common.exceptions.UnexpectedTagNameException: Message: Select only works on <select> elements, not on <div>
driver.find_element_by_css_selector('#j-browse-filters > div.j-browse-sorts.j-browse-filter-row.last-child').click()


#tagSelector.select_by_value('yoga')

TimeSelector = driver.find_element_by_css_selector('select#j-sort')
select = Select(TimeSelector)
TimeSelectorSel = select.select_by_visible_text('Sort by date created: newest first')

time.sleep(5)


thisEle = driver.find_element_by_xpath('//*[@id="j-browse-item-grid"]/ul/li')
thisEle.find_element_by_css_selector('header > h4').click()
time.sleep(10)
#canlenderUrl = "https://inside.dell.com/events/28253"
#driver.get(canlenderUrl)
ele = driver.find_element_by_css_selector('a.noprint.js-add-comment')
ele.click()
                                               
inputEle = driver.find_element_by_css_selector('form.j-comment-form')
time.sleep(10)

#typeKey.click()
keyVal = "Jenny.Chen@emc.com"
typeKey = inputEle.find_element_by_xpath('//*[@id="wysiwyg_id_0_ifr"]')
typeKey.click()
for x in keyVal:
    typeKey.sendKeys(x)

#await typeKey.send_keys('Jenny.Chen@emc.com', Key.RETURN);
#driver.getkeyboard().sendKeys("Jenny.Chen@emc.com")

#String str="Sunday"; driver.findElement(By.id("0_4")).click(); for(int i=0; i<str.length(); i++){ driver.findElement(By.id("0_4")).sendKeys(String.valueOf(str.charAt(i)));


# sport = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="wysiwyg_id_0_ifr"]')))
# sport.click()



#typeKey.send_keys('dddeeffef')





submitButton = inputEle.find_element_by_css_selector('input.j-btn-callout')
submitButton.click()
#elements = driver.find_element(By.XPATH, '//ul//li//header[@class="js-thumb-header"]')
text = "ttr"
#Jenny.Chen@emc.com
