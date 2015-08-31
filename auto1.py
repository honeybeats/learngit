# -*- coding:utf-8 -*-
import sys
import urllib
import re
import xlwt
#reload(sys)
#sys.setdefaultencoding('utf-8')

def read_file():
    A = urllib.urlopen('file:///C:/Users/zhongxin/Desktop/test/huh.htm')
    global X
    global x
    global B
    B = []
    X = re.findall(r'美女\w', A.read())
    '''for x in X:
        x.decode()
        B.append(x)'''
def set_style(name,height,bold=False):


    style = xlwt.XFStyle() 
    font = xlwt.Font() 
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
 
  # borders= xlwt.Borders()
  # borders.left= 6
  # borders.right= 6
  # borders.top= 6
  # borders.bottom= 6
 
    style.font = font
  # style.borders = borders
 
    return style

#写excel
def write_excel():
    f = xlwt.Workbook() 

    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) 
    row0 = X


    for i in range(0,len(row0)):
        sheet1.write(i,0,row0[i],set_style('Times New Roman',220,False))
 

 
    f.save('demonnn.xls') 
 
if __name__ == '__main__':
  #generate_workbook()
  #read_excel()
    read_file()
    write_excel()
