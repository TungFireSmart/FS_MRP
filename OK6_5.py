import sys
import mysql.connector

# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QTextEdit
from PyQt6.QtGui import QKeyEvent
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

        self.conn = mysql.connector.connect(user='root', password='btk123456', host='127.0.0.1', database='mrp')
        self.cursor = self.conn.cursor(buffered=True)

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
        search_text = self.uic1.text_search_sp.toPlainText().strip()

        # Connect to the SQLite database
        conn = mysql.connector.connect(user='root', password='btk123456', host='127.0.0.1', database='mrp')
        cursor = conn.cursor(buffered=True)

        # Query the table for any rows where either field1 or field2 contains a substring of the input text
        query = "SELECT * FROM ds_san_pham WHERE model LIKE '%" + search_text + "%' OR ten_san_pham LIKE '%" + search_text + "%'"
        cursor.execute(query)
        results = cursor.fetchall()
        self.uic1.table_sanpham.clearContents()
        if results:
            for i,k in enumerate(results):

                self.uic1.table_sanpham.setItem(i, 0, QTableWidgetItem(k[0]))
                self.uic1.table_sanpham.setItem(i, 1, QTableWidgetItem(k[1]))
                self.uic1.table_sanpham.setItem(i, 2, QTableWidgetItem(k[2]))

            for i in range(0, len(results)):
                text = self.uic1.table_sanpham.item(i, 0).text()
                self.btn = QPushButton()
                self.btn.setText(text)
                self.btn.clicked.connect(self.show_sanpham)
                self.uic1.table_sanpham.setCellWidget(i,0, self.btn)

        else:
            self.uic1.table_sanpham.clearContents()
            self.uic1.table_sanpham.setItem(1, 1, QTableWidgetItem('Không có kết quả phù hợp !!!!'))
            self.uic1.table_sanpham.setItem(2, 1, QTableWidgetItem('Lêu Lêu !!!!'))


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

        self.uic3.but_search_linhkien.clicked.connect(self.search_lk)

    def search_lk(self):
        search_text = self.uic3.search_linhkien.toPlainText().strip()
        # Connect to the SQLite database
        conn = mysql.connector.connect(user='root', password='btk123456', host='127.0.0.1', database='mrp')
        cursor = conn.cursor(buffered=True)

        # Query the table for any rows where either field1 or field2 contains a substring of the input text
        query = "SELECT * FROM chi_tiet_linh_kien WHERE sku LIKE '%" + search_text + "%' OR ten_linh_kien LIKE '%" + search_text + "%' OR part_number LIKE '%" + search_text + "%' OR thong_so_chinh LIKE '%" + search_text + "%'"
        cursor.execute(query)
        results = cursor.fetchall()
        self.uic3.table_dslinhkien.clearContents()


        if results:
            for i,k in enumerate(results):

                self.uic3.table_dslinhkien.setItem(i, 0, QTableWidgetItem(k[0]))
                self.uic3.table_dslinhkien.setItem(i, 1, QTableWidgetItem(k[1]))
                self.uic3.table_dslinhkien.setItem(i, 2, QTableWidgetItem(k[2]))

            for i in range(0, len(results)):
                text = self.uic3.table_dslinhkien.item(i, 0).text()
                self.btn = QPushButton()
                self.btn.setText(text)
                self.btn.clicked.connect(self.show_linhkien)
                self.uic3.table_dslinhkien.setCellWidget(i,0, self.btn)

        else:
            self.uic3.table_dslinhkien.clearContents()
            self.uic3.table_dslinhkien.setItem(1, 1, QTableWidgetItem('Không có kết quả phù hợp !!!!'))
            self.uic3.table_dslinhkien.setItem(2, 1, QTableWidgetItem('Lêu Lêu !!!!'))

    def load_sanpham(self):
        conn = mysql.connector.connect(user='root', password='btk123456', host='127.0.0.1', database='mrp')
        mycur = conn.cursor(buffered=True)

        # file_name = sql_table
        # # Tạo header cho các cột trong bảng
        header = ['Xem chi tiết', 'Tên sản phẩm', 'Version', 'Tồn kho']
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

            for row_number, row_data in enumerate(result):

                # Đoạn này điền thông tin vào từng dòng
                for column_number, data in enumerate(row_data):
                    self.uic1.table_sanpham.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                text = self.uic1.table_sanpham.item(row_number, 0).text()
                self.btn = QPushButton()
                self.btn.setText(text)
                self.btn.clicked.connect(self.show_sanpham)
                self.uic1.table_sanpham.setCellWidget(row_number,0, self.btn)

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

        self.sub_win7 = QMainWindow()
        self.uic7 = Ui_tao_bom()
        self.uic7.setupUi(self.sub_win7)
        self.sub_win7.show()
        self.uic7.but_back.clicked.connect(self.close)
        self.uic7.but_linhkienmoi.clicked.connect(self.themlinhkienmoi)

        # Đoạn này nạp file Bom List lên màn hình, nếu chưa có thì tạo bom list trống

        self.uic7.label_4.setText('Bom list của model: ' + self.current_item)
        tenfile1 = 'bom_' + str(self.current_item).replace('-', '_')
        self.current_file = tenfile1

        # Check if the table exists
        self.cursor.execute("SHOW TABLES LIKE %s", (tenfile1,))
        table_exists = self.cursor.fetchone() is not None

        if table_exists:
            self.load_bom_list_table()
        else:
            # Tạo bom_list theo tên model từ table bom_list_mau
            code = "create table " + tenfile1 + " as select * from bom_list_mau"
            self.cursor.execute(code)
            self.conn.commit()
            self.current_file = tenfile1
            self.load_bom_list_table()

        # Đoạn này load linh kiện vào table widget - Sau này sẽ viết lại, gộp vào def loadlinhkien

        file_name = 'chi_tiet_linh_kien'
        # # Tạo header cho các cột trong bảng
        header = ['SKU', 'Tên vật tư', 'Part number', 'Action']
        self.uic7.table_dslinhkien.setHorizontalHeaderLabels(header)
        try:
            code = "select sku, ten_linh_kien, part_number, thong_so_chinh from " + file_name
            self.cursor.execute(code)

            result = self.cursor.fetchall()
            # show kết quả lên tablewidget

            self.uic7.table_dslinhkien.setRowCount(len(result))  # tạo số row
            self.uic7.table_dslinhkien.setColumnCount(4)  # tạo số column
            self.uic7.table_dslinhkien.setColumnWidth(0, 70)

            self.uic7.table_dslinhkien.setColumnWidth(1, 260)
            self.uic7.table_dslinhkien.setColumnWidth(2, 100)
            self.uic7.table_dslinhkien.setColumnWidth(2, 260)

            for row_number, row_data in enumerate(result):

                # Đoạn này điền thông tin vào từng dòng
                for column_number, data in enumerate(row_data):
                    self.uic7.table_dslinhkien.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                self.btn = QPushButton()
                text = self.uic7.table_dslinhkien.item(row_number, 0).text()
                self.btn.setText(text)
                self.btn.clicked.connect(self.add_lk_vao_bom)
                self.uic7.table_dslinhkien.setCellWidget(row_number, 0, self.btn)

        except:
            self.uic7.label_ketqua.setText('File data error')

    def load_bom_list_table(self):
        self.uic7.table_bom_temp.clearContents()

        code = "select sku, ten_linh_kien, part_number, so_luong from " + self.current_file
        self.cursor.execute(code)
        kq = self.cursor.fetchall()

        header = ['SKU', 'Tên linh kiện', 'Part number', 'Số lượng', 'Action']
        self.uic7.table_bom_temp.setHorizontalHeaderLabels(header)

        self.uic7.table_bom_temp.setRowCount(len(kq))  # tạo số row
        self.uic7.table_bom_temp.setColumnCount(5)  # tạo số column

        self.uic7.table_bom_temp.setColumnWidth(0, 80)
        self.uic7.table_bom_temp.setColumnWidth(1, 360)
        self.uic7.table_bom_temp.setColumnWidth(2, 120)
        self.uic7.table_bom_temp.setColumnWidth(3, 120)
        self.uic7.table_bom_temp.setColumnWidth(4, 120)

        for row_number, row_data in enumerate(kq):

            # Đoạn này điền thông tin vào từng dòng
            for column_number, data in enumerate(row_data):
                self.uic7.table_bom_temp.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            text = str(row_data[0])
            self.btn = QPushButton()
            self.btn.setText(text)
            self.btn.clicked.connect(self.xoa_linhkien)
            self.uic7.table_bom_temp.setCellWidget(row_number, 0, self.btn)

            self.uic7.table_bom_temp.repaint()

    def xoa_linhkien(self):

        selected_row = self.uic7.table_bom_temp.currentRow()
        if selected_row >= 0:
            self.uic7.table_bom_temp.removeRow(selected_row)

        self.uic7.label_ketqua.setText('Đã xóa một linh kiện!')

    def add_lk_vao_bom(self):
        r = self.uic7.table_dslinhkien.currentRow()
        c = self.uic7.table_dslinhkien.currentColumn()
        text = self.uic7.table_dslinhkien.item(r, c).text()

        code = "select sku, ten_linh_kien, part_number, thong_so_chinh, mo_ta_chi_tiet, brand, nha_san_xuat, hinh_anh from chi_tiet_linh_kien where sku like '%" + text + "%'"
        self.cursor.execute(code)
        kq = self.cursor.fetchall()

        code = "insert into " + self.current_file + " (sku, ten_linh_kien, part_number, thong_so_chinh, mo_ta_chi_tiet, brand, nha_san_xuat, hinh_anh) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
        self.cursor.execute(code.format(kq[0][0],kq[0][1],kq[0][2],kq[0][3],kq[0][4],kq[0][5],kq[0][6],kq[0][7]))
        self.conn.commit()

        self.load_bom_list_table()

    def load_linhkien(self, sql_table):

        file_name = sql_table
        # # Tạo header cho các cột trong bảng
        header = ['SKU', 'Tên vật tư', 'Part number', 'Action']
        self.uic3.table_dslinhkien.setHorizontalHeaderLabels(header)
        try:
            code = "select sku, ten_linh_kien, part_number from " + file_name
            self.cursor.execute(code)

            result = mycur.fetchall()
            # show kết quả lên tablewidget

            self.uic3.table_dslinhkien.setRowCount(len(result))  # tạo số row
            self.uic3.table_dslinhkien.setColumnCount(4)  # tạo số column
            self.uic3.table_dslinhkien.setColumnWidth(0, 100)

            self.uic3.table_dslinhkien.setColumnWidth(1, 360)
            self.uic3.table_dslinhkien.setColumnWidth(2, 120)
            self.uic3.table_dslinhkien.setColumnWidth(3, 120)

            for row_number, row_data in enumerate(result):

                # Đoạn này điền thông tin vào từng dòng
                for column_number, data in enumerate(row_data):
                    self.uic3.table_dslinhkien.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                text = self.uic3.table_dslinhkien.item(row_number, 0).text()
                self.btn = QPushButton()
                self.btn.setText(text)
                self.btn.clicked.connect(self.show_linhkien)
                self.uic3.table_dslinhkien.setCellWidget(row_number, 0, self.btn)


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
