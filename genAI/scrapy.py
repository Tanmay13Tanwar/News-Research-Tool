from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from langchain_community.document_loaders import UnstructuredHTMLLoader




url = 'https://realpython.com/python-web-scraping-practical-introduction/'
path = "D:\chromedriver\chromedriver.exe"

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up the Chrome driver service
service = Service(path)

# Initialize the WebDriver with options and service
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set a timeout for loading the page
timeout = 30  # seconds

try:
    driver.set_page_load_timeout(timeout)
    driver.get(url)
    # Optional: Wait until a specific element is loaded (replace with an actual element selector)
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "main-content")))
    print("Page loaded successfully")
except TimeoutException:
    print(f"Page load timed out after {timeout} seconds")

# Scrape the whole page content
page_content = driver.page_source

# Print the page content
'''try:
    print(page_content)
except UnicodeEncodeError:
    print(page_content.encode('utf-8').decode('utf-8'))'''

# Close the driver
driver.quit()

# Optional: Save the content to a file
with open("page_content.html", "w", encoding="utf-8") as file:
    file.write(page_content)

file.close()

path = "page_content.html"

print("content written")
loader = UnstructuredHTMLLoader(path)
print("loader created")
data = loader.load()
print("Data loaded")
data
