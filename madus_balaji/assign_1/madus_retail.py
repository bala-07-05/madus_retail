import time
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

driver.find_element(By.ID, "LINK").click()
driver.find_element(By.ID, "MainContent_M_DisplayPageNavigationControl_MoDataList_HyperLink1_2").click()
driver.find_element(By.LINK_TEXT,"3").click()
time.sleep(3)
driver.find_element(By.ID, "MainContent_ModuleSubModule_grdModule_btnViewLevel_4").click()

driver.find_element(By.ID,"MainContent_ModuleSubModule_btnAddNew").click()
time.sleep(3)
driver.find_element(By.ID, "MainContent_ModuleSubModule_txtName").send_keys("Test Automated Value Chain (qwe)")

dropdown = Select(driver.find_element(By.ID,"MainContent_ModuleSubModule_ddlSelectModuleGroup"))
dropdown_selection = dropdown.select_by_visible_text("Modus QA Group")
driver.find_element(By.NAME,"ctl00$MainContent$ModuleSubModule$btnOkay").click()
time.sleep(3)

list_of_values = driver.find_elements(By.CSS_SELECTOR, '.jtree_parent_node.jtree_parent_node_display.TeamList')
elements = driver.find_elements(By.CSS_SELECTOR, '.jtree_expand.jtree_node_close')
elements[2].click()
elements[3].click()
radio_buttons = driver.find_elements(By.NAME, "PermissionSets3")
radio_buttons[1].click()
driver.find_element(By.ID, "BtnSave_SubModulePermissionMapping UHAllbuttonColors").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
driver.find_element(By.ID, "btnSaveSubModuleFeatureMapping").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()

dropdown = Select(driver.find_element(By.ID,"DdlRoleValues"))
dropdown.select_by_visible_text("Business Role")
driver.find_element(By.ID, "btnSaveFeatureRolePermissionMapping").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)
driver.close()
