import pandas as pd
import numpy as np
import xlrd
import os
import glob

# read in the protein files
colon_tumors_pro = pd.read_excel(
    'proteomics data/colon tumors/2017-03-19_Haigis_5v5_Pro copy.xlsx', 'Protein', index_col=None, na_values=['NA'])
pancreas_tumors_pro = pd.read_excel(
    '/Users/benjaminwu/Desktop/excel_script/proteomics data/pancreas tumors/2017-10-05_EP_KH_panc_Pro copy.xlsx', index_col=None, na_values=['NA'])
scraped_colon_pro = pd.read_excel(
    '/Users/benjaminwu/Desktop/excel_script/proteomics data/scraped colon/2015-03_HaigisMouseColon8plex_Prot copy.xlsx', index_col=None, na_values=['NA'])
whole_pancreas_pro = pd.read_excel(
    '/Users/benjaminwu/Desktop/excel_script/proteomics data/whole pancreas/2015-11_HaigisMousePancPro copy.xlsx', index_col=None, na_values=['NA'])


# change dates back to the gene names
def date_to_gene(df):
    # remove all rows that have ##
    df = df[~df['Protein Id'].str.contains('##', na=False)]
    # write dataframe to csv
    df.to_csv('foo.csv')
    # read csv
    df2 = pd.read_csv('foo.csv')
    df2['Gene Symbol'] = df2['Gene Symbol'].str.replace('00:00:00', '').str.replace(
        '2017-', '').str.replace('2016-', '').str.replace('2015-', '').str.replace(
        '09-0', 'Sept').str.replace('09-1', 'Sep1').str.replace('03-01', 'Marh1').str.replace(
        '03-02', 'Marc2').str.replace('03-05', 'Marh5').str.replace('03-06', 'Marh6')
    # delete file used to write df to
    os.remove('foo.csv')

    # TO DO: delete extra entries that are not relevant

    # write df to csv
    df2.to_csv('edited1.csv')


# date_to_gene(cprot)


# new_cprot.to_excel('bar1.xlsx')
