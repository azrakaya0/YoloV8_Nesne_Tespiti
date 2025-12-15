import sys
import cv2
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QImage
from ultralytics import YOLO


class YOLOApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 Object Detection")
        self.setGeometry(100, 100, 1000, 500)

        self.model = YOLO("best.pt")
        self.image_path = None

        self.original_label = QLabel("Original Image")
        self.result_label = QLabel("Detected Image")

        self.btn_select = QPushButton("Select Image")
        self.btn_test = QPushButton("Test Image")

        self.btn_select.clicked.connect(self.select_image)
        self.btn_test.clicked.connect(self.test_image)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.original_label)
        h_layout.addWidget(self.result_label)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.btn_select)
        v_layout.addWidget(self.btn_test)

        self.setLayout(v_layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "test_images",
            "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.image_path = file_path
            self.show_image(file_path, self.original_label)

    def test_image(self):
        if self.image_path is None:
            return

        results = self.model(self.image_path)
        img = results[0].plot()

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.result_label.setPixmap(QPixmap.fromImage(qt_img).scaled(
            400, 400
        ))

    def show_image(self, path, label):
        img = cv2.imread(path)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(qt_img).scaled(400, 400))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YOLOApp()
    window.show()
    sys.exit(app.exec_())
