import requests
import re
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find("div",class_="title").find("a")["title"]
    company = html.find("span",class_="company")
    if(company is None):
        company = "No Information"
    else:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
        company = company.strip()
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title': title, 
        'company': company, 
        'location': location, 
        'link':f"https://www.indeed.com/viewjob?jk={job_id}"
        }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed: Page: {page}")
        result = requests.get(f"{URL}&start={0*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",class_="jobsearch-SerpJobCard")
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs