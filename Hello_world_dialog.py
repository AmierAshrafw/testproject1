# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HelloWorldDialog
                                 A QGIS plugin
 this is a test
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-11-02
        git sha              : $Format:%H$
        copyright            : (C) 2022 by amier
        email                : aa
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Hello_world_dialog_base.ui'))


class HelloWorldDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(HelloWorldDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pbStart.clicked.connect(self.print_hello_world)
        self.pbCalculate.clicked.connect(self.Calculate)

    def print_hello_world(self):
        text1 = "Salam Dunia"
        text2 = "hello World"

        show = text1 if self.cbUseMalay.isChecked() else text2

        self.lbHello.setText(show)

        #if self.cbUseMalay.isChecked():
        #     self.lbHello.setText("Salam Dunia")
        #else:
        #     self.lbHello.setText("Hello World")

    def Calculate(self):
        num1 = self.sbValue1.value()
        num2 = self.sbValue2.value()

        product = num1 * num2

        self.lbAnswer.setText(f"{product}")

        print(product)