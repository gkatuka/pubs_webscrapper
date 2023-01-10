#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:30:28 2022

@author: gloriakatuka
"""

import sys
import urllib3
import requests
import pandas as pd
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# pip install chromedriver-autoinstaller
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def search_anySearchLink():
    #databases 
    dbDict = {
    'ACMurl':"https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&field1=AllField&text1=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28“human-human”%29NOT+Agent+",
    'IEEEurl':"https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=(Conversat*%20OR%20dialog*)%20AND%20(acts%20OR%20moves%20OR%20Schema%20OR%20Annotation%20OR%20classification%20OR%20Taxonomy)%20AND%20(“human-human”)%20NOT%20Agent",
    'SDurl':"https://www.sciencedirect.com/search?tak=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29&qs=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29%20AND%20%22human-human%22%20Not%20agent",
   'Wileyurl':"https://onlinelibrary.wiley.com/action/doSearch?field1=AllField&text1=%28convers*%2BOR%2Bdialog*%29%2BAND%2B%28acts%2BOR%2Bmoves%2BOR%2BSchema%2BOR%2BAnnotation%2BOR%2Bclassification%2BOR%2BTaxonomy%29%2BAND%2B%22human-human%22%2BNOT&Ppub=",
    'Springerurl':"https://link.springer.com/search?query=%28Conversation*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28%E2%80%9Chuman-human%E2%80%9D%29++NOT+agent&facet-content-type=%22Article%22",
    'islsurl':"https://repository.isls.org/simple-search?location=%2F&query=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+OR+%22human-human%22+NOT+Agent+&rpp=10&sort_by=score&order=desc#"
        }
    urlList = ["https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&field1=AllField&text1=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28“human-human”%29NOT+Agent+",
    "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=(Conversat*%20OR%20dialog*)%20AND%20(acts%20OR%20moves%20OR%20Schema%20OR%20Annotation%20OR%20classification%20OR%20Taxonomy)%20AND%20(“human-human”)%20NOT%20Agent",
    "https://www.sciencedirect.com/search?tak=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29&qs=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29%20AND%20%22human-human%22%20Not%20agent",
    "https://onlinelibrary.wiley.com/action/doSearch?field1=AllField&text1=%28convers*%2BOR%2Bdialog*%29%2BAND%2B%28acts%2BOR%2Bmoves%2BOR%2BSchema%2BOR%2BAnnotation%2BOR%2Bclassification%2BOR%2BTaxonomy%29%2BAND%2B%22human-human%22%2BNOT&Ppub=",
    "https://link.springer.com/search?query=%28Conversation*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28%E2%80%9Chuman-human%E2%80%9D%29++NOT+agent&facet-content-type=%22Article%22",
    "https://repository.isls.org/simple-search?location=%2F&query=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+OR+%22human-human%22+NOT+Agent+&rpp=10&sort_by=score&order=desc#"]
    
    driver = webdriver.Chrome()
    paper_names = []
    paper_types = []
    papers_pubDate = []
    papers_proc = []
    papers_pdfLink = []
    
    
    #ACM 
    page_no = 0
    page_size = 0
    acm_papers_title = []
    acm_papers_type = []
    acm_papers_pubDate = []
    acm_papers_proc = []
    acm_papers_pdfLink = []
    
    while (page_no <= 14):        
        url = f"https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&field1=AllField&text1=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28“human-human”%29NOT+Agent+&startPage={page_no}&pageSize=50"
        driver.get(url)
        wait = WebDriverWait(driver,10)    
        page_content = driver.page_source
        soup= BeautifulSoup(page_content,'html.parser')
        paper_names_search = soup.find_all('h5',class_='issue-item__title')
        paper_type_search = soup.find_all('div',class_='issue-heading')
        paper_pubDate_search = soup.find_all('div',class_='bookPubDate simple-tooltip__block--b')
        paper_proc_search = soup.find_all('div',class_='issue-item__detail')
        # paper_pdfLink_search = soup.find_all('div',class_='issue-item__detail')
        
        # paper_years_search = soup.find!_all('div',attrs={'class','bookPubDate'})
        # paper_years_search = soup.find_all('div',attrs={'class','bookPubDate'})
        # paper_authors_search = soup.find_all
        # paper_cite_search = 
        # paper_pdflink_search = 
        # papers_proceedings_search = soup.find_all
      
        for pn in paper_names_search:
            acm_papers_title.append(pn.getText())
            paper_names.append(pn.getText())
            
        for pt in paper_type_search:
            acm_papers_type.append(pt.getText())
            paper_types.append(pt.getText())   
            
        for ppd in paper_pubDate_search:
            acm_papers_pubDate.append(ppd.getText())
            papers_pubDate.append(ppd.getText()) 
            
        for pro in paper_proc_search:
            acm_papers_proc.append(pro.getText())
            papers_proc.append(pro.getText()) 
        
        
        # for lk in paper_pdfLink_search:
        #     if lk.has_attr('href'):
        #         acm_papers_pdfLink.append(lk['href'])
        #         papers_pdfLink.append(lk['href'])
        #     print(acm_papers_pdfLink)
            
        page_no = page_no +1 
        
    print(len(paper_names))
    print(acm_papers_title)
    print(acm_papers_type)
    print(acm_papers_pubDate)
    print(len(paper_names))
    papers_dict = {'PN':[],
                    'PT':[],
                    'PPD':[],
                    'PRO':[]     
        }
    
    papers_dict['PN'].extend(acm_papers_title)
    papers_dict['PT'].extend(acm_papers_type)
    papers_dict['PPD'].extend(acm_papers_pubDate)
    papers_dict['PRO'].extend(acm_papers_proc)
    # papers_dict['LK'].extend(acm_papers_pdfLink)
    
    paper_df = pd.DataFrame(papers_dict)
    print(paper_df)
    
    paper_df.to_csv('acm_papers_2.csv')
    
    # IEEE - not working
    # acm_url = "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=(Conversat*%20OR%20dialog*)%20AND%20(acts%20OR%20moves%20OR%20Schema%20OR%20Annotation%20OR%20classification%20OR%20Taxonomy)%20AND%20(“human-human”)%20NOT%20Agent"
    # driver.get(acm_url)
    # wait = WebDriverWait(driver,10)
    # ieee_papers= []
    # for page in range(1,10):
    #     page_content = driver.page_source
    #     soup= BeautifulSoup(page_content,'html.parser')
    #     # paper_names_search = soup.find_all('h2',class_='result-item-title')
    #     paper_names_search = soup.find_all('div > a')
    #     # paper_years_search = soup.find_all('div',attrs={'class','bookPubDate'})
    #     # paper_authors_search = soup.find_all
    #     # paper_cite_search = 
    #     # paper_pdflink_search = 
    #     # papers_proceedings_search = soup.find_all
  
    #     for i in paper_names_search:
    #         ieee_papers.append(i.getText().lower())
    #         if (i.getText().lower() not in paper_names):
    #             paper_names.append(i.getText().lower())
    # print(ieee_papers)
    # print(len(ieee_papers))
   
     
    # ScienceDirect 
    # url = "https://www.sciencedirect.com/search?tak=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29&qs=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29%20AND%20%22human-human%22%20Not%20agent"
    # driver.get(url)
    # wait = WebDriverWait(driver,10)
    # sd_papers= []
    # for page in range(2):
    #     page_content = driver.page_source
    #     soup= BeautifulSoup(page_content,'html.parser')
    #     # paper_names_search = soup.find_all('h2',class_='result-list-title-link')
    #     paper_names_search = soup.find_all('a',attrs={'class','result-list-title-link u-font-serif text-s'})
    #     # paper_years_search = soup.find_all('div',attrs={'class','bookPubDate'})
    #     # paper_authors_search = soup.find_all
    #     # paper_cite_search = 
    #     # paper_pdflink_search = 
    #     # papers_proceedings_search = soup.find_all
  
    #     for i in paper_names_search:
    #         sd_papers.append(i.getText())
    #         if (i.getText() not in paper_names):
    #             paper_names.append(i.getText())
    # print(sd_papers)
    # print(len(sd_papers))
   
    #Wiley
    # wiley_url ="https://onlinelibrary.wiley.com/action/doSearch?field1=AllField&text1=%28convers*%2BOR%2Bdialog*%29%2BAND%2B%28acts%2BOR%2Bmoves%2BOR%2BSchema%2BOR%2BAnnotation%2BOR%2Bclassification%2BOR%2BTaxonomy%29%2BAND%2B%22human-human%22%2BNOT&Ppub="
    # driver.get(wiley_url)
    # wait = WebDriverWait(driver,10)
    # wiley_papers= []
    # for page in range(1,10):
    #     page_content = driver.page_source
    #     soup= BeautifulSoup(page_content,'html.parser')
    #     # paper_names_search = soup.find_all('h2',class_='result-list-title-link')
    #     # paper_names_search = soup.find_all('div',attrs={'class','result-item-title'})
    #     paper_names_search = soup.find_all('a',attrs={'class','publication_title visitable'})
    #     # paper_years_search = soup.find_all('a',attrs={'class','publication_title visitable'})
    #     # paper_authors_search = soup.find_all
    #     # paper_cite_search = 
    #     # paper_pdflink_search = 
    #     # papers_proceedings_search = soup.find_all
  
    #     for i in paper_names_search:
    #         wiley_papers.append(i.getText())
    #         if (i.getText() not in paper_names):
    #             paper_names.append(i.getText())
    
    # # print(wiley_papers)
    # print(len(wiley_papers))
   
 
    #Springer
    # springer_url = "https://link.springer.com/search?query=%28Conversation*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28%E2%80%9Chuman-human%E2%80%9D%29++NOT+agent&facet-content-type=%22Article%22"
    # driver.get(springer_url)
    # wait = WebDriverWait(driver,10)
    # springer_papers= []
    # for page in range(1,35):
    #     page_content = driver.page_source
    #     soup= BeautifulSoup(page_content,'html.parser')
    #     # paper_names_search = soup.find_all('h2',class_='result-list-title-link')
    #     # paper_names_search = soup.find_all('div',attrs={'class','result-item-title'})
    #     paper_names_search = soup.find_all('a',attrs={'class','publication_title visitable'})
    #     # paper_years_search = soup.find_all('a',attrs={'class','publication_title visitable'})
    #     # paper_authors_search = soup.find_all
    #     # paper_cite_search = 
    #     # paper_pdflink_search = 
    #     # papers_proceedings_search = soup.find_all
  
    #     for i in paper_names_search:
    #         springer_papers.append(i.getText())
    #         if (i.getText() not in paper_names):
    #             paper_names.append(i.getText())
    
    # # print(springer_papers)
    # print(len(springer_papers)) #391
   
    
    #ISLS
    # isls_url = "https://repository.isls.org/simple-search?location=%2F&query=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+OR+%22human-human%22+NOT+Agent+&rpp=10&sort_by=score&order=desc#"
    # driver.get(isls_url)
    # wait = WebDriverWait(driver,10)
    # isls_papers= []
    # for page in range(1,35):
    #     page_content = driver.page_source
    #     soup= BeautifulSoup(page_content,'html.parser')
    #     # paper_names_search = soup.find_all('h2',class_='result-list-title-link')
    #     # paper_names_search = soup.find_all('div',attrs={'class','result-item-title'})
    #     paper_names_search = soup.find_all('td',attrs={'headers,''t2})
    #     # paper_years_search = soup.find_all('a',attrs={'class','publication_title visitable'})
    #     # paper_authors_search = soup.find_all
    #     # paper_cite_search = 
    #     # paper_pdflink_search = 
    #     # papers_proceedings_search = soup.find_all
  
    #     for i in paper_names_search:
    #         isls_papers.append(i.getText())
    #         if (i.getText() not in paper_names):
    #             paper_names.append(i.getText())
    # print(len(isls_papers))
    # # print(springer_papers)
   
   
    #combining all lists together 
   # for url in urlList:
   #      driver.get(url)
   #      wait = WebDriverWait(driver,10)
   #      # page_content = driver.page_source
   #      # print(page_content)
   #      # soup= BeautifulSoup(page_content,'html.parser')
        
   #      #might be dofferent for each db
   #      for page in range(1,10):
   #          page_content = driver.page_source
   #          soup= BeautifulSoup(page_content,'html.parser')
   #          if (paper_name search == 
   #              result-item-title (h2), 
   #          paper_names_search = soup.find_all('h5',class_='issue-item__title')
   #          # paper_years_search = soup.find_all('div',attrs={'class','bookPubDate'})
   #          # paper_authors_search = soup.find_all
   #          # paper_cite_search = 
   #          # paper_pdflink_search = 
   #          # papers_proceedings_search = soup.find_all
            
   #          paper_names = []
   #          for i in paper_names_search:
   #              paper_names.append(i.getText())
                
   #          print(paper_names)
    # for tag in paper_names_class:
    #      # paper_names.append(driver.find_element_by_class_name(paper_names_class).text)
    #      paper_names.append(driver.find_element(by=By.CLASS_NAME, value=paper_names_class).text)
    # print(paper_names)
    # search_string  = "Dialog conversat communicat Acts Moves scheme annotation classification taxonomy human-human collab learning"
    # add_ss = driver.find_element_by_id("query")
    # add_ss = driver.find_element(id, "query")
    # add_ss.send_keys(search_string)
    
    # s = driver.find_element_by_css_selector("span[class='bar-title']")
    # s.click()
    # print(s.text)
    
    #filter for articles 
    # art_btn_path = "/html/body/div[5]/div[3]/div/div[2]/div[2]/ol/li[1]/a/span[2]"
    # art_btn = wait.until(EC.element_to_be_clickable((By.XPATH, art_btn_path)))
    
    # art_btn_class = "bar-title"
    # art_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class = 'bar-title']")))
    
    
    # art_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, art_btn_class)))
    
    # art_btn = wait.until(EC.element_to_be_clickable((By.XPATH, art_btn_path)))
    # print(art_btn.text)
    # art_btn.click()
    
    
    
    # assert "Python" in driver.title
    return
    

def search_Springer():
    #searching for articles in springer 
    url = "https://link.springer.com/search?facet-content-type=Article"
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver,10)
    
    search_string  = "Dialog conversat communicat Acts Moves scheme annotation classification taxonomy human-human collab learning"
    # add_ss = driver.find_element_by_id("query")
    add_ss = driver.find_element(id, "query")
    add_ss.send_keys(search_string)
    
    # s = driver.find_element_by_css_selector("span[class='bar-title']")
    # s.click()
    # print(s.text)
    
    #filter for articles 
    # art_btn_path = "/html/body/div[5]/div[3]/div/div[2]/div[2]/ol/li[1]/a/span[2]"
    # art_btn = wait.until(EC.element_to_be_clickable((By.XPATH, art_btn_path)))
    
    # art_btn_class = "bar-title"
    # art_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class = 'bar-title']")))
    
    
    # art_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, art_btn_class)))
    
    # art_btn = wait.until(EC.element_to_be_clickable((By.XPATH, art_btn_path)))
    # print(art_btn.text)
    # art_btn.click()
    
    
    
    # assert "Python" in driver.title
    
    return
    


def main():
    print("Welcome to research paper searching engine")
    search_anySearchLink()
    # while(1):
    #     print("1. ACM")
    #     print("2. SpringerLink")
        
    #     try:
    #         ip = int(input("Select a database to search from the options:  ")or 0)
    #     except ValueError:
    #         print("/n Invalid Input: Numeric characters only")
    #         continue
        
    #     if(ip == 0):
    #         print("")
    #     elif(ip==1):
    #         pass
    #         # search_ACM()
    #     elif(ip==2):
    #         pass
    #         # search_Springer()
    #     else:
    #         print("/n" +str(ip)+ "is not an option")
    return

if __name__ == "__main__":
    main()