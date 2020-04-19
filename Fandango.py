#Project of data scrapping of a site fandango.com
#Data is save out in CSV file

#By Ali Ahmad

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import csv

def csv_f(filename,data):
        data_cc=[]
        with open(filename,'a') as f:
            w=csv.writer(f, delimiter="\t")
            try:
              w.writerow(data)
            except:
                try:
                    for i in data:
                        try:
                            i.encoda("UTF-8")
                        except:
                            try:
                                i.decode("UTF-8")
                            except:
                                i=''
                        data_cc.append(i)
                except:
                    pass

                data_cc=[i.encode("ascii" , 'replace') for i in data_cc]
                w.writerow(data_cc)
        f.close()

def file_cc(outputfile,data):
        if not  os.path.exists(outputfile):
            csv_f(outputfile,['name', 'time' , 'link'])

        csv_f(outputfile,[data[0],data[1] ,data[2]])
def main() :
    driver = webdriver.Chrome()
    outputfile = 'selenium1.csv'
    try:
        driver.get("https://www.fandango.com/movies-in-theaters")
        delay = 5
        wait = WebDriverWait(driver, delay)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'now-playing__wrap')))
        print("done")
    except:
        print("Not done")

    try:
        mm = driver.find_elements(By.CLASS_NAME, "now-playing__wrap")
        for k in mm:
            li = k.find_elements_by_tag_name("li")
            try:
                for j in li:
                    an = j.find_element_by_tag_name('a')
                    l = an.get_attribute("href")
                    d = an.find_element_by_class_name("poster-card--title-block")
                    n = d.find_element_by_tag_name("span")
                    name = n.text
                    t = d.find_element_by_tag_name("time")
                    time=t.text
                    if time=="":
                        time="Not Mentioned"
                    file_cc(outputfile, [name,time,l])
            except Exception as ee:
                print("Exception 1 detected:", ee)
    except Exception as e:
        print("Exception 2 detected :", e)
    driver.close()


if __name__ == "__main__":
    main()

