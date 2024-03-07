import requests
from bs4 import BeautifulSoup

def search_soft_skills(keyword):
    url = f"https://www.saramin.co.kr/zf_user/jobs/relay/view-list?search_key=0&search_optional_item=n&search_done=y&panel_count=y&rec_idx=&sort=RL&type=list&searchword={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []

    job_items = soup.select('.part_top .list_default li')
    for job_item in job_items:
        title = job_item.select_one('.job_tit a').text.strip()
        company = job_item.select_one('.part_top .company_name .company').text.strip()
        location = job_item.select_one('.job_condition .work_place').text.strip()
        skills = job_item.select_one('.job_condition .condition').text.strip()
        link = job_item.select_one('.job_tit a')['href']
        results.append({
            'title': title,
            'company': company,
            'location': location,
            'skills': skills,
            'link': link
        })

    return results

def print_results(results):
    for idx, result in enumerate(results, start=1):
        print(f"Job #{idx}")
        print(f"Title: {result['title']}")
        print(f"Company: {result['company']}")
        print(f"Location: {result['location']}")
        print(f"Skills: {result['skills']}")
        print(f"Link: {result['link']}")
        print()

def main():
    keyword = input("Enter a keyword to search for soft skills: ")
    results = search_soft_skills(keyword)
    print(f"Found {len(results)} job postings related to {keyword}:")
    print_results(results)

if __name__ == "__main__":
    main()