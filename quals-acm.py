#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:53:38 2022

@author: gloriakatuka
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:30:28 2022

@author: gloriakatuka
"""

#import sys
import urllib3
#import requests
import pandas as pd
#import re

from bs4 import BeautifulSoup
# pip install selenium
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
   #  dbDict = {
   #  'ACMurl':"https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&field1=AllField&text1=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28“human-human”%29NOT+Agent+",
   #  'IEEEurl':"https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=(Conversat*%20OR%20dialog*)%20AND%20(acts%20OR%20moves%20OR%20Schema%20OR%20Annotation%20OR%20classification%20OR%20Taxonomy)%20AND%20(“human-human”)%20NOT%20Agent",
   #  'SDurl':"https://www.sciencedirect.com/search?tak=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29&qs=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29%20AND%20%22human-human%22%20Not%20agent",
   # 'Wileyurl':"https://onlinelibrary.wiley.com/action/doSearch?field1=AllField&text1=%28convers*%2BOR%2Bdialog*%29%2BAND%2B%28acts%2BOR%2Bmoves%2BOR%2BSchema%2BOR%2BAnnotation%2BOR%2Bclassification%2BOR%2BTaxonomy%29%2BAND%2B%22human-human%22%2BNOT&Ppub=",
   #  'Springerurl':"https://link.springer.com/search?query=%28Conversation*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28%E2%80%9Chuman-human%E2%80%9D%29++NOT+agent&facet-content-type=%22Article%22",
   #  'islsurl':"https://repository.isls.org/simple-search?location=%2F&query=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+OR+%22human-human%22+NOT+Agent+&rpp=10&sort_by=score&order=desc#"
   #      }
   #  urlList = ["https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&field1=AllField&text1=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28“human-human”%29NOT+Agent+",
   #  "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=(Conversat*%20OR%20dialog*)%20AND%20(acts%20OR%20moves%20OR%20Schema%20OR%20Annotation%20OR%20classification%20OR%20Taxonomy)%20AND%20(“human-human”)%20NOT%20Agent",
   #  "https://www.sciencedirect.com/search?tak=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29&qs=%28Conversation%20OR%20dialog%29%20AND%20%28acts%20OR%20moves%20OR%20schema%20OR%20annotation%29%20AND%20%22human-human%22%20Not%20agent",
   #  "https://onlinelibrary.wiley.com/action/doSearch?field1=AllField&text1=%28convers*%2BOR%2Bdialog*%29%2BAND%2B%28acts%2BOR%2Bmoves%2BOR%2BSchema%2BOR%2BAnnotation%2BOR%2Bclassification%2BOR%2BTaxonomy%29%2BAND%2B%22human-human%22%2BNOT&Ppub=",
   #  "https://link.springer.com/search?query=%28Conversation*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+AND+%28%E2%80%9Chuman-human%E2%80%9D%29++NOT+agent&facet-content-type=%22Article%22",
   #  "https://repository.isls.org/simple-search?location=%2F&query=%28Conversat*+OR+dialog*%29+AND+%28acts+OR+moves+OR+Schema+OR+Annotation+OR+classification+OR+Taxonomy%29+OR+%22human-human%22+NOT+Agent+&rpp=10&sort_by=score&order=desc#"]
    
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
    
    while (page_no <= 17):        
        url = f"https://dl.acm.org/action/doSearch?AllField=%28convers*+OR+dialog*+OR+speech+OR+comm*%29+AND+%28acts+OR+moves+OR+schem*+OR+annotation+OR+taxonomy%29+AND+%22human-human%22+NOT+agent+NOT+robot+&startPage={page_no}&pageSize=50"
        driver.get(url)
        wait = WebDriverWait(driver,10)    
        page_content = driver.page_source
        soup= BeautifulSoup(page_content,'html.parser')
        paper_names_search = soup.find_all('h5',class_='issue-item__title')
        paper_type_search = soup.find_all('div',class_='issue-heading')
        paper_pubDate_search = soup.find_all('div',class_='bookPubDate simple-tooltip__block--b')
        paper_proc_search = soup.find_all('div',class_='issue-item__detail')

      
        for pn in paper_names_search:
            acm_papers_title.append(pn.getText().lower())
            paper_names.append(pn.getText().lower())
            
        for pt in paper_type_search:
            acm_papers_type.append(pt.getText().lower())
            paper_types.append(pt.getText().lower())   
            
        for ppd in paper_pubDate_search:
            acm_papers_pubDate.append(ppd.getText().lower())
            papers_pubDate.append(ppd.getText().lower()) 
            
        for pro in paper_proc_search:
            acm_papers_proc.append(pro.getText().lower())
            papers_proc.append(pro.getText().lower()) 
        
        
        # for lk in paper_pdfLink_search:
        #     if lk.has_attr('href'):
        #         acm_papers_pdfLink.append(lk['href'])
        #         papers_pdfLink.append(lk['href'])
        #     print(acm_papers_pdfLink)
            
        page_no = page_no +1 
        
    # print(paper_names)
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
    
    # paper_df = pd.DataFrame(papers_dict)
    paper_df = pd.DataFrame.from_dict(papers_dict,orient='index')
    paper_df = paper_df.transpose()
    print(len(paper_df))
    
    paper_df.to_csv('acm_papers_412.csv')
    
    return
    



def main():
    print("Welcome to research paper searching engine")
    search_anySearchLink()
    return

if __name__ == "__main__":
    main()