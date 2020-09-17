""" 
Name:         Roger Silva Santos Aguiar
Function:     Learning TDD
Initial date: September 17, 2020
Last update:  September 17, 2020
 """

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('Http://localhost:8000')

assert 'Django' in browser.title