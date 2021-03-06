import os
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from ui import main


class MyFileBrowser(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.model = QtWidgets.QFileSystemModel()
        self.setupUi(self)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()

    def populate(self):
        path = r"E:"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        delete = menu.addAction("Delete")
        delete.triggered.connect(self.delete_file)
        new = menu.addAction("New File")
        new.triggered.connect(self.new_file)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def delete_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        os.remove(file_path)

    def new_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        f = open(file_path + "/newFile.txt", 'a')
        f.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()
