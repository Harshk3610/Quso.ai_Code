from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Setup WebDriver
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  # Keep browser open after script ends
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

# Replace with your email and password
email = "vikram0812+niit@proton.me"
password = "NIIT@2024"

try:
    # Step 1: Load the website
    driver.get("https://quso.ai/")
    logger.info("Website loaded!")

    # Step 2: Click on the Login link
    wait = WebDriverWait(driver, 30)
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/auth/login')]")))
    login_link.click()
    logger.info("Login link clicked!")

    # Step 3: Click on "Continue with Email" button
    email_button = wait.until(EC.element_to_be_clickable((By.ID, "auth-email-password-btn")))
    email_button.click()
    logger.info("Continue with Email clicked!")

    # Step 4: Enter Email and Password
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))  # Adjust if necessary
    password_input = driver.find_element(By.ID, "password")  # Adjust if necessary

    email_input.send_keys(email)
    password_input.send_keys(password)
    logger.info("Email and password entered!")

    # Step 5: Submit the login form (or click login button if needed)
    password_input.send_keys(Keys.RETURN)  # Submit the form using the RETURN key
    logger.info("Login submitted!")

    # Step 6: Navigate to the "AI Video Generator" tile
    video_tile = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'AI Video Generator')]")))
    video_tile.click()
    logger.info("AI Video Generator tile clicked!")

    # Step 7: Generate an AI Script
    generate_script_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate Script')]")))
    generate_script_button.click()
    logger.info("AI Script generation started!")

    # Step 8: Proceed to generate the video
    generate_video_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate Video')]")))
    generate_video_button.click()
    logger.info("Video generation started!")

    # Step 9: Wait for video generation to complete and download it
    download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Download Video')]")))
    download_button.click()
    logger.info("Video downloaded successfully!")

    # Add delay to observe the download completion (if needed)
    time.sleep(10)

except TimeoutException as e:
    logger.error(f"Timeout occurred: {str(e)}")
except NoSuchElementException as e:
    logger.error(f"Element not found: {str(e)}")
except Exception as e:
    logger.error(f"Unexpected error: {str(e)}")

finally:
    driver.quit()
    logger.info("Browser closed.")
