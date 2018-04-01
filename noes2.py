from multiprocessing import Process
import xlwings as xw
from time import clock

def insert(sht):
    for i in range(1,3000):
        sht.range("A{}".format(i)).value = str(i) + 't'

def run(file):
    wb = xw.Book(file)
    sht = wb.sheets[0]
    insert(sht)

if __name__ == '__main__':
    file_path1 = r'C:\Users\何方辉\Desktop\pythonexcel\\xls1.xlsx'
    file_path2 = r'C:\Users\何方辉\Desktop\pythonexcel\\xls2.xlsx'
    file_path3 = r'C:\Users\何方辉\Desktop\pythonexcel\\xls3.xlsx'
    file_path = [file_path1,file_path2]
    clock()
    p1 = Process(target=run,args=(file_path1,))
    # p2 = Process(target=run, args=(file_path2,))
    # p3 = Process(target=run, args=(file_path3,))
    p1.start()
    # p2.start()
    # p3.start()
    p1.join()
    # p2.join()
    # p3.join()
    print(clock())