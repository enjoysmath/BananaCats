# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagram_name_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiagramNameDialog(object):
    def setupUi(self, DiagramNameDialog):
        DiagramNameDialog.setObjectName("DiagramNameDialog")
        DiagramNameDialog.resize(247, 67)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/galaxy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DiagramNameDialog.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(DiagramNameDialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DiagramNameDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameLineEdit = QtWidgets.QLineEdit(DiagramNameDialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(DiagramNameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(DiagramNameDialog)
        self.buttonBox.accepted.connect(DiagramNameDialog.accept)
        self.buttonBox.rejected.connect(DiagramNameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DiagramNameDialog)

    def retranslateUi(self, DiagramNameDialog):
        _translate = QtCore.QCoreApplication.translate
        DiagramNameDialog.setWindowTitle(_translate("DiagramNameDialog", "Diagram Name"))
        self.label.setText(_translate("DiagramNameDialog", "Name:"))
import resources_rc