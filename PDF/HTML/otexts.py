import sys
import time
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)
loader.page().pdfPrintingFinished.connect(
    lambda *args: print('finished:', args))

loader.load(QtCore.QUrl("https://otexts.com/fppkr/forecasting-regression.html"))

def emit_pdf(finished):
    loader.show()
    loader.page().printToPdf('47_forecasting-regression.pdf')

loader.loadFinished.connect(emit_pdf)
sys.exit(app.exec_())