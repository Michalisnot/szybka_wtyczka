# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SzybkaWtyczkaDialog
                                 A QGIS plugin
 Podstawy Informatyki
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-03
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Michał Spręga 
        email                : cokolwiek
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
from PyQt5.QtCore import Qt
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtWidgets import QMessageBox
# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'szybka_wtyczka_dialog_base.ui'))


class SzybkaWtyczkaDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SzybkaWtyczkaDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton_calc_dh.clicked.connect(self.calculate_dh)
        self.pushButton_calc_area.clicked.connect(self.calculate_area)  
        self.pushButton_clear.clicked.connect(self.czysc)  
        # self.pushButton_calc_area.clicked.connect(self.launch_Popup)
        self.dlg = SzybkaWtyczkaDialo()
        self.dlg.setWindowFlags(Qt.WindowStaysOnTopHint)
    def czysc(self):
        mc = self.mMapLayerComboBox.currentLayer()

        # for layer in mc.layers():
        #     if layer.type() == layer.VectorLayer:
        mc.removeSelection()
        self.label_3_area_result.setText(f'')
        self.label_dh_results.setText(f'')
        # mc.refresh()
    def calculate_area(self):
        current_layer = self.mMapLayerComboBox.currentLayer()
        selected_features = current_layer.selectedFeatures()
        x2_area = 0
        j=0
        for d in selected_features:
            j+=1
        if j<3:
            j = 3-j
            xdd = f"Zaznaczono {j} punktów za mało"
            self.launch_Popup(xdd)
        else:
            for i,feature in enumerate(selected_features):
                current_x = feature.geometry().asPoint().x()
                previous_y = selected_features[i-1].geometry().asPoint().y()
                try:
                    next_y = selected_features[i+1].geometry().asPoint().y()
                except:
                    next_y = selected_features[0].geometry().asPoint().y()
                x2_area += current_x*(next_y-previous_y)
                area = abs(x2_area/2)
                self.label_3_area_result.setText(f'{area:.1f} m')
            
    def calculate_dh(self):
        current_layer = self.mMapLayerComboBox.currentLayer()
        selected_features = current_layer.selectedFeatures()
        j=0
        for i in selected_features:
            j+=1
        # if(j==2):
        if(j==0 or j==1):
            j=2-j
            xd = f"Zaznaczono {j} punktów za mało"
            self.launch_Popup(xd)
        elif(j>2):
            j = j-2
            xd = f"Zaznaczono {j} punktów za wiele"
            self.launch_Popup(xd)
        else:
            h_1 = float(selected_features[0]['wysokosc'])
            h_2 = float(selected_features[1]['wysokosc'])
            d_h = h_2-h_1
            self.label_dh_results.setText(f'{d_h:.2f} m')
    def launch_Popup(self,text):
        current_layer = self.mMapLayerComboBox.currentLayer()
        selected_features = current_layer.selectedFeatures()        
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText(f"{text}")
        x = msg.exec_()











