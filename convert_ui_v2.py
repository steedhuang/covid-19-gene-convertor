#The program is to convert virus ammonia acid sequence into charges
#By Lishen Wang and Steed Huang et al from 
#https://www.linkedin.com/company/institute-for-industrial-technology-research
#Jan 2021 for UK Wales COVID19 virus mutation analysis

#Include libraries
import csv,os,math
import pandas as pd
import xlrd
import xlwt
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication,QPushButton,QGridLayout,QTextEdit
import QtTest

#Globe variables to pass file name and content
global ss,a

#Method to read file name
def get_name(num):
    global a
    ls = []
    for i in range(num):
        a = ex.name
        ls.append(a)
    return ls

#Method to read said file 
def read_file(file_num,name):
    back_file_data = []
    for i in range(file_num):
        f = open(r"Source/%s.txt"%(name[i]),'r')
        file_temp = f.read().replace("\n","")
        file_temp = file_temp.replace(" ","")
        back_file_data.append(file_temp)
        f.close()
    return back_file_data

#Method to convert protein into charge
def convert(COV1,ls_COV1):
    global ss
    data = xlrd.open_workbook('Source/Basis.xlsx')#Read file content
    table=data.sheet_by_index(0)
    ss = ex.choice
    print(ss)
    ls = []
    for j in range(0,table.nrows-3):
        a = table.row_values(j)[ss]
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

#Method to output file 
def get_dynamic_list(names):
    createVar = globals()
    # createVar = locals()
    for i in range(len(names)):
        createVar[names[i]] = list()

#Method to write output
def write_to_excel(ls_name,ls):
    global ss
    title_name = ['molecular mass','isoelectric point ','electric charge','mass charge ratio']
    f = xlwt.Workbook() #Create workbook
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)#set artribute
    k = 0
    for j in range(len(ls_name)):
        k = 0
        sheet1.write(k,j,ls_name[j])
        for i in ls[j]:
            sheet1.write(k+1,j,i)
            k+=1
    
    data ='a'+'_'+ title_name[ss-1]
    f.save('Result/%s.xls'%(data))

#Main loop    
def init():
    ls = []
    ls_name = []
    file_num = 1
    ls_name = get_name(file_num)
    # get_dynamic_list(ls_name)
    ls = read_file(file_num,ls_name)
    for i in range(len(ls_name)):
    	locals()[ls_name[i]] = []
    i = 0
    for i in range(len(ls_name)):
        ls[i] = convert(ls[i],locals()[ls_name[i]])
    write_to_excel(ls_name,ls)    

#User Interface
class Example(QWidget):
    name = 0
    choice = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        #x-the starting position of the abscissa text box, 
        qle.move(70, 30)
        #y-the starting position of the ordinate
        
        self.lbl = QLabel(self)
        qle1 = QLineEdit(self)
        qle1.move(70, 70)
        self.lbl.move(60, 40)

        redb = QPushButton('Convert', self)
        redb.move(100, 130)

        qle.textChanged[str].connect(self.onChanged_1)
        qle1.textChanged[str].connect(self.onChanged_2)
        redb.clicked.connect(init)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged_1(self, text):
        name = text
    def onChanged_2(self, text):
        choice = eval(text)

#User Warning
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
