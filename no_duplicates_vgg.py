# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:50:19 2020

@author: Windows7
"""

import pandas as pd
import csv

data_frame = pd.read_csv('D:/BS-EE/CONVSYS_Internship/Python_Scripts/Remove_Duplicates/Remove_duplicates_in_vgg/22 July 2020 (Aleem)_csv.csv')

df = data_frame.drop_duplicates(subset=["filename","region_shape_attributes"])

df.to_csv(r'D:/BS-EE/CONVSYS_Internship/Python_Scripts/Remove_Duplicates/Remove_duplicates_in_vgg/Aleem_duplicates_removed.csv',index=False)
