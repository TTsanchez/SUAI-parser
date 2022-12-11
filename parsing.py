import requests
from bs4 import BeautifulSoup
import lxml
import time

def checkNet():
    try:
        response = requests.get("http://www.google.com")
        return True
    except requests.ConnectionError:
        return False


def rasp_out(teg, self, PG_bar):
    schedule = ''
    percent = teg.find_parent()
    print(percent)
    print(len(percent))
    percent = 100 / len(percent)
    print(percent)
    while True:
        PG_bar += percent
        self.progressBar.setValue(PG_bar)
        time.sleep(0.00001)
        teg = teg.find_next_sibling()
        if teg == None:
            break
        if teg.name == 'h3' or teg.name == 'h4':
            if teg.name == 'h3' and schedule != '':
                schedule += "\n"
            schedule += teg.text
            schedule += "\n"
        if teg.attrs == {'class': ['study']}:
            for el in teg.find_all('span'):
                schedule += el.get_text()
                schedule += "\n"
    return schedule


def teacher(soup, form_out):
    bb = soup.find_all('option')
    for option in bb:
        value = option.get('value')
        txt0 = option.contents[0].strip()
        txt = option.contents[0].split('-')[0].strip().upper()
        if form_out == txt:
            print(txt, form_out)
            print(txt0)
            return txt0
    return 0

def AUDIT(soup, form_out):
    bb = soup.find_all('option')
    for option in bb:
        value = option.get('value')
        txt0 = option.contents[0].strip()
        txt = option.contents[0].split('-')[0].strip().upper()
        if form_out == txt:
            print(txt, form_out)
            print(txt0)
            return txt0
    return 0

def weeks(soup):
    print(soup.find('em', class_='up'))
    print(soup.find('em', class_='up') == None)
    if soup.find('em', class_='up') == None:
        week = soup.find('em', class_='dn').text
    else:
        week = soup.find('em', class_='up').text
    if 'нечетная' in week:
        week = 'нечетная'
    else:
        week = 'четная'
    return week

def parser(form_out, self):
    PG_bar = 0
    self.progressBar.setValue(PG_bar)
    if checkNet() == True:
        url = 'https://guap.ru/rasp/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        form_out = form_out.upper().strip()
        if self.search == "GP":
            if "-" in form_out:
                return -2,-2
            option_tag = soup.find_all('option', text=form_out)
        elif self.search == "Teach":
            texter = teacher(soup, form_out)
            print(form_out)
            if texter == 0:
                return 0,0
            option_tag = soup.find_all('option', text=texter)
        elif self.search == "AU":
            if form_out == "116" or form_out == "СПОРТЗАЛ*" or form_out == "СПОРТ.ЗАЛ*":
                option_tag = soup.find_all('option', text=form_out.lower())
            elif "-" not in form_out:
                return -2, -2
            else:
                option_tag = soup.find_all('option', text=form_out)
        if option_tag == []:
            return 0,0
        else:
            if self.search == "GP":
                for option in option_tag:
                    value = option.get('value')
                link = "https://guap.ru/rasp/?g=" + value
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'lxml')
                week = weeks(soup)
                raspis = soup.find('h2').text
                print(raspis)
                teg = soup.find('h2')
                schedule = rasp_out(teg, self, PG_bar)
                return schedule, week

            elif self.search == "Teach":
                print("Teach")
                print(form_out)
                for option in option_tag:
                    value = option.get('value')

                print(f"{value} value")
                link = "https://guap.ru/rasp/?p=" + value
                response = requests.get(link)
                print(link + "link")
                soup = BeautifulSoup(response.text, 'lxml')
                week = weeks(soup)
                raspis = soup.find('h2').text
                print(raspis)
                teg = soup.find('h2')
                schedule = rasp_out(teg, self, PG_bar)
                return schedule, week

            elif self.search == "AU":
                for option in option_tag:
                    value = option.get('value')
                link = "https://guap.ru/rasp/?r=" + value
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'lxml')
                print(soup)
                week = weeks(soup)
                raspis = soup.find('h2' ).text
                print(raspis)
                teg = soup.find('h2')
                schedule = rasp_out(teg, self, PG_bar)
                return schedule, week

    elif checkNet() == False:
        return -1,-1