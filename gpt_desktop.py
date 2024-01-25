import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCalendarWidget, QPushButton, QDialog, QLabel, \
    QDateEdit, QLineEdit, QWidget


class EventDialog(QDialog):
    def __init__(self):
        super(EventDialog, self).__init__()

        self.setWindowTitle("Добавить событие")

        layout = QVBoxLayout()

        self.date_label = QLabel("Дата:")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)

        self.event_label = QLabel("Событие:")
        self.event_edit = QLineEdit()

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.accept)

        layout.addWidget(self.date_label)
        layout.addWidget(self.date_edit)
        layout.addWidget(self.event_label)
        layout.addWidget(self.event_edit)
        layout.addWidget(self.add_button)

        self.setLayout(layout)


class CalendarApp(QMainWindow):
    def __init__(self):
        super(CalendarApp, self).__init__()

        self.setWindowTitle("Календарь событий")

        self.central_widget = QCalendarWidget()
        self.central_widget.clicked.connect(self.show_event_dialog)

        self.add_event_button = QPushButton("Добавить событие")
        self.add_event_button.clicked.connect(self.show_event_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.central_widget)
        layout.addWidget(self.add_event_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    # def show_event_dialog(self, date):
    #     dialog = EventDialog()
    #     dialog.date_edit.setDate(date)
    #     result = dialog.exec_()
    #
    #     if result == QDialog.Accepted:
    #         event_date = dialog.date_edit.date()
    #         event_text = dialog.event_edit.text()
    #
    #         # Здесь можно обработать данные и добавить событие в вашу базу данных или другое хранилище
    #         print(f"Добавлено событие на {event_date.toString('dd.MM.yyyy')}: {event_text}")

    def show_event_dialog(self, date):
        dialog = EventDialog()
        dialog.date_edit.setDate(date)

        def on_accepted():
            event_date = dialog.date_edit.date()
            event_text = dialog.event_edit.text()
            print(f"Добавлено событие на {event_date.toString('dd.MM.yyyy')}: {event_text}")

        dialog.accepted.connect(on_accepted)

        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    app.exec_()
