from os import close

file = open(file= 'C:/Users/Fowls/Documents/gratitude.txt', mode='r')

content = file.read()
print(content)

file.close()

from bs4 import BeautifulSoup
import requests

nasa_chandra_html = requests.get("https://www.asc-csa.gc.ca/eng/astronomy/")
parsed_html = BeautifulSoup(nasa_chandra_html.content, 'html5lib')

all_paragraph_elements = parsed_html.find_all('a')
first_paragraph = all_paragraph_elements[0]
print(first_paragraph)

second_paragraph = all_paragraph_elements[1]
print(second_paragraph)

third_paragraph = all_paragraph_elements[2]
print(third_paragraph)

fourth_paragraph = all_paragraph_elements[3]
print(fourth_paragraph)

fifth_paragraph = all_paragraph_elements[4]
print(fifth_paragraph)

sixth_paragraph = all_paragraph_elements[5]
print(sixth_paragraph)

seventh_paragraph = all_paragraph_elements[6]
print(seventh_paragraph)

eighth_paragraph = all_paragraph_elements[7]
print(eighth_paragraph)