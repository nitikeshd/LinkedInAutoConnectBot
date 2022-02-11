from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from mail import mail

#get it from browserstack.com
def getDriver():
    desired_cap = {'os': 'Windows', 'os_version': '10', 'browser': 'Chrome', 'browser_version': '57.0' }
    return webdriver.Remote(command_executor='http://*************:**************@hub.browserstack.com:80/wd/hub', desired_capabilities=desired_cap)
def linkedinLogin(driver):
    driver.get('https://www.linkedin.com/login')
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys("****YOUR_USERNAME*****")
    password.send_keys("****YOUR_PASSWORD*****")
    driver.find_element_by_tag_name("button").click()
    time.sleep(5)
def checkOTP(driver):
    code=mail().getCode()
    try:
        pin=driver.find_element_by_name("pin")
        pin.send_keys(code)
        driver.find_element_by_id("email-pin-submit-button").click()
    except:
        pass
    finally:
        executeBot(driver)
def executeBot(driver):
    driver.get('https://www.linkedin.com/mynetwork/')
    driver.execute_script('async function moreConnectionsPlease(){const n=600,o=15,e=300,t=10;var c,l=0,s=0;function i(){return[...document.querySelectorAll("button span")].filter(n=>n.textContent.includes("Connect"))}async function r(){return new Promise(o=>{setTimeout(()=>{window.scrollTo(0,document.body.scrollHeight),console.log("scroll!"),o()},n)})}async function a(n){return new Promise(o=>{setTimeout(()=>{n.click(),o()},e)})}async function u(){for(let n=0;n<o;n++)await r()}async function f(){let n=i();console.log("elements length:",n.length);for(let o=0;o<n.length-t;o++)try{await a(n[o]),console.log("click!"),l++}catch(n){s++}}do{c=60,i().length>=c?(console.log("There are plenty of connections, time to click..."),await f()):(console.log("Out of connections, need to scroll..."),await u()),console.log(`New Connections:${l} Failed clicks:${s}`)}while(l<500)}moreConnectionsPlease();')
    
driver = getDriver()
#Step - 1 : Login
linkedinLogin(driver)
#Step 2 : Check OTP
#checkOTP(driver)
#Now Linked in has removed OTP Auth for some caseds. So use it at your own convinient.
executeBot(driver)
#Step 3 : Run BOT
