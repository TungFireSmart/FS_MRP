# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_sanpham = QtWidgets.QPushButton(parent=self.centralwidget)
        self.but_sanpham.setGeometry(QtCore.QRect(10, 20, 120, 35))
        self.but_sanpham.setObjectName("but_sanpham")
        self.but_sanxuat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.but_sanxuat.setGeometry(QtCore.QRect(140, 20, 120, 35))
        self.but_sanxuat.setObjectName("but_sanxuat")
        self.but_kho = QtWidgets.QPushButton(parent=self.centralwidget)
        self.but_kho.setGeometry(QtCore.QRect(270, 20, 120, 35))
        self.but_kho.setObjectName("but_kho")
        self.but_banhang = QtWidgets.QPushButton(parent=self.centralwidget)
        self.but_banhang.setGeometry(QtCore.QRect(400, 20, 120, 35))
        self.but_banhang.setObjectName("but_banhang")
        self.text_login = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_login.setGeometry(QtCore.QRect(560, 20, 150, 35))
        self.text_login.setObjectName("text_login")
        self.but_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.but_login.setGeometry(QtCore.QRect(720, 20, 75, 35))
        self.but_login.setObjectName("but_login")
        self.text_khsx = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_khsx.setGeometry(QtCore.QRect(20, 110, 221, 431))
        self.text_khsx.setObjectName("text_khsx")
        self.text_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(270, 110, 501, 121))
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(270, 250, 501, 131))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(270, 400, 501, 141))
        self.text_4.setObjectName("text_4")
        self.lable_date = QtWidgets.QLabel(parent=self.centralwidget)
        self.lable_date.setGeometry(QtCore.QRect(50, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lable_date.setFont(font)
        self.lable_date.setObjectName("lable_date")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuS_n_ph_m = QtWidgets.QMenu(parent=self.menubar)
        self.menuS_n_ph_m.setObjectName("menuS_n_ph_m")
        self.menuS_n_xu_t = QtWidgets.QMenu(parent=self.menubar)
        self.menuS_n_xu_t.setObjectName("menuS_n_xu_t")
        self.menuQu_n_l_kho = QtWidgets.QMenu(parent=self.menubar)
        self.menuQu_n_l_kho.setObjectName("menuQu_n_l_kho")
        self.menuB_n_h_ng = QtWidgets.QMenu(parent=self.menubar)
        self.menuB_n_h_ng.setObjectName("menuB_n_h_ng")
        self.menuTr_gi_p = QtWidgets.QMenu(parent=self.menubar)
        self.menuTr_gi_p.setObjectName("menuTr_gi_p")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_sanphammoi = QtGui.QAction(parent=MainWindow)
        self.action_sanphammoi.setObjectName("action_sanphammoi")
        self.action_sanpham = QtGui.QAction(parent=MainWindow)
        self.action_sanpham.setObjectName("action_sanpham")
        self.action_linhkien = QtGui.QAction(parent=MainWindow)
        self.action_linhkien.setObjectName("action_linhkien")
        self.action_khsx = QtGui.QAction(parent=MainWindow)
        self.action_khsx.setObjectName("action_khsx")
        self.action_lsx = QtGui.QAction(parent=MainWindow)
        self.action_lsx.setObjectName("action_lsx")
        self.action_test = QtGui.QAction(parent=MainWindow)
        self.action_test.setObjectName("action_test")
        self.action_nhapkho = QtGui.QAction(parent=MainWindow)
        self.action_nhapkho.setObjectName("action_nhapkho")
        self.action_xuatkho = QtGui.QAction(parent=MainWindow)
        self.action_xuatkho.setObjectName("action_xuatkho")
        self.action_dathang = QtGui.QAction(parent=MainWindow)
        self.action_dathang.setObjectName("action_dathang")
        self.action_lktk = QtGui.QAction(parent=MainWindow)
        self.action_lktk.setObjectName("action_lktk")
        self.action_bg = QtGui.QAction(parent=MainWindow)
        self.action_bg.setObjectName("action_bg")
        self.action_ddh = QtGui.QAction(parent=MainWindow)
        self.action_ddh.setObjectName("action_ddh")
        self.action_bh = QtGui.QAction(parent=MainWindow)
        self.action_bh.setObjectName("action_bh")
        self.action_dskh = QtGui.QAction(parent=MainWindow)
        self.action_dskh.setObjectName("action_dskh")
        self.action_hdcd = QtGui.QAction(parent=MainWindow)
        self.action_hdcd.setObjectName("action_hdcd")
        self.action_hdsd = QtGui.QAction(parent=MainWindow)
        self.action_hdsd.setObjectName("action_hdsd")
        self.actionUpdate = QtGui.QAction(parent=MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionK_t_th_c = QtGui.QAction(parent=MainWindow)
        self.actionK_t_th_c.setObjectName("actionK_t_th_c")
        self.actionNh_cung_c_p = QtGui.QAction(parent=MainWindow)
        self.actionNh_cung_c_p.setObjectName("actionNh_cung_c_p")
        self.menuS_n_ph_m.addAction(self.action_sanphammoi)
        self.menuS_n_ph_m.addAction(self.action_sanpham)
        self.menuS_n_ph_m.addSeparator()
        self.menuS_n_ph_m.addAction(self.action_linhkien)
        self.menuS_n_ph_m.addSeparator()
        self.menuS_n_ph_m.addAction(self.actionK_t_th_c)
        self.menuS_n_xu_t.addAction(self.action_khsx)
        self.menuS_n_xu_t.addAction(self.action_lsx)
        self.menuS_n_xu_t.addSeparator()
        self.menuS_n_xu_t.addAction(self.action_test)
        self.menuQu_n_l_kho.addAction(self.action_nhapkho)
        self.menuQu_n_l_kho.addAction(self.action_xuatkho)
        self.menuQu_n_l_kho.addSeparator()
        self.menuQu_n_l_kho.addAction(self.action_dathang)
        self.menuQu_n_l_kho.addAction(self.action_lktk)
        self.menuQu_n_l_kho.addSeparator()
        self.menuQu_n_l_kho.addAction(self.actionNh_cung_c_p)
        self.menuB_n_h_ng.addAction(self.action_bg)
        self.menuB_n_h_ng.addAction(self.action_ddh)
        self.menuB_n_h_ng.addSeparator()
        self.menuB_n_h_ng.addAction(self.action_bh)
        self.menuB_n_h_ng.addSeparator()
        self.menuB_n_h_ng.addAction(self.action_dskh)
        self.menuTr_gi_p.addAction(self.action_hdcd)
        self.menuTr_gi_p.addAction(self.action_hdsd)
        self.menuTr_gi_p.addSeparator()
        self.menuTr_gi_p.addAction(self.actionUpdate)
        self.menubar.addAction(self.menuS_n_ph_m.menuAction())
        self.menubar.addAction(self.menuS_n_xu_t.menuAction())
        self.menubar.addAction(self.menuQu_n_l_kho.menuAction())
        self.menubar.addAction(self.menuB_n_h_ng.menuAction())
        self.menubar.addAction(self.menuTr_gi_p.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FSMRP - phần mềm quản lý sản xuất FireSmart"))
        self.but_sanpham.setText(_translate("MainWindow", "Sản phẩm"))
        self.but_sanxuat.setText(_translate("MainWindow", "Sản xuất"))
        self.but_kho.setText(_translate("MainWindow", "Quản lý kho"))
        self.but_banhang.setText(_translate("MainWindow", "Bán hàng"))
        self.but_login.setText(_translate("MainWindow", "Login"))
        self.text_khsx.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kế hoạch sản xuất trong ngày</p></body></html>"))
        self.text_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sản phẩm đang test / đang bảo hành</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nguyên vật liệu trên đường về kho</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Biểu đồ thống kê:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Mức độ đạt kế hoạch sản xuất</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Mức độ đạt kế hoạch bán hàng</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Báo xanh khi đạt điểm hòa vốn</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Báo đỏ khi chậm kế hoạch hoặc doanh thu bán hàng dưới điểm hòa vốn</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lable_date.setText(_translate("MainWindow", "Ngày / tháng / năm"))
        self.menuS_n_ph_m.setTitle(_translate("MainWindow", "Sản phẩm"))
        self.menuS_n_xu_t.setTitle(_translate("MainWindow", "Sản xuất"))
        self.menuQu_n_l_kho.setTitle(_translate("MainWindow", "Quản lý kho"))
        self.menuB_n_h_ng.setTitle(_translate("MainWindow", "Bán hàng"))
        self.menuTr_gi_p.setTitle(_translate("MainWindow", "Trợ giúp"))
        self.action_sanphammoi.setText(_translate("MainWindow", "Sản phẩm mới"))
        self.action_sanpham.setText(_translate("MainWindow", "Danh sách sản phẩm"))
        self.action_linhkien.setText(_translate("MainWindow", "Linh kiện"))
        self.action_khsx.setText(_translate("MainWindow", "Kế hoạch SX"))
        self.action_lsx.setText(_translate("MainWindow", "Lệnh sản xuất"))
        self.action_test.setText(_translate("MainWindow", "Test QC"))
        self.action_nhapkho.setText(_translate("MainWindow", "Nhập kho"))
        self.action_xuatkho.setText(_translate("MainWindow", "Xuất kho"))
        self.action_dathang.setText(_translate("MainWindow", "Đặt hàng linh kiện"))
        self.action_lktk.setText(_translate("MainWindow", "Linh kiện tồn kho"))
        self.action_bg.setText(_translate("MainWindow", "Báo giá"))
        self.action_ddh.setText(_translate("MainWindow", "Đơn đặt hàng"))
        self.action_bh.setText(_translate("MainWindow", "Sản phẩm bảo hành"))
        self.action_dskh.setText(_translate("MainWindow", "Danh sách khách hàng"))
        self.action_hdcd.setText(_translate("MainWindow", "Hướng dẫn cài đặt"))
        self.action_hdsd.setText(_translate("MainWindow", "Hướng dẫn sử dụng"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionK_t_th_c.setText(_translate("MainWindow", "Kết thúc"))
        self.actionNh_cung_c_p.setText(_translate("MainWindow", "Nhà cung cấp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
