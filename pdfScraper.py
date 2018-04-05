#######################################
# Name: pdfScraper.py
#
# Description: Scrapes webpage for pdf 
# files and saves them to the directory
#
#######################################

from bs4 import BeautifulSoup
import requests

# homepage url
url = "https://www.ma.utexas.edu/users/mcudina/course2.html"

# package request
r = requests.get(url)

# get html doc from request
html_doc = r.text

# use bs4 to parse
soup = BeautifulSoup(html_doc, "html.parser")

# get all <a> tags
a_tags = soup.find_all("a")

# check if <a> contains pdf and downloads
for link in a_tags:
    s = link.get("href")
    try:
        # check if .pdf extension
        if s.endswith(".pdf"):

            # check if href is not local or not
            if s.startswith("http://"):
                file_request = requests.get(s, stream=True)
                with open(s.split("/")[-1], "wb") as f:
                    f.write(file_request.content)
            else:
                file_request = requests.get("/".join(url.split("/")[:-1]) + "/" + s, stream=True)
                with open(s.split("/")[-1], "wb") as f:
                    f.write(file_request.content)
            print("Successfully downloaded " + s.split("/")[-1])

    # lazy error handling
    except Exception as e:
        print("\tError: " + str(e))
        
print("Finished.")
