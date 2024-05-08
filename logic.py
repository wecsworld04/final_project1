from PyQt6.QtWidgets import *
from voting_system import *
import csv


class Logic(QMainWindow, Ui_voting_system):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.vote_attempts = 0
        self.results = QLabel(self)

        self.error_label = QLabel(self)
        self.error_label.setGeometry(90, 180, 180, 50)
        self.error_label.setText("")

        self.login_button.clicked.connect(lambda: self.candidate_submit())
        self.vote_submit.clicked.connect(lambda: self.candidate_submit())
        self.exit_button.clicked.connect(lambda: self.close())

        self.hide_vote_menu()

    def candidate_submit(self):
        try:
            first_name_input = self.first_name.text()
            last_name_input = self.last_name.text()
            i_d_input = self.i_d.text()
            id_input = int(i_d_input)

            if len(i_d_input) != 4:
                raise ValueError("Invalid PIN. Please enter a 4-digit number.")

            login_data = []
            with open('login_data.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    login_data.append(row)

            for row in login_data:
                if self.login_button.isChecked():
                    if row[0] == first_name_input and row[1] == last_name_input and row[2] == str(id_input):
                        self.show_vote_menu()

                        thomas = 0
                        george = 0
                        abraham = 0

                        if self.thomas_j.isChecked():
                            thomas += 1
                        if self.george_w.isChecked():
                            george += 1
                        if self.abraham_l.isChecked():
                            abraham += 1

                        self.vote_attempts += 1
                        if self.vote_attempts == 10:
                            total = thomas + george + abraham
                            self.results.setText(
                                f"Thomas – {thomas}, George – {george}, Abraham – {abraham}, Total – {total}")

            self.error_label.setText()
        except ValueError as e:
            self.error_label.setText("Invalid Name and/or PIN, please try again.")
    def show_vote_menu(self):
        self.first_name.clear()
        self.last_name.clear()
        self.i_d.clear()

        self.cand_label.show()
        self.thomas_j.show()
        self.george_w.show()
        self.abraham_l.show()
        self.vote_submit.show()
        self.exit_button.show()

    def hide_vote_menu(self):
        # Hide vote menu components
        self.cand_label.hide()
        self.thomas_j.hide()
        self.george_w.hide()
        self.abraham_l.hide()
        self.vote_submit.hide()
        self.exit_button.hide()

    def clear(self):
        self.first_name.clear()
        self.last_name.clear()
        self.i_d.clear()
