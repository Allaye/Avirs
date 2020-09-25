import base64
import os
import io
import random
import sys
import cv2 as cv
import style
import maindb
import qimage2ndarray
import warnings
from PIL import Image, ImageQt
from PyQt5.Qt import QT_VERSION_STR

import back_to_back as b2b
import numpy as np
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QPixmap, QFont, QImage, QIcon
from PyQt5.QtWidgets import *

warnings.filterwarnings('ignore')
index = 0
raange = 0


class aboutwindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle('About Avirs')
        self.setGeometry(750, 150, 450, 600)
        self.setFixedSize(self.size())
        self.parent = parent
        self.setWindowIcon(QIcon('cctv (1).png'))
        self.ui()
        self.label()

    def ui(self):
        self.show()

    def label(self):
        self.label = QLabel("AVIRS is an Automated vehicle identification and recognition system, as part o the "
                            "requirement by the university (Ghana Technology University) requrement, KOLADE GIDEON "
                            "and CHARLES ASARE have embark on the developemnt of this system to help the police "
                            "service in ALAJO ACCRA to detect and recognize vehicles of interest, this system helps "
                            "eliminate the use of manpower for scanning through video and image feeds in other to "
                            "identify vehicles of interest.", self)
        self.inputbox = QLineEdit(self)
        self.inputbox.setText("AVIRS is an Automated vehicle identification and recognition system, as part o the "
                              "requirement by the university (Ghana Technology University) requrement, KOLADE GIDEON "
                              "and CHARLES ASARE have embark on the developemnt of this system to help the police "
                              "service in ALAJO ACCRA to detect and recognize vehicles of interest, this system helps "
                              "eliminate the use of inefficient manpower for scanning through huge video and image feeds in other to "
                              "identify vehicles of interest.")

        font = QFont('Arial', 10, QFont.Bold)
        self.label.setWordWrap(True)
        # self.label.setGeometry(100, 100, 230, 230)
        self.label.resize(110, 80)
        self.label.setAlignment(QtCore.Qt.AlignAbsolute)
        self.label.setFont(font)

        self.mlayout = QHBoxLayout()

        # self.label.setStyleSheet("background-color: lightgreen")
        # self.label.setStyleSheet("background-color: yellow; border: 1px solid black; ")
        self.label.setStyleSheet("border: 5px solid black; border-radius: 5px; ")
        self.mlayout.addWidget(self.label)
        self.setLayout(self.mlayout)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent.setWindowOpacity(1.)


class helpwindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle('Avirs Help')
        self.setGeometry(750, 150, 450, 600)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('cctv (1).png'))
        self.parent = parent
        self.label()
        self.ui()

    def ui(self):
        self.show()

    def label(self):
        self.label = QLabel("The File menu contains one action button that can be use to import single or multiple image or video "
                            "files. \b "
                            "The Scan button is used to process the current image in view and all the information "
                            "retrieved are sent into the database. \b"
                            "The Next Button is used to move forward through the list of images in the system. \b"
                            "The Back Button is used to move backward through the list of images in the system.\b"
                            "The hits button displays the amount of hits the system had at a particular instance.\b"
                            "Total scan buttons displays theb amount of scan the system has performed over a perform "
                            "of time. \b", self)

        font = QFont('Arial', 10, QFont.Bold)
        self.label.setWordWrap(True)

        # self.label.setGeometry(100, 100, 230, 230)
        self.label.resize(110, 80)
        self.label.setAlignment(QtCore.Qt.AlignAbsolute)
        self.label.setFont(font)

        self.mlayout = QHBoxLayout()

        # self.label.setStyleSheet("background-color: lightgreen")
        # self.label.setStyleSheet("background-color: yellow; border: 1px solid black; ")
        self.label.setStyleSheet("border: 5px solid black; border-radius: 5px; ")
        self.mlayout.addWidget(self.label)
        self.setLayout(self.mlayout)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent.setWindowOpacity(1.)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Avirs')
        self.setGeometry(350, 250, 1350, 700)
        self.setFixedSize(self.size())
        self.timer = QTimer(self)
        self.setWindowIcon(QIcon('cctv (1).png'))

        # adding action to timer
        self.timer.timeout.connect(self.showTime)
        # update the timer every second
        self.timer.start(1000)
        self.date = QDate.currentDate()
        self.ui()
        self.setWindowOpacity(5.4)
        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        self.setAutoFillBackground(True)
        self.flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(self.flags)
        self.setStyleSheet("background-color:#f5f7f7;")
        self.hitvalue = 0
        print(self.scan_img_label.size())

    def ui(self):
        self.ui_layouts()
        self.ui_widgets()
        self.style_ui_widgets()
        self.fetchdata()
        # self.b2bfrontview()

    def ui_layouts(self):
        self.mainlayout = QHBoxLayout()
        self.left_group_layout = QGroupBox('')
        self.left_main_layout = QVBoxLayout()
        self.right_main_layout = QVBoxLayout()
        self.left_top_layout = QHBoxLayout()
        self.left_middle_layout = QHBoxLayout()
        self.left_middle_left_layout = QVBoxLayout()
        self.left_middle_right_layout = QVBoxLayout()
        self.left_down_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.right_down_layout = QHBoxLayout()
        self.left_group_layout.setLayout(self.left_middle_layout)
        self.left_middle_layout.setSpacing(40)
        self.left_middle_layout.addLayout(self.left_middle_left_layout, 50)
        self.left_middle_layout.addLayout(self.left_middle_right_layout, 50)
        self.left_main_layout.addLayout(self.left_top_layout, 10)
        self.left_main_layout.addWidget(self.left_group_layout, 50)
        self.left_main_layout.addLayout(self.left_down_layout, 40)
        self.right_main_layout.addLayout(self.right_top_layout, 10)
        self.right_main_layout.addLayout(self.right_middle_layout, 50)
        self.right_main_layout.addLayout(self.right_down_layout, 20)
        self.mainlayout.addLayout(self.left_main_layout, 10)
        self.mainlayout.addLayout(self.right_main_layout, 90)
        self.mainlayout.setSpacing(10)

        self.setLayout(self.mainlayout)

    def helpwin(self):
        self.newwin = helpwindow(self)
        self.setWindowOpacity(0.)

    def aboutwin(self):
        self.newwin = aboutwindow(self)
        self.setWindowOpacity(0.)

    def ui_widgets(self):
        self.mainMenu = QMenuBar()
        self.project = QLabel()
        self.fileMenu = self.mainMenu.addMenu('File')
        self.fileMenu.addAction('Add File')
        self.fileMenu.setIcon(QIcon('folder.png'))
        # self.fileMenu.setIconSize(QtCore.QSize(90, 70))
        self.help = self.mainMenu.addMenu('Help')
        self.help.aboutToShow.connect(self.helpwin)
        self.help.setIcon(QIcon('question (1).png'))
        self.about = self.mainMenu.addMenu('About US')
        self.about.aboutToShow.connect(self.aboutwin)
        self.about.setIcon(QIcon('two.png'))

        self.fileMenu.triggered.connect(self.loadImageFromFile)

        self.back_btn = QPushButton()
        self.search_btn = QPushButton()
        self.scan_btn = QPushButton()
        self.scan_btn.clicked.connect(self.b2bfrontview)
        self.next_btn = QPushButton()
        self.next_btn.clicked.connect(self.nextimage)
        self.back_btn.clicked.connect(self.previousimage)
        self.hits_btn = QPushButton('Nextbtn')
        self.gui_label = QLabel()
        self.totalscan_btn = QPushButton()
        self.left_main_layout.addWidget(self.mainMenu)
        self.left_top_layout.addWidget(self.project)
        #  self.left_top_layout.addWidget(self.editMenu)
        self.left_middle_left_layout.addStretch(15)
        # self.left_middle_left_layout.setSpacing(10)
        self.left_middle_left_layout.addWidget(self.scan_btn)
        self.left_middle_left_layout.addStretch(10)
        self.left_middle_left_layout.addWidget(self.search_btn)
        self.left_middle_left_layout.addStretch(10)
        self.left_middle_left_layout.addWidget(self.hits_btn)
        self.left_middle_right_layout.addStretch(15)
        self.left_middle_right_layout.addWidget(self.next_btn)
        self.left_middle_right_layout.addStretch(10)
        self.left_middle_right_layout.addWidget(self.back_btn)
        self.left_middle_right_layout.addStretch(10)
        self.left_middle_right_layout.addWidget(self.totalscan_btn)

        self.hits_tb = QTableWidget()
        self.left_down_layout.addStretch(0)
        self.left_down_layout.addWidget(self.hits_tb)
        self.hits_tb.setColumnCount(5)
        self.hits_tb.setFont(QFont('Arial', 10, QFont.Bold))
        self.hits_tb.setHorizontalHeaderLabels(['Logid', 'Vehicle_number', 'Location',
                                                'Date_Time', 'Vehicle_color'])
        self.hits_tb.horizontalHeader().setStretchLastSection(True)
        self.hits_tb.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.left_down_layout.addStretch(4)
        self.scan_img_label = QLabel()
        # self.scan_img_label.setPixmap(QPixmap('009.jpg'))
        self.right_middle_layout.addWidget(self.scan_img_label)
        self.scan_img_label.setScaledContents(True)
        # self.scan_img_label.setFixedSize(self.scan_img_label.size())
        print(self.scan_img_label.size())
        self.scan_img_label.setFixedSize(800, 390)
        # self.scan_img_label.adjustSize()
        print(self.scan_img_label.size())

        self.vehicle_table = QTableWidget()
        self.vehicle_table.setColumnCount(6)
        self.vehicle_table.setFont(QFont('Arial', 8, QFont.Bold))
        self.vehicle_table.setHorizontalHeaderLabels(['Scanid', 'Vehicle_number', 'Vehicle_type', 'Cam_loc',
                                                      'Date_Time', 'Vehicle_num_pic'])
        self.vehicle_table.horizontalHeader().setStretchLastSection(True)
        self.vehicle_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.db_table.
        self.right_down_layout.addWidget(self.vehicle_table)
        self.time_label = QPushButton()
        self.date_label = QPushButton()
        self.right_top_layout.addStretch()
        self.right_top_layout.addWidget(self.time_label)
        self.right_top_layout.addWidget(self.date_label)

    def style_ui_widgets(self):
        font = QFont('Arial', 20, QFont.Bold)
        self.left_group_layout.setStyleSheet(style.groupboxStyle())

        self.scan_btn.setStyleSheet("background-color: #d8ffcf;")
        self.scan_btn.setIcon(QIcon('cctv.png'))
        self.scan_btn.setIconSize(QtCore.QSize(90, 70))
        self.hits_btn.setStyleSheet("background-color: #b9a3c7 ;")
        self.next_btn.setStyleSheet("background-color: #cbc6f7")
        self.next_btn.setIcon(QIcon('next.png'))
        self.next_btn.setIconSize(QtCore.QSize(90, 70))
        self.back_btn.setStyleSheet("background-color: #b3ffff;")
        self.back_btn.setIcon(QIcon('back.png'))
        self.back_btn.setIconSize(QtCore.QSize(90, 70))
        self.totalscan_btn.setStyleSheet("background-color:#ffd9cc;")
        self.time_label.setFont(font)
        self.project.setFont(QFont('Arial', 10, QFont.Bold))
        self.time_label.setStyleSheet("border-radius:15px;")
        self.vehicle_table.setStyleSheet(style.groupboxStyle())
        self.hits_tb.setStyleSheet(style.groupboxStyle())
        self.vehicle_table.setStyleSheet("background-color: #f2f2f2; border-radius:20px; border:5px solid gray;")
        self.hits_tb.setStyleSheet("background-color: #f2f2f2; border-radius:20px; border:5px solid gray;")
        self.time_label.setStyleSheet("border:5px solid gray; border-radius:95px;background-color: #cbc6f7")
        self.date_label.setStyleSheet("border:5px solid gray; border-radius:95px;background-color: #cbc6f7")
        self.project.setStyleSheet("border:5px solid gray; border-radius:95px;background-color: #cbc6f7")
        self.search_btn.setStyleSheet("border:0px #D3D3D3; border-radius:0px;background-color: #D3D3D3")
        self.search_btn.setStyleSheet('QPushButton {color: #f6f6f6}')

        self.date_label.setFont(font)
        self.scan_btn.setFont(QFont('Arial', 20, QFont.Bold))
        self.next_btn.setFont(QFont('Arial', 20, QFont.Bold))
        self.search_btn.setFont(QFont('Arial', 40, QFont.Courier))
        self.hits_btn.setFont(QFont('Arial', 40, QFont.Bold))
        self.totalscan_btn.setFont(QFont('Arial', 40, QFont.Bold))
        self.back_btn.setFont(QFont('Arial', 20, QFont.Bold))
        self.scan_btn.setText('Scan')
        self.next_btn.setText('Next')
        self.search_btn.setText('Find')
        self.search_btn.setEnabled(False)

        self.hits_btn.setText('Hits')
        self.back_btn.setText('Back')
        self.project.setText('Automated Vehicle Identification and Recognition System')

        # self.qr_label.setFont(font)
        # self.date_label.resize(80, 80)d
        # self.scan_img_label.resize(300, 300)
        # self.scan_btn.resize(120, 120)
        self.next_btn.resize(120, 120)

        self.scan_img_label.setStyleSheet("border:5px solid gray; border-radius:15px;")

        self.date_label.setText(self.date.toString(Qt.ISODate))
        # self.date_label.setStyleSheet("Backgroundcolor: (255, 255, 255)")

        self.date_label.setGeometry(220, 150, 100, 100)
        self.time_label.setGeometry(200, 150, 100, 100)

    #   self.qr_label.resize(300, 300)
    # self.qr_label.setGeometry(120, 120, 430, 430)
    #  self.qr_label.setStyleSheet("border: 1px solid yellow; border-radius: 150px; ")

    # setting radius and border
    # self.date_label.setStyleSheet("border-radius : 50; border: 2px solid black")
    # self.time_label.setStyleSheet("border-radius : 50; border: 2px solid black")
    # self.date_label.setStyleSheet("background-color: yellow; border: 1px solid black; ")

    def showTime(self):
        # getting current time
        self.current_time = QTime.currentTime()

        # converting QTime object to string
        self.label_time = self.current_time.toString('hh:mm:ss')

        # showing it to the label
        self.time_label.setText(self.label_time)

    def loadImageFromFile(self, fileName=""):
        """ Load an image from file.
        """
        global index, raange
        self.url, _ = QFileDialog.getOpenFileNames(self, 'Open file', 'c:/', "Image files (*.jpg *.gif *.png)")
        print(type(list(self.url)))
        for i in range(len(self.url)):
            self.raange = i
        # self.url = self.url[0]
        self.index = 0
        print(self.url)
        print(self.url[self.index])
        self.urlfirst = self.url[self.index]
        self.content = QPixmap(self.urlfirst)
        self.scan_img_label.setPixmap(self.content)

    def b2bfrontview(self):
        self.test_image_path = self.url[self.index]
        wpod_net_path = "wpod-net.json"
        wpod_net = b2b.load_model(wpod_net_path)
        self.vehicle, self.LpImg, self.cor = b2b.get_plate(self.test_image_path)
        self.leplate = self.LpImg[0]  # send this to the database
        # self.binaryleplate = base64.b64encode(self.leplate)

        self.boundingbox_image = b2b.draw_box(self.test_image_path, self.cor)  # display this image
        # self.boundingbox_image = cv.cvtColor(self.boundingbox_image, cv.COLOR_BGR2RGB)
        self.image, self.x, self.y, self.a, self.b = b2b.draw_plate(self.test_image_path, self.cor)
        self.qImg = qimage2ndarray.array2qimage(self.image)
        self.cropped_plate = self.qImg.copy(self.x, self.y, self.a, self.b)
        self.cropped_plate = qimage2ndarray.byte_view(self.cropped_plate)
        self.scan_img_label.setPixmap(QPixmap(self.qImg))
        self.cropped_plate = Image.fromarray(self.cropped_plate)
        self.cropped_plate.save('cropped_plat_e.png')
        self.imagecropped = Image.open('cropped_plat_e.png')
        f = io.BytesIO()
        self.imagecropped.save(f, format="PNG")
        self.img_bytes = f.getvalue()
        self.b2bbackview()
        self.hits_tb.clearContents()
        self.vehicle_table.clearContents()
        self.fetchdata()

        if self.final_license_number in self.hitnumbers:
            self.hitvalue += 1
            self.hits_btn.setText(str(self.hitvalue) + " " + "Hit")
        else:
            self.hits_btn.setText(str(self.hitvalue) + " " + "Hit")

    def b2bbackview(self):
        self.json_file = open('MobileNets_character_recognition.json', 'r')
        self.load_model_json = self.json_file.read()
        self.json_file.close()
        self.model = b2b.model_from_json(self.load_model_json)
        self.model.load_weights("License_character_recognition_weight.h5")
        print("[INFO] Model loaded successfully...")
        self.labels = b2b.LabelEncoder()
        self.labels.classes_ = np.load('license_character_classes.npy')
        if len(self.LpImg):
            # check if there is at least one license image
            # Scales, calculates absolute values, and converts the result to 8-bit.
            # self.cropped_plate = self.qImg.copy(self.x, self.y, self.a, self.b)
            self.plate_image = cv.convertScaleAbs(self.LpImg[0], alpha=255.0)

            # convert to grayscale and blur the image
            gray = cv.cvtColor(self.plate_image, cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(gray, (7, 7), 0)

            # Applied inversed thresh_binary
            binary = cv.threshold(blur, 180, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

            kernel3 = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
            thre_mor = cv.morphologyEx(binary, cv.MORPH_DILATE, kernel3)
        cont, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        test_roi = self.plate_image.copy()
        self.crop_characters = []
        for c in b2b.sort_contours(cont):
            (x, y, w, h) = cv.boundingRect(c)
            ratio = h / w
            if 1 <= ratio <= 3.5:  # Only select contour with defined ratio
                if h / self.plate_image.shape[0] >= 0.5:  # Select contour which has the height larger than 50% of
                    # the plate
                    # Draw bounding box arroung digit number
                    cv.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    # Sperate number and gibe prediction
                    curr_num = thre_mor[y:y + h, x:x + w]
                    curr_num = cv.resize(curr_num, dsize=(b2b.digit_w, b2b.digit_h))
                    _, curr_num = cv.threshold(curr_num, 220, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
                    self.crop_characters.append(curr_num)
        self.final_license_number = ''
        if len(self.crop_characters) >= 3:
            for i, character in enumerate(self.crop_characters):
                title = np.array2string(b2b.predict_from_model(character, self.model, self.labels))
                self.final_license_number += title.strip("'[]")
        else:
            print('error with the license plate')

        self.veh_type, self.cam_loc, self.dt = self.randomdetails()
        maindb.vehicledetailsquery(self.final_license_number, self.veh_type, self.cam_loc,
                                   self.dt, self.img_bytes)
        print(self.final_license_number)

    def randomdetails(self):
        vehicles = ['Car', 'Bus', 'Car', 'Car', 'pickup', 'Car']
        camera = ['Cam 1', 'Cam 2', 'Cam 3']
        self.veh_type = random.choice(vehicles)
        self.cam_loc = random.choice(camera)
        d = self.date_label.text()
        t = self.time_label.text()
        self.dt = str(d) + '-' + str(t)
        return self.veh_type, self.cam_loc, self.dt

    def previousimage(self):
        if self.index != self.raange:
            print(self.index)
            print(self.raange)
            self.index -= 1
            print('Printing fro nextfrontion')
            print(self.url)
            print(self.index)
            print('---------------------------------------------')
            print(self.url[self.index])
            # self.scan_img_label.clear()
            self.urlfirst = self.url[self.index]
            self.content = QPixmap(self.urlfirst)
            self.scan_img_label.setPixmap(self.content)
        else:
            self.index = 0
            self.urlfirst = self.url[self.index]
            self.content = QPixmap(self.urlfirst)
            self.scan_img_label.setPixmap(self.content)

    def nextimage(self):
        #  self.img_url = self.url
        if self.index != self.raange:
            print(self.index)
            print(self.raange)
            self.index += 1
            print('Printing fro nextfrontion')
            print(self.url)
            print(self.index)
            print('---------------------------------------------')
            print(self.url[self.index])
            # self.scan_img_label.clear()
            self.urlfirst = self.url[self.index]
            self.scan_img_label.clear()
            self.content = QPixmap(self.urlfirst)
            self.scan_img_label.setPixmap(self.content)
        else:
            self.index = 0
            self.urlfirst = self.url[self.index]
            self.content = QPixmap(self.urlfirst)
            self.scan_img_label.setPixmap(self.content)

    def storedata(self):
        pass

    def fetchdata(self):
        maindb.createtb()
        self.hits_data = maindb.vehicle_hitstbquery()
        self.vehicle_data = maindb.vehicletbquery()
        self.hitnumbers = []
        for self.row_id, self.row_data in enumerate(self.hits_data):
            self.hits_tb.insertRow(self.row_id)
            for self.column_id, self.column_data in enumerate(self.row_data):
                self.hits_tb.setItem(self.row_id, self.column_id, QTableWidgetItem(str(self.column_data)))
                if self.column_id == 1:
                    self.hitnumbers.append(self.column_data)
        print(self.hitnumbers)
        for self.row_id, self.row_data in enumerate(self.vehicle_data):
            self.vehicle_table.insertRow(self.row_id)
            for self.column_id, self.column_data in enumerate(self.row_data):
                if self.column_id == 5:

                    pix = QPixmap()
                    self.veh_img = QLabel('Image')
                    if pix.loadFromData(self.column_data):
                        self.veh_img.setPixmap(pix)
                        self.veh_img.setScaledContents(True)
                        self.vehicle_table.setCellWidget(self.row_id, self.column_id, self.veh_img)
                else:
                    self.vehicle_table.setItem(self.row_id, self.column_id, QTableWidgetItem(str(self.column_data)))


def main():
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
