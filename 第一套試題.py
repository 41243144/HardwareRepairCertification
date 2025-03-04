import tkinter as tk
class Test1():
    def __init__(self):
        # 建立Tkinter視窗
        self.main_window = tk.Tk()

        self.main_window.title('第一套試題')

        # 設定視窗大小為800x600
        self.main_window.geometry('800x600')
        
        # 執行第一題
        self.exampleTest1()

        # 執行第二題
        self.exampleTest2()

        # 執行第三題
        self.exampleTest3()

        # 執行第四題
        self.exampleTest4()

        # 執行第五題
        self.exampleTest5()

        # 啟動主視窗
        self.main_window.mainloop()
        
        
    def loadFile(self, fileName):
        # 讀取檔案
        with open(fileName, 'r', encoding="utf-8") as fileObject:
            data = fileObject.read()
        # 回傳讀取的資料
        return data
    
    def showResult(self, resultMsg):
        ''' 
            顯示執行結果，pack()將元件加入到視窗中
            self.main_window為主視窗
            text    顯示的文字
            justify 物件對齊方式
            anchor  文字對齊方式
            relief  邊框樣式
            height  高度

            fill    填充方式
            expand  是否允許擴展
            padx    與左右邊界的距離
            pady    與上下邊界的距離
        '''

        self.label = tk.Label(self.main_window, text=resultMsg, justify='left', anchor='w', relief='solid').pack(fill='both', expand=False, padx=10, pady=10)

    def exampleTest1(self):
        # *****************************
        # *11900-1060301 Program Start*
        # *****************************
        '''
            請利用『指定』迴圈控制指令，由外部資料檔讀入一個欲判斷的數字，若此數
            字為迴文(Palindrome，左右讀起均同，例如 12321)，則印出此數字及“is a
            palindrome.”，若不是則印出此數字及“is not a palindrome.”
        '''
        
        fileLocation = './測試題目/1060301.SM'

        data = self.loadFile(fileLocation)
        
        resultMsg = f'第一題結果：{data} '

        # 判斷是否為回文，是的話顯示is a palindrome.，否則顯示is not a palindrome.
        resultMsg += 'is a palindrome.' if data == data[::-1] else 'is not a palindrome.'

        # 顯示結果
        self.showResult(resultMsg)

    def exampleTest2(self):
        # *****************************
        # *11900-1060302 Program Start*
        # *****************************

        '''
            利用『指定』廻圈控制指令，由外部資料檔讀入數字，列印從 1 開始直到該數
            字為止之直角三角形。
        '''
        fileLocation = './測試題目/1060303.SM'

        data = self.loadFile(fileLocation)
        
        resultMsg = '第三題結果：'

        # 依續加入數字，並換行
        for i in range(1, len(data)+1):
            resultMsg += '\n' + data[:i]

        # 依續加入數字，並換行(while)
        # i = 1
        # while i <= len(data):
        #     resultMsg += '\n' + data[:i]
        #     i += 1

        # 依續加入數字，並換行(do while)
        # i = 1
        # while True:
        #     resultMsg += '\n' + data[:i]
        #     i += 1
        #     if i > len(data):
        #         break


        # 顯示結果
        self.showResult(resultMsg)

    def exampleTest3(self):
        # *****************************
        # *11900-1060303 Program Start*
        # *****************************

        '''
            請利用『指定』迴圈控制指令，由外部資料檔讀入欲檢查的數字，若此數字是
            質數則印出此數字及 “is a prime number.”，若不是則印出此數字及 “is not a
            prime number.” 
        '''
        fileLocation = './測試題目/1060303.SM'

        data = self.loadFile(fileLocation)
        
        resultMsg = f'第三題結果：{data} '

        # 判斷是否為質數，是的話顯示is a prime number.，否則顯示is not a prime number.
        resultMsg += 'is a prime number.' if all([int(data) % i != 0 for i in range(2, int(int(data) ** 0.5) + 1)]) else 'is not a prime number.'

        # 顯示結果
        self.showResult(resultMsg)

    def exampleTest4(self):
        # *****************************
        # *11900-1060304 Program Start*
        # *****************************

        '''
            體質指數 BMI（Body Mass Index）是常用在評估人體肥胖程度的一種指標，其
            計算公式為體重除以身高的平方：
            BMI = 體重(公斤)/(身高 × 身高)(公尺 2
            )
            一般而言，正常的體重其 BMI 範圍=20～25。請設計一個程式，輸入 3 組身高與體重後，
            將 BMI 值最小者印出並判斷是否在正常範圍內(BMI 之計算身高以公尺，體重以公斤計
            算，計算至個位數，小數點後第一位數以四捨五入計算)。

        '''
        fileLocation = './測試題目/1060304.SM'

        data = self.loadFile(fileLocation)

        bmiData = data.split()

        minmiumBMI = float('inf')

        for inf in bmiData:
            height, weight = inf.split(',')
            bmi = round(float(weight) / ((float(height) / 100) ** 2), 1)
            minmiumBMI = min(bmi, minmiumBMI)
        
        resultMsg = f'第四題結果：最小BMI值={minmiumBMI} ' 
        resultMsg += "正常" if 20 <= minmiumBMI <= 25 else "不正常"

        # 顯示結果
        self.showResult(resultMsg)

    def exampleTest5(self):
        # *****************************
        # *11900-1060305 Program Start*
        # *****************************

        '''
            請利用『指定』迴圈控制指令，由外部資料檔讀入兩組 2 乘 2 矩陣數值後，將
            此兩矩陣數值相加後，列印出此矩陣。
        '''
        
        fileLocation = './測試題目/1060305.SM'

        data = self.loadFile(fileLocation)

        lines = data.split('\n')
        matrixData = []

        # 將矩陣資料轉換成二維陣列
        for line in lines:
            matrixData.append(list(map(int, line.split(','))))

        # 矩陣1為前兩行，矩陣2為後兩行
        matrix1 = matrixData[:2]
        matrix2 = matrixData[2:]

        resultMatrix = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]
        
        
        resultMsg = f'第五題結果：\n'
        resultMsg += f'[{matrix1[0][0]:<4} {matrix1[0][1]:>4}]\n'
        resultMsg += f'[{matrix1[1][0]:<4} {matrix1[1][1]:>4}]'

        # 顯示結果
        self.showResult(resultMsg)
    
if __name__ == '__main__':
    Test1()