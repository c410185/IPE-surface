import xlwings as xw
from time import clock
from multiprocessing import Process

m = [[x] for x in range(3000)]
def insert(sht):
    for i in range(1,3000):
        sht.range("A{}".format(i)).value = str(i) + 't'

if __name__ == '__main__':
    file_path1 = r'C:\Users\何方辉\Desktop\pythonexcel\\xls1.xlsx'
    file_path2 = r'C:\Users\何方辉\Desktop\pythonexcel\\xls2.xlsx'
    clock()
    wb1 = xw.Book(file_path1)
    wb2 = xw.Book(file_path2)
    sht1 = wb1.sheets[0]
    sht2 = wb2.sheets[0]
    # sht1.range('A1').value = m
    # sht2.range('A1').value = m
    # 28.6712626941584s 逐步运行，
    insert(sht1)
    insert(sht2)
    print(clock())

    #使用双进程,两个文件处理完29.87S，还慢了1S,不知道是程序的问题还是我自己的写法问题。
    #但是这毕竟可以同时处理两个文件了
    # m3 处理器，4G内存
    """
    clock()
    p1 = Process(target=run, args=(file_path1,))
    p2 = Process(target=run, args=(file_path2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(clock())
    """