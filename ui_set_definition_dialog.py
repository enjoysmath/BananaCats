# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_definition_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetDefinitionDialog(object):
    def setupUi(self, SetDefinitionDialog):
        SetDefinitionDialog.setObjectName("SetDefinitionDialog")
        SetDefinitionDialog.resize(301, 60)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/galaxy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SetDefinitionDialog.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(SetDefinitionDialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(SetDefinitionDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetDefinitionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.buttonBox)

        self.retranslateUi(SetDefinitionDialog)
        self.buttonBox.accepted.connect(SetDefinitionDialog.accept)
        self.buttonBox.rejected.connect(SetDefinitionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SetDefinitionDialog)

    def retranslateUi(self, SetDefinitionDialog):
        _translate = QtCore.QCoreApplication.translate
        SetDefinitionDialog.setWindowTitle(_translate("SetDefinitionDialog", "Set Definition"))
        self.label.setText(_translate("SetDefinitionDialog", "Navigate to the diagram that is the definition then click OK."))
import resources_rc
