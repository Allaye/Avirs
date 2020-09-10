def groupboxStyle():
    return """
        QGroupBox {
        background-color:#f5f7f7;
        font:10pt Times Bold;
        color:white;
        border:5px solid gray;
        border-radius:15px;
        }

    """


'''
 QPushButton {
            color: grey;
            border-image: url(/home/kamlie/code/button.png) 3 10 3 10;
            border-top: 3px transparent;
            border-bottom: 3px transparent;
            border-right: 10px transparent;
            border-left: 10px transparent;
        }
'''


def groupboxbtn():
    return """
        QPushButton {
        border-radius: 50%;
        #background-color: Black;
        font-size: 24px;
        
        }

    """


def mainwindow():
    return """
    QGroupBox {
        background-color:#fcc324;
        font:15pt Times Bold;
        color:white;
        border:2px solid gray;
        border-radius:15px;
        }

    
    
    """


def progressBarStyle():
    return """
        QProgressBar {
        border: 1px solid #bbb;
        background: white;
        height: 10px;
        border-radius: 6px;
        
        }
    """


def playListStyle():
    return """
        QListWidget{
        background-color:#fff;
        border-radius: 10px;
        border:3px solid blue;
        
        }
    
    
    
    """
def get_veh_img(self, image):
    self.image = image
    self.veh_img = QLabel('Image')
    self.pixmap = QPixmap()
    self.pixmap.loadFromData(base64.b64decode(self.image), 'jpg')
    self.veh_img.setPixmap(self.pixmap)
    return self.veh_img


    for self.row_id, self.row_data in enumerate(self.vehicle_data):
        self.vehicle_table.insertRow(self.row_id)
        for self.column_id, self.column_data in enumerate(self.row_data):
            if self.column_id == 4:
                self.img = self.get_veh_img(self.column_data)
                print(type(self.img))
                print(type(self.column_data))

                self.vehicle_table.setCellWidget(self.row_id, self.column_id, self.img)
            else:
                self.vehicle_table.setItem(self.row_id, self.column_id, QTableWidgetItem(str(self.column_data)))