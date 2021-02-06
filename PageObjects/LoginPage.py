class LoginPage:
    txtUsername_id = "Email"
    txtPassword_id = "Password"
    btnLogin_xpath = "//*[@type='submit']"
    linkLogout_link_text_ = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.txtUsername_id).clear()
        self.driver.find_element_by_id(self.txtUsername_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txtPassword_id).clear()
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.btnLogin_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.linkLogout_link_text_).click()
