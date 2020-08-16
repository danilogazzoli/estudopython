from pyvirtualdisplay import Display
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from functools import wraps

class FindJob():
    def __init__(self, cargo,  localidade):
        self.cargo = cargo
        self.localidade = localidade
        self.driver = None

    def display_start(self):
        display = Display(visible=0, size=(800, 600))
        display.start()

    def display_stop(self):
        display.stop()


class Indeed(FindJob):
    def executa(self):
        self.display_start()
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

            dataframe = pd.DataFrame(
                columns=["Title", "Location", "Company", "Salary", "Description"])
            # self.driver.minimize_window()
            for cnt in range(0, 50, 10):
                self.driver.get(f"https://www.indeed.com.br/empregos?q={self.cargo}&l={self.localidade}%2C+PR&start=" + str(cnt))

                sleep(10)

                try:
                    pop_up = 'None'

                    jobs = self.driver.find_elements_by_class_name('result')

                    for job in jobs:
                        try:
                          close_window = self.driver.find_element_by_id('popover-close-link')
                          close_window.click()
                        except:
                            pass

                        result = job.get_attribute('innerHTML')
                        soup = BeautifulSoup(result, 'html.parser')

                        title = soup.find(
                            "a", class_="jobtitle").text.replace('\n', '')
                        location = soup.find(class_="location").text
                        employer = soup.find(
                            class_="company").text.replace('\n', '').strip()
                        try:
                            salary = soup.find(class_="salary").text.replace(
                                '\n', '').strip()
                        except:
                            salary = 'None'

                        print(title, location, employer, salary)

                        summ = job.find_elements_by_class_name("summary")[0]
                        summ.click()
                        sleep(1)
                        try:
                            job_desc = self.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[3]/div/div[2]/div[1]/div[2]').text

                            dataframe = dataframe.append(
                                 {'Title': title, 'Location': location, 'Employer': employer, 'Description': job_desc}, ignore_index=True)
                        except:
                            pass

                        sleep(2)
                except:
                    try:
                        close_window = self.driver.find_element_by_id('popover-close-link')
                        close_window.click()
                    except:
                        pass
                    ##pop_up = self.driver.find_element_by_xpath(
                    ##    '/html/body/table[2]/tbody/tr/td/div[2]/div[2]/div[4]/div[3]/div[2]/a')
                    ##pop_up.click()
                dataframe.to_csv("jobs.csv", index=False)
        finally:
            self.display_stop()



def executa(lista):
    for obj in lista:
        obj.executa()


lista = []
lista.append(Indeed('Desenvolvedor+Python','Curitiba'))
executa(lista)
