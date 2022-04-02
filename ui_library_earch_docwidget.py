# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library_search_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LibrarySearchDockWidget(object):
    def setupUi(self, LibrarySearchDockWidget):
        LibrarySearchDockWidget.setObjectName("LibrarySearchDockWidget")
        LibrarySearchDockWidget.resize(222, 394)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.searchPathTab = QtWidgets.QWidget()
        self.searchPathTab.setObjectName("searchPathTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.searchPathTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fileSystemLayout = QtWidgets.QGridLayout()
        self.fileSystemLayout.setObjectName("fileSystemLayout")
        self.gridLayout_2.addLayout(self.fileSystemLayout, 2, 0, 1, 3)
        self.recompileButton = QtWidgets.QPushButton(self.searchPathTab)
        self.recompileButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.recompileButton.setObjectName("recompileButton")
        self.gridLayout_2.addWidget(self.recompileButton, 3, 0, 1, 3)
        self.checkAllButton_2 = QtWidgets.QPushButton(self.searchPathTab)
        self.checkAllButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.checkAllButton_2.setObjectName("checkAllButton_2")
        self.gridLayout_2.addWidget(self.checkAllButton_2, 1, 0, 1, 1)
        self.checkNoneButton_3 = QtWidgets.QPushButton(self.searchPathTab)
        self.checkNoneButton_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.checkNoneButton_3.setObjectName("checkNoneButton_3")
        self.gridLayout_2.addWidget(self.checkNoneButton_3, 1, 1, 1, 1)
        self.tabWidget.addTab(self.searchPathTab, "")
        self.queryDiagramTab = QtWidgets.QWidget()
        self.queryDiagramTab.setObjectName("queryDiagramTab")
        self.tabWidget.addTab(self.queryDiagramTab, "")
        self.searchResultsTab = QtWidgets.QWidget()
        self.searchResultsTab.setObjectName("searchResultsTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.searchResultsTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.searchResultsTab)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.searchProgressBar = QtWidgets.QProgressBar(self.searchResultsTab)
        self.searchProgressBar.setProperty("value", 24)
        self.searchProgressBar.setObjectName("searchProgressBar")
        self.gridLayout_3.addWidget(self.searchProgressBar, 3, 0, 1, 4)
        self.checkBox = QtWidgets.QCheckBox(self.searchResultsTab)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 4)
        self.orderByComboBox = QtWidgets.QComboBox(self.searchResultsTab)
        self.orderByComboBox.setObjectName("orderByComboBox")
        self.orderByComboBox.addItem("")
        self.gridLayout_3.addWidget(self.orderByComboBox, 2, 1, 1, 3)
        self.tabWidget.addTab(self.searchResultsTab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 3)
        self.searchButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.searchButton.setMinimumSize(QtCore.QSize(40, 0))
        self.searchButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 3)
        LibrarySearchDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(LibrarySearchDockWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LibrarySearchDockWidget)

    def retranslateUi(self, LibrarySearchDockWidget):
        _translate = QtCore.QCoreApplication.translate
        LibrarySearchDockWidget.setWindowTitle(_translate("LibrarySearchDockWidget", "Library Search"))
        self.recompileButton.setText(_translate("LibrarySearchDockWidget", "Recompile"))
        self.checkAllButton_2.setText(_translate("LibrarySearchDockWidget", "all"))
        self.checkNoneButton_3.setText(_translate("LibrarySearchDockWidget", "none"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchPathTab), _translate("LibrarySearchDockWidget", "Sources"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.queryDiagramTab), _translate("LibrarySearchDockWidget", "Query"))
        self.label_2.setText(_translate("LibrarySearchDockWidget", "Order by:"))
        self.checkBox.setText(_translate("LibrarySearchDockWidget", "Auto-update results"))
        self.orderByComboBox.setItemText(0, _translate("LibrarySearchDockWidget", "alphabetical on name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchResultsTab), _translate("LibrarySearchDockWidget", "Results"))
        self.searchButton.setToolTip(_translate("LibrarySearchDockWidget", "Search for what is selected in the current diagram view (see tabs)."))
        self.searchButton.setText(_translate("LibrarySearchDockWidget", "🔍 Search library"))
