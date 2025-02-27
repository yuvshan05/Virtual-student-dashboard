import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)  # Increased explicit wait time

def capture_screenshot(name):
    """Captures a screenshot if an error occurs."""
    driver.save_screenshot(f"{name}.png")
    print(f"📸 Screenshot saved as {name}.png")

try:
    # **Step 1: Signup**
    print("🔹 Navigating to Signup Page...")
    driver.get("http://localhost:5173/signup")

    print("🔹 Entering Signup Details...")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='fullName']"))).send_keys("yuvraja")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='email']"))).send_keys("yuvrajasz@thapar.edu")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='password']"))).send_keys("yuvrajhero")

    print("🔹 Clicking Create Account...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/section/form/button"))).click()
    time.sleep(3)  # Allow time for account creation

    # **Step 2: Logout**
    print("🔹 Opening Profile Menu for Logout...")
    profile_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/div/div[1]/label")))
    profile_menu.click()
    
    print("🔹 Clicking Logout Button...")
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/div/div[2]/ul/li[6]/div/button[2]/a")))
    logout_button.click()
    time.sleep(3)  # Buffer time after logout

    # **Step 3: Login**
    print("🔹 Navigating to Login Page...")
    driver.get("http://localhost:5173/login")
    wait = WebDriverWait(driver, 15)  # Increased wait time

    print("🔹 Entering Login Details...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/section/form/div[1]/input"))).send_keys("yuvraj@thapar.edu")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/section/form/div[2]/input"))).send_keys("yuvrajhero")

    print("🔹 Clicking Login Button...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/section/form/button"))).click()
    time.sleep(5)  # Allow login process to complete

    # **Step 4: Verify Home Page Loaded**
    try:
        dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/main/nav")))
        print("🎉✅ Login Successful! Navigated to Home Page.")
    except:
        print("❌ Login Failed. Dashboard element not found.")
        driver.quit()
        exit()

    # **Step 5: Navigate to Explore Courses**
    print("🔹 Navigating to Explore Courses...")
    explore_courses_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/section/div[1]/div/a[1]/button")))
    explore_courses_btn.click()
    time.sleep(5)  # Allow page to load

    # **Step 6: Click on Target Button in Explore Page**
    print("🔹 Clicking on Target Button in Explore Page...")
    target_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/main/section/div/div/div[2]")))
    target_button.click()
    print("🎯✅ Clicked the button on 'Explore Courses' Page.")

    print("✅ Automation Completed Successfully!")
    time.sleep(5)  # Wait for observation

except Exception as e:
    print(f"❌ Error Occurred: {e}")
    capture_screenshot("error_step")  # Capture screenshot on failure

finally:
    input("Press Enter to close the browser...")
    driver.quit()
