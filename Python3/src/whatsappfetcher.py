#!/bin/python3
from miscellaneous import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

class whatsbot :
    def __init__(self,browser,contact) :
        self.browser=browser
        self.contact=contact
