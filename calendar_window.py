import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QListWidget, QVBoxLayout, QDialog, QLabel
from qt import Ui_MainWindow
from database import Database


class TaskDialog(QDialog):
    def __init__(self, tasks, parent=None):
        super(TaskDialog, self).__init__(parent)
        self.setWindowTitle('Выберите задачи')
        layout = QVBoxLayout()

        self.task_list = QListWidget()
        self.task_list.addItems([f'{task[1]} - {task[2]}' for task in tasks])
        self.task_list.itemClicked.connect(self.task_clicked)

        self.assign_button = QPushButton('Назначить')
        self.assign_button.clicked.connect(self.accept)

        layout.addWidget(self.task_list)
        layout.addWidget(self.assign_button)
        self.setLayout(layout)

        self.selected_tasks = []

    def task_clicked(self, item):
        if item.isSelected():
            self.selected_tasks.append(item.text())
        else:
            self.selected_tasks.remove(item.text())


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.db = Database()

    def initUI(self):
        self.setWindowTitle('Taski')
        self.all_dates = {}
        self.pushButton.clicked.connect(self.find_date)
        self.tasks_button.clicked.connect(self.show_tasks)

    def find_date(self):
        # получаем дату
        string_date = self.calendarWidget.selectedDate().getDate()
        # добавляем ноль, если месяц <= 9
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        # добавляем ноль, если день <= 9
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        # берем текст из line edit
        line_edit = self.lineEdit.text()
        # задаем словарю новое значение или переопределяем старое
        self.all_dates[
            f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}'] = line_edit
        # избавляемся от повторов
        self.textBrowser.clear()
        # сортируем даты и выводим их
        for key in sorted(self.all_dates.keys()):
            self.textBrowser.append(f'{key} - {self.all_dates[key]}')

    def show_tasks(self):
        tasks = self.db.get_tasks()
        dialog = TaskDialog(tasks, parent=self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            for selected_task in dialog.selected_tasks:
                # Обработайте выбранные задачи, например, добавьте их в ваш словарь
                self.textBrowser.append(f'Выбрана задача: {selected_task}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
