#The program is to convert virus ammonia acid gene sequence into charges
#By Lishen Wang and Steed Huang et al from 
#https://www.linkedin.com/company/institute-for-industrial-technology-research
#June 2020 for Beijing COVID19 Pandemic analysis

import csv,os,math
import pandas as pd
import xlrd
import xlwt

def get_name(num):
    ls = []
    for i in range(num):
        a = input("the name of file")
        ls.append(a)
    return ls

def read_file(file_num,name):
    back_file_data = []
    for i in range(file_num):
        f = open(r"Source/%s.txt"%(name[i]),'r')
        file_temp = f.read().replace("\n","")
        file_temp = file_temp.replace(" ","")
        back_file_data.append(file_temp)
        f.close()
    return back_file_data

def convert(COV1,ls_COV1):
    data = xlrd.open_workbook('Source/ChargeTable.xls')#read charge value from table file
    table=data.sheet_by_index(1)
    print(data.sheet_names())
    ls = []
    for j in range(0,table.nrows-3):
        a = table.row_values(j)[7]
        ls.append(a)
    z = 64    
    for i in COV1:
        if i == '-':
            i = '['
        k = 1
        for j in ls:
            if i == chr(k+z):
                ls_COV1.append(j)
            k = k + 1            
    return ls_COV1

def get_dynamic_list(names):
    createVar = globals()
    # createVar = locals()
    for i in range(len(names)):
        createVar[names[i]] = list()

def write_to_excel(ls_name,ls):
    f = xlwt.Workbook() #Create workbook
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)#set artribute
    k = 0
    for j in range(len(ls_name)):
        k = 0
        sheet1.write(k,j,ls_name[j])
        for i in ls[j]:
            sheet1.write(k+1,j,i)
            k+=1
    f.save('Result/BeijingFishCOVID19Charge.xls')

if __name__ == '__main__':
    ls = []
    ls_name = []
    file_num = eval(input("Please input the number of file you want to convert:"))
    ls_name = get_name(file_num)
    # get_dynamic_list(ls_name)
    ls = read_file(file_num,ls_name)
    for i in range(len(ls_name)):
    	locals()[ls_name[i]] = []
    i = 0
    for i in range(len(ls_name)):
        ls[i] = convert(ls[i],locals()[ls_name[i]])
    write_to_excel(ls_name,ls)
