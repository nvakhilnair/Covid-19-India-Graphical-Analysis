from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import datetime
import sys
from PyQt4.QtGui import QMessageBox
try:
    global state_wise
    global case_time_series
    global tested_number_icmr_data
    global state_wise_daily
    global statewise_tested_number_data
    global state_district_wise
    state_wise = pd.read_csv(
        "https://api.covid19india.org/csv/latest/state_wise.csv")
    case_time_series = pd.read_csv(
        "https://api.covid19india.org/csv/latest/case_time_series.csv")
    tested_number_icmr_data = pd.read_csv(
        "https://api.covid19india.org/csv/latest/tested_numbers_icmr_data.csv")
    state_wise_daily = pd.read_csv(
        'https://api.covid19india.org/csv/latest/state_wise_daily.csv')
    statewise_tested_number_data = pd.read_csv(
        'https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv')
    state_district_wise = pd.read_csv(
        'https://api.covid19india.org/csv/latest/district_wise.csv')
except:
    application = QtGui.QApplication(sys.argv)
    QMessageBox.information(None, 'Error', 'No Network Connection',
                            QMessageBox.Ok,
                            QMessageBox.Ok)
    sys.exit(0)


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(694, 513)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(
            "QWidget#Dialog {background-image: url(logo.png);background-repeat: no-repeat; background-position: center;}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.ico")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 130, 701, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 400, 701, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 10, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 150, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 420, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.IndiaCurrent = QtGui.QPushButton(Dialog)
        self.IndiaCurrent.setGeometry(QtCore.QRect(60, 70, 111, 23))
        self.IndiaCurrent.setObjectName(_fromUtf8("IndiaCurrent"))
        self.IndiaCurrent.clicked.connect(self.total_india_status_pie_chart)
        self.IndiaLast10Status = QtGui.QPushButton(Dialog)
        self.IndiaLast10Status.setGeometry(QtCore.QRect(270, 70, 121, 23))
        self.IndiaLast10Status.setObjectName(_fromUtf8("IndiaLast10Status"))
        self.IndiaLast10Status.clicked.connect(self.daily_status_plot)
        self.IndiaTest = QtGui.QPushButton(Dialog)
        self.IndiaTest.setGeometry(QtCore.QRect(480, 70, 181, 23))
        self.IndiaTest.setObjectName(_fromUtf8("IndiaTest"))
        self.IndiaTest.clicked.connect(self.test_to_positive_rate)
        self.StateStatus = QtGui.QPushButton(Dialog)
        self.StateStatus.setGeometry(QtCore.QRect(200, 200, 101, 23))
        self.StateStatus.setObjectName(_fromUtf8("StateStatus"))
        self.StateStatus.clicked.connect(self.pie_status_state)
        self.Last10daysStatus = QtGui.QPushButton(Dialog)
        self.Last10daysStatus.setGeometry(QtCore.QRect(330, 200, 121, 23))
        self.Last10daysStatus.setObjectName(_fromUtf8("Last10daysStatus"))
        self.Last10daysStatus.clicked.connect(self.state_status)
        self.Last10daysTest = QtGui.QPushButton(Dialog)
        self.Last10daysTest.setGeometry(QtCore.QRect(480, 200, 201, 23))
        self.Last10daysTest.setObjectName(_fromUtf8("Last10daysTest"))
        self.Last10daysTest.clicked.connect(self.state_testing)
        self.Statecomparison = QtGui.QPushButton(Dialog)
        self.Statecomparison.setGeometry(QtCore.QRect(500, 310, 151, 23))
        self.Statecomparison.setObjectName(_fromUtf8("Statecomparison"))
        self.Statecomparison.clicked.connect(self.state_comparision)
        self.districtStatus = QtGui.QPushButton(Dialog)
        self.districtStatus.setGeometry(QtCore.QRect(270, 460, 181, 23))
        self.districtStatus.setObjectName(_fromUtf8("districtStatus"))
        self.districtStatus.clicked.connect(self.district_status)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 200, 121, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(13)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(18, 310, 121, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 310, 121, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_4 = QtGui.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(330, 310, 141, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_5 = QtGui.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(100, 460, 131, 22))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(510, 420, 151, 71))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def total_india_status_pie_chart(self):
        data = state_wise.copy()
        Active = int(data[data['State_code'] == 'TT'].Active)
        Recovered = int(data[data['State_code'] == 'TT'].Recovered)
        Deaths = int(data[data['State_code'] == 'TT'].Deaths)
        Confirmed = int(data[data['State_code'] == 'TT'].Confirmed)
        pie_data = [Active, Recovered, Deaths]
        explode = (0.1, 0.05, 0.1)
        labels = ["Active", "Recovered", "Deaths"]
        plt.pie(pie_data, autopct='%.1f%%', labels=labels, explode=explode)
        plt.title("Covid-19 India: Current Status")
        plt.show()
        plt.bar('Confirmed', Confirmed)
        plt.bar('Active', Active)
        plt.bar('Recovered', Recovered)
        plt.bar('Deaths', Deaths)
        plt.legend(["Confirmed", "Actice", "Recovered", "Deaths"])
        plt.title("Covid-19 India: Current Status")
        plt.ylabel('Number of People')
        plt.text('Confirmed', Confirmed, str(Confirmed))
        plt.text('Active', Active, str(Active))
        plt.text('Recovered', Recovered, str(Recovered))
        plt.text('Deaths', Deaths, str(Deaths))
        plt.show()

    def daily_status_plot(self):
        data = case_time_series.copy()
        Confirmed = []
        Recovered = []
        Deceased = []
        Date = []
        for i in range(0, 15):
            temp = data.tail(15).iloc[i, 0]
            Date.append(temp)
            temp = data.tail(15).iloc[i, 1]
            Confirmed.append(temp)
            temp = data.tail(15).iloc[i, 3]
            Recovered.append(temp)
            temp = data.tail(15).iloc[i, 5]
            Deceased.append(temp)
        plt.rcParams["figure.figsize"] = (10, 8)
        plt.rc('xtick', labelsize=8)
        plt.rc('ytick', labelsize=8)
        plt.plot(Date, Confirmed, marker='o')
        plt.plot(Date, Recovered, marker='o')
        plt.plot(Date, Deceased, marker='o')
        plt.title("Covid-19 India: Last 15 days Status")
        plt.xlabel('Date')
        plt.ylabel('Number of people')
        plt.legend(["Confirmed", "Recovered", "Deceased"])
        plt.grid(True)
        for a, b in zip(Date, Confirmed):
            plt.text(a, b, str(b))
        for a, b in zip(Date, Recovered):
            plt.text(a, b, str(b))
        for a, b in zip(Date, Deceased):
            plt.text(a, b, str(b))
        plt.show()

    def test_to_positive_rate(self):
        data = tested_number_icmr_data.copy()
        data.rename(columns={"Update Time Stamp": "Date"}, inplace=True)
        data['Date'] = pd.to_datetime(
            data['Date'], dayfirst=True, yearfirst=False).dt.date
        data1 = case_time_series.copy()
        data1['Date'] = data1['Date'].map('{}2020'.format)
        data1['Date'] = pd.to_datetime(
            data1['Date'], dayfirst=True, yearfirst=False).dt.date
        temp_date = data.tail(17).iloc[0, 0]
        temp_data = int(data[data['Date'] == temp_date].iloc[:, 1])
        temp_data1 = int(data1[data1['Date'] == temp_date].iloc[:, 2])
        Date = []
        test = []
        con = []
        rate = []
        for i in range(0, 15):
            x = data1.tail(15).iloc[i, 0]
            y = str(x)
            y = y[5:]
            Date.append(y)
            temp = int(data[data['Date'] == x].iloc[:, 1])
            new_temp = temp
            temp = temp-temp_data
            temp_data = new_temp
            test.append(temp)
            temp = int(data1[data1['Date'] == x].iloc[:, 2])
            new_temp1 = temp
            temp = temp-temp_data1
            temp_data1 = new_temp1
            con.append(temp)
            temp = (con[i]/test[i])*100
            temp = round(temp, 2)
            rate.append(temp)
        plt.rcParams["figure.figsize"] = (10, 8)
        plt.rc('xtick', labelsize=8)
        plt.rc('ytick', labelsize=8)
        plt.plot(Date, test, marker='o')
        plt.plot(Date, con, marker='o')
        plt.xlabel('Date')
        plt.title('Covid-19 India: Last 15 days Number of Tests to Positive Case')
        plt.legend(["Daily Test Count", "Daily Positive Case"])
        plt.grid(True)
        for a, b in zip(Date, test):
            plt.text(a, b, str(b))
        for a, b in zip(Date, con):
            plt.text(a, b, str(b))
        plt.show()
        plt.rc('xtick', labelsize=8)
        plt.rc('ytick', labelsize=8)
        plt.plot(Date, rate, marker='o')
        plt.title('Covid-19 India: Test Positive Rate %')
        plt.xlabel('Date')
        plt.ylabel('%Rate')
        plt.legend(["Test Positive Rate"])
        plt.grid(True)
        for a, b in zip(Date, rate):
            plt.text(a, b, str(b))
        plt.show()

    def state_status(self):
        try:
            state = self.comboBox.currentText()
            data = state_wise.copy()
            data["State_code"] = data["State_code"].astype(str)
            state_code = data[data['State'] == state].State_code
            temp = []
            for i in state_code:
                temp.append(i)
            code = ''.join([str(elem) for elem in temp])
            data = state_wise_daily.copy()
            data.rename(columns={code: "code"}, inplace=True)
            Confirmed = []
            Recovered = []
            deaths = []
            for i in range(0, 15):
                temp = data[data['Status'] == 'Confirmed'].tail(
                    15).code.iloc[i]
                Confirmed.append(temp)
                temp = data[data['Status'] == 'Recovered'].tail(
                    15).code.iloc[i]
                Recovered.append(temp)
                temp = data[data['Status'] == 'Deceased'].tail(15).code.iloc[i]
                deaths.append(temp)
            today = datetime.date.today()
            Date = []
            for i in range(15, 0, -1):
                x = str(today - datetime.timedelta(days=i))
                x = x[5:]
                Date.append(x)
            plt.rcParams["figure.figsize"] = (12, 12)
            plt.rc('xtick', labelsize=8)
            plt.rc('ytick', labelsize=8)
            plt.plot(Date, Confirmed, marker='o')
            plt.plot(Date, Recovered, marker='o')
            plt.plot(Date, deaths, marker='o')
            plt.legend(["Confirmed", "Recovered", "Deceased"])
            plt.xlabel('Date')
            plt.ylabel('Number of people')
            plt.grid(True)
            title = ('Covid-19 ' + state + ': Last 15 Day Status')
            plt.title(title)
            for a, b in zip(Date, Confirmed):
                plt.text(a, b, str(b))
            for a, b in zip(Date, Recovered):
                plt.text(a, b, str(b))
            for a, b in zip(Date, deaths):
                plt.text(a, b, str(b))
            plt.show()
        except:
            error = QtGui.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected state")

    def pie_status_state(self):
        state = self.comboBox.currentText()
        data = state_wise.copy()
        Active = int(data[data['State'] == state].Active)
        Recovered = int(data[data['State'] == state].Recovered)
        Deaths = int(data[data['State'] == state].Deaths)
        Confirmed = int(data[data['State'] == state].Confirmed)
        pie_data = [Active, Recovered, Deaths]
        explode = (0.1, 0.1, 0.1)
        labels = ["Active", "Recovered", "Deaths"]
        plt.pie(pie_data, autopct='%.1f%%', labels=labels, explode=explode)
        title = ('Covid-19 ' + state + ': Current Status')
        plt.title(title)
        plt.show()
        plt.bar('Confirmed', Confirmed)
        plt.bar('Active', Active)
        plt.bar('Recovered', Recovered)
        plt.bar('Deaths', Deaths)
        plt.xlabel('Date')
        plt.ylabel('Number of people')
        plt.legend(["Confirmed", "Active", "Recovered", "Deaths"])
        plt.title(title)
        plt.text('Confirmed', Confirmed, str(Confirmed))
        plt.text('Active', Active, str(Active))
        plt.text('Recovered', Recovered, str(Recovered))
        plt.text('Deaths', Deaths, str(Deaths))
        plt.show()

    def state_testing(self):
        try:
            state = self.comboBox.currentText()
            data = statewise_tested_number_data.copy()
            data.rename(columns={"Updated On": "Date"}, inplace=True)
            data.rename(columns={"Total Tested": "TotalTested"}, inplace=True)
            temp_tested = int(
                data[data['State'] == state].tail(17).TotalTested.iloc[0])
            temp_positive = int(
                data[data['State'] == state].tail(17).Positive.iloc[0])
            Date = []
            TT = []
            PT = []
            Rate = []
            for i in range(0, 15):
                tested = int(data[data['State'] == state].tail(
                    16).TotalTested.iloc[i])
                positive = int(
                    data[data['State'] == state].tail(16).Positive.iloc[i])
                x = str(data[data['State'] == state].tail(15).Date.iloc[i])
                x = x[:5]
                Date.append(x)
                loc_tested = tested
                loc_positive = positive
                tested = tested-temp_tested
                positive = positive-temp_positive
                temp_tested = loc_tested
                temp_positive = loc_positive
                TT.append(tested)
                PT.append(positive)
                Rate.append(round(((positive/tested)*100), 2))
            plt.rcParams["figure.figsize"] = (12, 12)
            plt.plot(Date, TT, marker='o')
            plt.plot(Date, PT, marker='o')
            plt.rc('xtick', labelsize=8)
            plt.rc('ytick', labelsize=8)
            title = "Covid-19 " + state + ": Last 15 days Testing to Corresponding Positive Count"
            plt.title(title)
            plt.xlabel('Date')
            plt.legend(["Daily Tested", "Daily Positive"])
            plt.grid(True)
            for a, b in zip(Date, TT):
                plt.text(a, b, str(b))
            for a, b in zip(Date, PT):
                plt.text(a, b, str(b))
            plt.show()
            plt.rcParams["figure.figsize"] = (12, 12)
            plt.rc('xtick', labelsize=8)
            plt.rc('ytick', labelsize=8)
            plt.plot(Date, Rate, marker='o')
            plt.legend(["Rate"])
            title = "Covid-19" + state + ": Last 15 days Test to Postive Rate in Pencentage"
            plt.title(title)
            plt.xlabel('Date')
            plt.ylabel('%Rate')
            for a, b in zip(Date, Rate):
                plt.text(a, b, str(b))
            plt.show()
        except:
            error = QtGui.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected state")

    def district_status(self):
        district = self.comboBox_5.currentText()
        data = state_district_wise.copy()
        active = int(data[data['District'] == district].Active)
        confirmed = int(data[data['District'] == district].Confirmed)
        deceased = int(data[data['District'] == district].Deceased)
        recovered = int(data[data['District'] == district].Recovered)
        plt.bar('Active', active)
        plt.bar('Confirmed', confirmed)
        plt.bar('Deceased', deceased)
        plt.bar('Recovered', recovered)
        plt.legend(["Active", "Confirmed", "Deceased", "Recovered"])
        title = "Covid-19 District(" + district + "): Current Status"
        plt.title(title)
        plt.text('Active', active, str(active))
        plt.text('Confirmed', confirmed, str(confirmed))
        plt.text('Deceased', deceased, str(deceased))
        plt.text('Recovered', recovered, str(recovered))
        plt.xlabel('Date')
        plt.ylabel('Number of people')
        plt.show()
        pie_data = [active, recovered, deceased]
        explode = (0.1, 0.05, 0.1)
        labels = ["Active", "Recovered", "Deaths"]
        plt.pie(pie_data, autopct='%.1f%%', labels=labels, explode=explode)
        plt.title(title)
        plt.show()

    def state_comparision(self):
        try:
            state1 = self.comboBox_2.currentText()
            state2 = self.comboBox_3.currentText()
            state3 = self.comboBox_4.currentText()
            data = state_wise.copy()
            data["State_code"] = data["State_code"].astype(str)
            state_code = data[data['State'] == state1].State_code
            temp = []
            for i in state_code:
                temp.append(i)
            code1 = ''.join([str(elem) for elem in temp])
            state_code = data[data['State'] == state2].State_code
            temp = []
            for i in state_code:
                temp.append(i)
            code2 = ''.join([str(elem) for elem in temp])
            state_code = data[data['State'] == state3].State_code
            temp = []
            for i in state_code:
                temp.append(i)
            code3 = ''.join([str(elem) for elem in temp])
            data = state_wise_daily.copy()
            data.rename(columns={code1: "code1"}, inplace=True)
            data.rename(columns={code2: "code2"}, inplace=True)
            data.rename(columns={code3: "code3"}, inplace=True)
            Confirmed1 = []
            Recovered1 = []
            deaths1 = []
            Confirmed2 = []
            Recovered2 = []
            deaths2 = []
            Confirmed3 = []
            Recovered3 = []
            deaths3 = []
            data1 = statewise_tested_number_data.copy()
            data1.rename(columns={"Updated On": "Date"}, inplace=True)
            data1.rename(columns={"Total Tested": "TotalTested"}, inplace=True)
            temp_tested1 = int(
                data1[data1['State'] == state1].tail(17).TotalTested.iloc[0])
            temp_positive1 = int(
                data1[data1['State'] == state1].tail(17).Positive.iloc[0])
            Rate1 = []
            temp_tested2 = int(
                data1[data1['State'] == state2].tail(17).TotalTested.iloc[0])
            temp_positive2 = int(
                data1[data1['State'] == state2].tail(17).Positive.iloc[0])
            Rate2 = []
            temp_tested3 = int(
                data1[data1['State'] == state3].tail(17).TotalTested.iloc[0])
            temp_positive3 = int(
                data1[data1['State'] == state3].tail(17).Positive.iloc[0])
            Rate3 = []
            for i in range(0, 15):
                tested1 = int(data1[data1['State'] == state1].tail(
                    16).TotalTested.iloc[i])
                positive1 = int(
                    data1[data1['State'] == state1].tail(16).Positive.iloc[i])
                loc_tested1 = tested1
                loc_positive1 = positive1
                tested1 = tested1-temp_tested1
                positive1 = positive1-temp_positive1
                temp_tested1 = loc_tested1
                temp_positive1 = loc_positive1
                Rate1.append(round(((positive1/tested1)*100), 2))
                tested2 = int(data1[data1['State'] == state2].tail(
                    16).TotalTested.iloc[i])
                positive2 = int(
                    data1[data1['State'] == state2].tail(16).Positive.iloc[i])
                loc_tested2 = tested2
                loc_positive2 = positive2
                tested2 = tested2-temp_tested2
                positive2 = positive2-temp_positive2
                temp_tested2 = loc_tested2
                temp_positive2 = loc_positive2
                Rate2.append(round(((positive2/tested2)*100), 2))
                tested3 = int(data1[data1['State'] == state3].tail(
                    16).TotalTested.iloc[i])
                positive3 = int(
                    data1[data1['State'] == state3].tail(16).Positive.iloc[i])
                loc_tested3 = tested3
                loc_positive3 = positive3
                tested3 = tested3-temp_tested3
                positive3 = positive3-temp_positive3
                temp_tested3 = loc_tested3
                temp_positive3 = loc_positive3
                Rate3.append(round(((positive3/tested3)*100), 2))
                temp = int(data[data['Status'] == 'Confirmed'].tail(
                    15).code1.iloc[i])
                Confirmed1.append(temp)
                temp = int(data[data['Status'] == 'Recovered'].tail(
                    15).code1.iloc[i])
                Recovered1.append(temp)
                temp = int(data[data['Status'] == 'Deceased'].tail(
                    15).code1.iloc[i])
                deaths1.append(temp)
                temp = int(data[data['Status'] == 'Confirmed'].tail(
                    15).code2.iloc[i])
                Confirmed2.append(temp)
                temp = int(data[data['Status'] == 'Recovered'].tail(
                    15).code2.iloc[i])
                Recovered2.append(temp)
                temp = int(data[data['Status'] == 'Deceased'].tail(
                    15).code2.iloc[i])
                deaths2.append(temp)
                temp = int(data[data['Status'] == 'Confirmed'].tail(
                    15).code3.iloc[i])
                Confirmed3.append(temp)
                temp = int(data[data['Status'] == 'Recovered'].tail(
                    15).code3.iloc[i])
                Recovered3.append(temp)
                temp = int(data[data['Status'] == 'Deceased'].tail(
                    15).code3.iloc[i])
                deaths3.append(temp)
            today = datetime.date.today()
            Date = []
            for i in range(15, 0, -1):
                x = str(today - datetime.timedelta(days=i))
                x = x[5:]
                Date.append(x)
            plt.rcParams["figure.figsize"] = (10, 8)
            plt.rc('xtick', labelsize=8)
            plt.rc('ytick', labelsize=8)
            plt.plot(Date, Confirmed1, marker='o')
            plt.plot(Date, Confirmed2, marker='o')
            plt.plot(Date, Confirmed3, marker='o')
            plt.legend([state1, state2, state3])
            plt.grid(True)
            plt.title('State Comparison of Confirmed Cases in Last 15 days')
            for a, b in zip(Date, Confirmed1):
                plt.text(a, b, str(b))
            for a, b in zip(Date, Confirmed2):
                plt.text(a, b, str(b))
            for a, b in zip(Date, Confirmed3):
                plt.text(a, b, str(b))
            plt.xlabel('Date')
            plt.ylabel('Number of people')
            plt.show()
            plt.rcParams["figure.figsize"] = (10, 8)
            plt.rc('xtick', labelsize=8)
            plt.rc('ytick', labelsize=8)
            plt.plot(Date, Recovered1, marker='o')
            plt.plot(Date, Recovered2, marker='o')
            plt.plot(Date, Recovered3, marker='o')
            plt.legend([state1, state2, state3])
            plt.grid(True)
            plt.title('State Comparison of Recovered Cases in last 15 days')
            plt.xlabel('Date')
            plt.ylabel('Number of people')
            for a, b in zip(Date, Recovered1):
                plt.text(a, b, str(b))
            for a, b in zip(Date, Recovered2):
                plt.text(a, b, str(b))
            for a, b in zip(Date, Recovered3):
                plt.text(a, b, str(b))
            plt.show()
            plt.rcParams["figure.figsize"] = (10, 8)
            plt.rc('xtick', labelsize=8)
            plt.rc('ytick', labelsize=8)
            plt.plot(Date, deaths1, marker='o')
            plt.plot(Date, deaths2, marker='o')
            plt.plot(Date, deaths3, marker='o')
            plt.legend([state1, state2, state3])
            plt.grid(True)
            plt.title('State Comparison of Deceased Cases in last 15 days')
            plt.xlabel('Date')
            plt.ylabel('Number of people')
            for a, b in zip(Date, deaths1):
                plt.text(a, b, str(b))
            for a, b in zip(Date, deaths2):
                plt.text(a, b, str(b))
            for a, b in zip(Date, deaths3):
                plt.text(a, b, str(b))
            plt.show()
            plt.rcParams["figure.figsize"] = (10, 8)
            plt.rc('xtick', labelsize=8)
            plt.rc('ytick', labelsize=8)
            plt.plot(Date, Rate1, marker='o')
            plt.plot(Date, Rate2, marker='o')
            plt.plot(Date, Rate3, marker='o')
            plt.legend([state1, state2, state3])
            plt.grid(True)
            plt.title(
                'State Comparison of tested to positive rate in last 15 days')
            plt.xlabel('Date')
            plt.ylabel('%Rate')
            for a, b in zip(Date, Rate1):
                plt.text(a, b, str(b))
            for a, b in zip(Date, Rate2):
                plt.text(a, b, str(b))
            for a, b in zip(Date, Rate3):
                plt.text(a, b, str(b))
            plt.show()
        except:
            error = QtGui.QMessageBox.critical(
                self, 'Error', "Data insufficient for the any 1 or more selected state")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Covid-19 Analysis", None))
        self.label.setText(_translate(
            "Dialog", "Covid-19: India Analysis", None))
        self.label_2.setText(_translate(
            "Dialog", "Covid-19: State Analysis", None))
        self.label_3.setText(_translate(
            "Dialog", "Covid-19: District Analysis", None))
        self.IndiaCurrent.setText(_translate("Dialog", "Current Status", None))
        self.IndiaLast10Status.setText(_translate(
            "Dialog", "Last 15 Days Status", None))
        self.IndiaTest.setText(_translate(
            "Dialog", "Last 15 days Test to Positive Rate", None))
        self.StateStatus.setText(_translate("Dialog", "Current Status", None))
        self.Last10daysStatus.setText(_translate(
            "Dialog", "Last 15 Days Status", None))
        self.Last10daysTest.setText(_translate(
            "Dialog", "Last 15 days Test to Positive Rate", None))
        self.Statecomparison.setText(_translate(
            "Dialog", "Selected State Comparison", None))
        self.districtStatus.setText(_translate(
            "Dialog", "Selected district Current Status", None))
        data = state_wise.copy()
        state_names = []
        for i in range(1, len(data)):
            temp = str(data.iloc[i, 0])
            state_names.append(temp)
        state_names.sort()
        data = state_district_wise.copy()
        district_name = []
        for i in range(1, 756):
            temp = str(data.iloc[i, 4])
            district_name.append(temp)
        district_name.sort()
        district_name = list(dict.fromkeys(district_name))
        district_name.remove('Other Region')
        district_name.remove('Other State')
        for i in range(0, len(state_names)):
            self.comboBox.insertItem(i, _translate(
                "Dialog", state_names[i], None))
            self.comboBox_2.insertItem(
                i, _translate("Dialog", state_names[i], None))
            self.comboBox_3.insertItem(
                i, _translate("Dialog", state_names[i], None))
            self.comboBox_4.insertItem(
                i, _translate("Dialog", state_names[i], None))
        for i in range(0, len(district_name)):
            self.comboBox_5.insertItem(i, _translate(
                "Dialog", district_name[i], None))
        self.comboBox.setCurrentIndex(state_names.index('Kerala'))
        self.comboBox_2.setCurrentIndex(state_names.index('Kerala'))
        self.comboBox_3.setCurrentIndex(state_names.index('Gujarat'))
        self.comboBox_4.setCurrentIndex(state_names.index('Karnataka'))
        self.comboBox_5.setCurrentIndex(district_name.index('Kannur'))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Developed</span><span style=\" font-weight:600;\">: Akhil</span></p><p><span style=\" font-weight:600;\">developmentuse009@gmail.com</span></p><p><span style=\" font-weight:600; text-decoration: underline;\">Data</span><span style=\" font-weight:600;\">: </span><a href=\"https://api.covid19india.org/\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">api.covid19india.org</span></a></p></body></html>", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
