import json
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
from config import METHODS, FIELD_DEFAULT_TYPE
from pydantic.error_wrappers import ValidationError


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.list_input.setSpacing(5)
        self.connect_list_widget(METHODS.keys())
        self.pb_calculate.clicked.connect(self.on_calculate)
        self.method_selected_model, self.method_selected = None, None
        self.text_entry.setText('Здесь будет результат работы программы')
        self.graphWidget = None

    def create_fields_input(
            self,
            titles: list[str],
            values_names: list[str],
            values_default: list[FIELD_DEFAULT_TYPE]
    ):
        self.list_input.clear()
        for i in range(len(titles)):
            self.create_field_input(i, titles[i], values_names[i], values_default[i])

    def create_field_input(
            self,
            field_number: int,
            title: str,
            value_name: str,
            value_default: FIELD_DEFAULT_TYPE = None,
    ):
        item = QListWidgetItem()
        item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.list_input.addItem(item)
        widget = MyWidget(field_number, title, value_name, value_default)
        self.list_input.setItemWidget(item, widget)

    def connect_list_widget(self, methods_names: list) -> None:
        self.list_methods.addItems(methods_names)
        self.list_methods.itemDoubleClicked.connect(self.select_method)

    def select_method(self, item: QListWidgetItem) -> None:
        self.delete_graph()
        self.text_entry.setText('Здесь будет результат работы программы')

        method_title = item.text()
        self.method_selected_model, self.method_selected = METHODS[method_title]
        model_schema = json.loads(self.method_selected_model.schema_json())
        if 'required' in model_schema:
            model_schema.pop('required')
        titles = [value['description'] for value in model_schema['properties'].values()]
        values_names = list(model_schema['properties'].keys())
        values_default = [value.get('default') for value in model_schema['properties'].values()]
        self.create_fields_input(titles, values_names, values_default)

    def get_input_text(self) -> list[str]:
        items = [self.list_input.item(row) for row in range(self.list_input.count())]
        input_values = {
            self.list_input.itemWidget(item).text()[0]: self.list_input.itemWidget(item).text()[1]
            for item in items
        }
        try:
            values_validated = self.method_selected_model.parse_obj(input_values)
        except AttributeError:
            raise ValueError("Ошибка: Ни одного параметра не введено")
        return values_validated

    @classmethod
    def __get_error_message(cls, errors: list):
        error_messages = []
        for error in errors:
            message = error.get('msg')
            message = f"Ошибка валидации типа {message.split()[-1]}" \
                if message.startswith('value is not') else message
            error_messages.append(f"{message}. Поля: {', '.join(error.get('loc'))}")
        return "\n".join(error_messages)

    def on_calculate(self):
        try:
            result = self.method_selected(self.get_input_text())
            if isinstance(result, tuple):
                result, graph = result
                self.layout_output.addWidget(graph)
                self.delete_graph()
                self.graphWidget = graph

        except ValidationError as e:
            result = self.__get_error_message(e.errors())
        except ValueError as e:
            result = str(e)
        except RecursionError:
            result = 'Ошибка: Бесконечный цикл. Проверьте значение шага.'
        self.text_entry.setText(result)

    def delete_graph(self):
        if not self.graphWidget:
            return
        self.layout_output.removeWidget(self.graphWidget)
        self.graphWidget.deleteLater()
        self.graphWidget = None


class MyWidget(QWidget):
    def __init__(
            self,
            field_number: int,
            title: str,
            value_name: str,
            value_default: FIELD_DEFAULT_TYPE = None
    ):
        super().__init__()

        self.label = QLabel()
        self.label.setText(title)
        self.label.setToolTip(value_name)
        self.label.setObjectName(f"label_input_{field_number}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.label.setSizePolicy(size_policy)

        self.lineEdit = QLineEdit()
        self.lineEdit.setObjectName(f"le_input_{field_number}")
        self.lineEdit.setSizePolicy(size_policy)
        if value_default is not None:
            self.lineEdit.setText(str(value_default))

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(self.label, 1)
        layout.addWidget(self.lineEdit, 0, alignment=Qt.AlignmentFlag.AlignRight)

    def text(self):
        return self.label.toolTip(), self.lineEdit.text()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
