
import sys
from PyQt5.QtWidgets import QApplication, QWidget

print("1. 프로그램 시작")

class Calculator(QWidget):
    
    def __init__(self):
        print("2. Calculator __init__ 진입")
        super().__init__()
        self.initUI()
        
    def initUI(self):
        print("3. initUI 실행됨")
        self.setWindowTitle('Calculator')
        self.resize(256, 256)
        self.show()
        
        
if __name__ == '__main__':
    print("4. main 시작")
    
    app = QApplication(sys.argv)
    print("5. QApplication 생성 완료")
    
    view = Calculator()
    print("6. Calculator 객체 생성 완료")
    
    print("7. app.exec_() 진입 직전")
    sys.exit(app.exec_())
    
    print("8. 여기 찍히면 비정상 (실행 안되는게 정상)")
