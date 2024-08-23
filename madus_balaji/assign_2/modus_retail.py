import time
from select import select
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Edge(executable_path="//Users//balaj//Downloads//edgedriver_arm64//msedgedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://modusretail.azurewebsites.net/Pages/Hierarchy/home.aspx")
wait_for_webpage = True
while (wait_for_webpage):
    try:
        if (driver.find_element(By.ID, 'idSIButton9') is None): # If webpage is not loaded
            time.sleep(1)
            wait_for_webpage = True
        else: # If webpage is loaded
            time.sleep(1)
            wait_for_webpage = False
    except:
        wait_for_webpage = True

driver.find_element(By.ID,"i0116").send_keys("QA-Assignment@outlook.com")
driver.find_element(By.ID, 'idSIButton9').click()
time.sleep(5)

driver.find_element(By.ID,"i0118").send_keys("qa-assign10")
driver.find_element(By.ID, 'idSIButton9').click()
time.sleep(3)
driver.find_element(By.ID, 'declineButton').click()
driver.find_element(By.ID, "MainContent_M_HomeControl_dtlist1_hypModule1_1").click()
driver.find_element(By.XPATH, "//*[@id='s4-bodyContainer']/div[3]/div[2]/div[1]/ul/li[3]/a").click()
driver.find_element(By.ID, "MainContent_M_SubModulesControl1_rptAccordianContent_dtlist_2_hypModule_34").click()

driver.find_element(By.XPATH, "//*[@id='btnAddNew']").click()
driver.find_element(By.ID,"txtHeaderTitle").send_keys("assignment2")
driver.find_element(By.XPATH, "//*[@id='btnSave']/span[2]").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()

driver.find_element(By.ID,"btnAddNewLevelZero").click()
driver.find_element(By.ID,"txtTitle").send_keys("Test Automated Level Zero C1")
driver.find_element(By.ID,"txtDescription").send_keys("Description L0 C1")
driver.find_element(By.ID,"chk").click()

dropdown = Select(driver.find_element(By.ID,"selectProcessHeaderLevelZero"))
dropdown_selection = dropdown.select_by_visible_text("assignment2")
save = driver.find_elements(By.XPATH,"//*[@id='btnSave']/span[2]")
save[1].click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()

driver.find_element(By.ID,"btnAddNewLevelOne").click()
driver.find_element(By.ID,"txtTitleLevelOne").send_keys("Test Automated Level One C1")
driver.find_element(By.ID,"txtDescriptionLevelOne").send_keys("Description L1 C1")
driver.find_element(By.ID,"txtShortDescriptionLevelOne").send_keys("L1A")

# Team selection
button_for_dropdown = driver.find_element(By.XPATH,"//*[@id='divAddNewLevelOne']/div/div/div[2]/div/div/div[1]/div[6]/div[2]/span/span/div/button")
button_for_dropdown.click()
aa_lists = driver.find_elements(By.CSS_SELECTOR, ".checkbox")
#for aa in aa_lists:
    #print("button displayed? ", str(aa.is_displayed()))
    #print("button selected ? ", str(aa.is_selected()))
    #print("button enabled ? ", str(aa.is_enabled()))
aa = aa_lists[-2]
aa.click()
button_for_dropdown.click()

## Department Selection
button_for_dropdown = driver.find_element(By.XPATH,"//button[@title='Select Department']")
button_for_dropdown.click()
aa_lists = driver.find_elements(By.CSS_SELECTOR, ".checkbox")
'''
for aa in aa_lists:
    print("button displayed? ", str(aa.is_displayed()))
    print("button selected ? ", str(aa.is_selected()))
    print("button enabled ? ", str(aa.is_enabled()))
'''
aa = aa_lists[-1]
aa.click()
button_for_dropdown.click()


## Role Selection
button_for_dropdown = driver.find_element(By.XPATH,"//button[@title='Select Role']")
button_for_dropdown.click()
aa_lists = driver.find_elements(By.CSS_SELECTOR, ".checkbox")
'''
for aa in aa_lists:
    print("button displayed? ", str(aa.is_displayed()))
    print("button selected ? ", str(aa.is_selected()))
    print("button enabled ? ", str(aa.is_enabled()))
'''
aa = aa_lists[-1]
aa.click()
button_for_dropdown.click()

driver.find_element(By.ID,"chkLevelOne").click()
dropdown = Select(driver.find_element(By.ID,"DdlProcessHeaders"))
dropdown.select_by_visible_text("assignment2")
driver.find_element(By.ID,"btnSaveLevelOne").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)
driver.close()

