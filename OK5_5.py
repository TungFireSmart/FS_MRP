import sys
import mysql.connector

# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from gui import Ui_MainWindow
from sanpham import Ui_sanpham
from sanxuat import Ui_sanxuat
from linhkien import Ui_linhkien
from chi_tiet_linh_kien import Ui_chitietlinhkien
from chi_tiet_san_pham import Ui_chitietsanpham
from san_pham_moi import Ui_sanphammoi
from tao_bom import Ui_tao_bom


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.current_file = None
        self.current_item = None
        self.current_win = None

        self.uic.but_sanpham.clicked.connect(self.sanpham)
        self.uic.action_sanpham.triggered.connect(self.sanpham)

        self.uic.but_sanxuat.clicked.connect(self.sanxuat)
        self.uic.action_khsx.triggered.connect(self.sanxuat)

        self.uic.action_linhkien.triggered.connect(self.linhkien)


    def sanpham(self):
        self.sub_win1 = QMainWindow()
        self.uic1 = Ui_sanpham()
        self.uic1.setupUi(self.sub_win1)
        self.sub_win1.show()
        self.uic1.but_home.clicked.connect(self.close)

        self.uic1.action_linhkien1.triggered.connect(self.linhkien)
        self.uic1.but_linhkien1.clicked.connect(self.linhkien)

        self.uic1.action_sanphammoi.triggered.connect(self.sanphammoi)
        self.uic1.but_sp_moi.clicked.connect(self.sanphammoi)

        self.uic1.but_search.clicked.connect(self.search_sp)

        self.load_sanpham()

    def search_sp(self):
        search_text = self.uic1.text_search_sp.toPlainText()
        print('Bắt đầu tìm kiếm từ khóa "' +  str(search_text) + '" trong bảng ds_san_pham')
        print('Sau khi tìm kiếm sẽ hiển thị kết quả trong table widget')
        print('Tìm cách thực hiện lệnh tìm kiếm khi nhập Enter trong ô search')

    def sanphammoi(self):
        self.sub_win6 = QMainWindow()
        self.uic6 = Ui_sanphammoi()
        self.uic6.setupUi(self.sub_win6)
        self.sub_win6.show()
        self.uic6.but_back.clicked.connect(self.close)

    def sanxuat(self):
        self.sub_win2 = QMainWindow()
        self.uic2 = Ui_sanxuat()
        self.uic2.setupUi(self.sub_win2)
        self.sub_win2.show()
        self.uic2.but_home2.clicked.connect(self.close)

    def linhkien(self):
        self.sub_win3 = QMainWindow()
        self.uic3 = Ui_linhkien()
        self.uic3.setupUi(self.sub_win3)
        self.sub_win3.show()
        self.uic3.but_home3.clicked.connect(self.close)
        self.uic3.but_linhkien_moi.clicked.connect(self.themlinhkienmoi)

        self.load_linhkien('chi_tiet_linh_kien')

    def load_sanpham(self):
        conn = mysql.connector.connect(user='root', password='btk123456', host='127.0.0.1', database='mrp')
        mycur = conn.cursor(buffered=True)

        # file_name = sql_table
        # # Tạo header cho các cột trong bảng
        header = ['Model', 'Tên sản phẩm', 'Version', 'Action']
        self.uic1.table_sanpham.setHorizontalHeaderLabels(header)
        try:
            code = "select Model, ten_san_pham from ds_san_pham"
            mycur.execute(code)

            result = mycur.fetchall()
            # show kết quả lên tablewidget

            self.uic1.table_sanpham.setRowCount(len(result))  # tạo số row
            self.uic1.table_sanpham.setColumnCount(4)  # tạo số column
            self.uic1.table_sanpham.setColumnWidth(0, 100)

            self.uic1.table_sanpham.setColumnWidth(1, 360)
            self.uic1.table_sanpham.setColumnWidth(2, 120)
            self.uic1.table_sanpham.setColumnWidth(3, 120)

            # Đoạn này định nghĩa 1 nút tên là 'Load', khi bấm nút này sẽ show chi tiết linh kiện
            self.btn = QPushButton()
            self.btn.setText('Load')
            self.btn.clicked.connect(self.show_linhkien)

            for row_number, row_data in enumerate(result):
                self.btn = QPushButton()
                self.btn.setText('Load')
                self.btn.clicked.connect(self.show_sanpham)
                self.uic1.table_sanpham.setCellWidget(row_number, 3, self.btn)

                # Đoạn này điền thông tin vào từng dòng
                for column_number, data in enumerate(row_data):
                    self.uic1.table_sanpham.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except:
            self.uic1.lable_sp.setText('File data error')

    def show_sanpham(self):
        r = self.uic1.table_sanpham.currentRow()
        c = self.uic1.table_sanpham.currentColumn()
        model = self.uic1.table_sanpham.item(r, 0).text()
        ten_sp = self.uic1.table_sanpham.item(r, 1).text()

        self.sub_win5 = QMainWindow()
        self.uic5 = Ui_chitietsanpham()
        self.uic5.setupUi(self.sub_win5)
        self.sub_win5.show()
        self.uic5.but_back.clicked.connect(self.close)

        self.current_item = model
        self.uic5.but_bom.clicked.connect(self.bom)

        self.uic5.lable_sp.setText(ten_sp + '\n' + 'Model: ' + model)

    def bom(self):
        print('Model của sản phẩm hiện tại là: ' + str(self.current_item))
        print('Kiểm tra xem model có tồn tại chưa? nếu có thì sản phẩm hiện tại đã có BOM list hay chưa')
        print('Nếu chưa có thì chuyển sang tạo BOM')
        print('Nếu có rồi thì show lên và cho phép sửa BOM nếu được phân quyền')

        self.sub_win7 = QMainWindow()
        self.uic7 = Ui_tao_bom()
        self.uic7.setupUi(self.sub_win7)
        self.sub_win7.show()
        self.uic7.but_back.clicked.connect(self.close)

        self.uic7.but_linhkienmoi.clicked.connect(self.themlinhkienmoi)


    def load_linhkien(self, sql_table):
        conn = mysql.connector.connect(user='root', password='btk123456', host='127.0.0.1', database='mrp')
        mycur = conn.cursor(buffered=True)

        file_name = sql_table
        # # Tạo header cho các cột trong bảng
        header = ['SKU', 'Tên vật tư', 'Part number', 'Action']
        self.uic3.table_dslinhkien.setHorizontalHeaderLabels(header)
        try:
            code = "select sku, ten_linh_kien, part_number from " + file_name
            mycur.execute(code)

            result = mycur.fetchall()
            # show kết quả lên tablewidget

            self.uic3.table_dslinhkien.setRowCount(len(result))  # tạo số row
            self.uic3.table_dslinhkien.setColumnCount(4)  # tạo số column
            self.uic3.table_dslinhkien.setColumnWidth(0, 100)

            self.uic3.table_dslinhkien.setColumnWidth(1, 360)
            self.uic3.table_dslinhkien.setColumnWidth(2, 120)
            self.uic3.table_dslinhkien.setColumnWidth(3, 120)

            # Đoạn này định nghĩa 1 nút tên là 'Load', khi bấm nút này sẽ show chi tiết linh kiện
            self.btn = QPushButton()
            self.btn.setText('Load')
            self.btn.clicked.connect(self.show_linhkien)

            for row_number, row_data in enumerate(result):
                self.btn = QPushButton()
                self.btn.setText('Load')
                self.btn.clicked.connect(self.show_linhkien)
                self.uic3.table_dslinhkien.setCellWidget(row_number, 3, self.btn)

                # Đoạn này điền thông tin vào từng dòng
                for column_number, data in enumerate(row_data):
                    self.uic3.table_dslinhkien.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except:
            self.uic3.label_ketqua.setText('File data error')

    def show_linhkien(self):
        print('Đã show chi tiết linh kiện')

    def themlinhkienmoi(self):
        self.sub_win4 = QMainWindow()
        self.uic4 = Ui_chitietlinhkien()
        self.uic4.setupUi(self.sub_win4)
        self.sub_win4.show()
        self.uic4.but_home4.clicked.connect(self.close)

    def close(self):
        try:
            self.sub_win1.close()
        except:
            print('Sub_win_1 Already Closed')

        try:
            self.sub_win2.close()
        except:
            print('Sub_win_2 Already Closed')

        try:
            self.sub_win3.close()
        except:
            print('Sub_win_3 Already Closed')

        try:
            self.sub_win4.close()
        except:
            print('Sub_win_4 Already Closed')

        try:
            self.sub_win5.close()
        except:
            print('Sub_win_5 Already Closed')

        try:
            self.sub_win6.close()
        except:
            print('Sub_win_6 Already Closed')

        try:
            self.sub_win7.close()
        except:
            print('Sub_win_7 Already Closed')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
