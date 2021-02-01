# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:56:34 2021

@author: avry_
"""


import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/avry_/Documents/ds_salary_proj/chromedriver.py"

df = gs.get_jobs('data scientist',15, False, path, 15)