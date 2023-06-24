import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QListWidgetItem,
    QLineEdit,
    QWidget,
    QLabel,
    QSizePolicy,
    QHBoxLayout,
)

from PyQt6.QtCore import Qt

from ui.main_window_ui import Ui_MainWindow
from config import METHODS_NAMES


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_list_widget()
        self.create_fields_input(METHODS_NAMES)

    def create_fields_input(self, titles: list):
        for i in range(len(titles)):
            item = QListWidgetItem()  # - str(i)
            item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.list_input.addItem(item)
            widget = MyWidget(i, titles[i])
            self.list_input.setItemWidget(item, widget)

    def create_field_input(self, title, field_number=0):
        text_input = QLineEdit(parent=self.centralwidget)
        text_input.setObjectName(f"text_input_{field_number}")
        text_input.setText(title)
        text_input.setReadOnly(True)
        self.layout_text_input.addWidget(text_input)

    def connect_list_widget(self) -> None:
        self.list_methods.addItems(METHODS_NAMES)
        self.list_methods.itemDoubleClicked.connect(self.select_method)

    def select_method(self, item: QListWidgetItem) -> None:
        print(item.text())


class MyWidget(QWidget):
    def __init__(self, field_number: int, title: str):
        super().__init__()

        self.flag = True

        self.label = QLabel()
        self.label.setText(title)
        self.label.setObjectName(f"label_input_{field_number}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.label.setSizePolicy(size_policy)
        # self.label.setStyleSheet("background-color: #E7F7F4;")

        self.lineEdit = QLineEdit()
        self.lineEdit.setObjectName(f"le_input_{field_number}")

        # self.lineEdit.setEnabled(False)
        # self.lineEdit..connect(self.onClicked)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.label, 1)
        layout.addWidget(self.lineEdit, 0, alignment=Qt.AlignmentFlag.AlignRight)


    def onClicked(self):
        print('sdf')

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
