# Varzesh3.com surveillance system
## **Introduction**
This Python script is a web scraping tool designed to monitor the Varzesh3 website for new news articles and download associated images. It uses threading to ensure continuous monitoring and downloading without interruption. Here's an overview of its functionality:
## Key Features
**1. Continuous News Monitoring:**

- The script continuously fetches the main news page of the Varzesh3 website every 30 seconds.
- It identifies new links to articles by comparing them with previously processed links.

**2. Image Downloading:**

- For each new article, the script extracts the images displayed in the "news-main-image" section of the page.
- These images are downloaded and saved to a local folder (downloaded_images).

**3. Threaded Processing:**

- The script uses Python's threading module to simultaneously monitor the website and download images without blocking.

**4. Error Handling:**

- Gracefully handles errors, such as network issues or invalid URLs, ensuring the script continues running.

## **Setup Instructions**
### Follow these steps to set up and run the project on your system:

#### 1. Create and Activate a Virtual Environment
Run the following commands in your terminal to create and activate a virtual environment (Windows)
```
python -m venv .venv
.\.venv\scripts\activate
```
#### 2. Install Required Dependencies
Install all the required libraries by running the command below:
```
pip install -r req.txt
```
Ensure your req.txt file contains the following:
```
requests
beautifulsoup4
lxml
```
#### 3. Run the Script
Start the script with the following command:
```
python varzesh3.py
```

## **Execution Details**
Once the script is executed, it will:
- Continuously fetch the main page of the Varzesh3 website to look for new article links.
- Compare newly found links with previously processed ones to avoid duplication.
- For each new link, it will download associated images and save them to the `downloaded_images` folder.
- This process runs indefinitely, ensuring the latest articles and their images are always captured.

