# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


CalUI = "C:/Users/woosung/Desktop/python project/pyqt5_calc/calculator.ui"
# 폴더 안에서 ui 확장자 명을 가진 파일을 찾아서 경로를 변경해주면 된다.
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button=self.num_pushButton_1: self.NumClicked(state, button))
        # Connect 안에 실행된 함수 x 함수 자체를 넣은 것이다.  lambda : 코드를 한줄로 함수를 만들어준다.
        # 버튼 1을 눌렀을 경우 연결한다 ( state: 에러를 막기위한 인자. button은 numpushButton_1  )
        self.num_pushButton_2.clicked.connect(lambda state, button=self.num_pushButton_2: self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button=self.num_pushButton_3: self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button=self.num_pushButton_4: self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button=self.num_pushButton_5: self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button=self.num_pushButton_6: self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button=self.num_pushButton_7: self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button=self.num_pushButton_8: self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button=self.num_pushButton_9: self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button=self.num_pushButton_0: self.NumClicked(state, button))

        self.sign_pushButton_1.clicked.connect(lambda state, button=self.sign_pushButton_1: self.NumClicked(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button=self.sign_pushButton_2: self.NumClicked(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button=self.sign_pushButton_3: self.NumClicked(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button=self.sign_pushButton_4: self.NumClicked(state, button))

        self.p_open_pushButton.clicked.connect(lambda state, button=self.p_open_pushButton: self.NumClicked(state, button))
        self.p_close_pushButton.clicked.connect(lambda state, button=self.p_close_pushButton: self.NumClicked(state, button))
        self.dot_pushButton.clicked.connect(lambda state, button=self.dot_pushButton: self.NumClicked(state, button))
        self.per_pushButton.clicked.connect(lambda state, button=self.per_pushButton: self.NumClicked(state, button))

        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)
        self.del_pushButton.setStyleSheet(
            '''
            QPushButton{image:url(C:/Users/woosung/Desktop/pyqt5_calc/del.png); border:0px;}
            QPushButton:hover{image:url(C:/Users/woosung/Desktop/pyqt5_calc/dell.png); border:0px;}
            ''')

    def NumClicked(self, state, button):
        if button == self.per_pushButton:
            now_num_text = '*0.01'
        else:
            now_num_text = button.text()

        exist_line_text = self.q_lineEdit.text() # 텍스트 붙임.
        self.q_lineEdit.setText(exist_line_text + now_num_text) #뒤에 덧붙임.

    def MakeResult(self):
        try:
            result = eval(self.q_lineEdit.text())
            self.a_lineEdit.setText(str(result))
        except Exception as e:
            print(e)
            self.result_pushButton.clicked.connect(self.MakeResult)
            self.reset_pushButton.clicked.connect(self.Reset)

    def Reset(self):
        self.q_lineEdit.clear()
        self.a_lineEdit.setText('0')
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)


app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()

# 출처 : 동계산기(https://umnoni.com/category/%E2%94%94%20%EB%A7%9B%EB%B3%B4%EA%B8%B0%20%23%EB%8F%99%EA%B3%84%EC%82%B0%EA%B8%B0)
# Python으로 프로그램을 만들어보고자 /위 url을 참고해  만들어본 코드 입니다.
