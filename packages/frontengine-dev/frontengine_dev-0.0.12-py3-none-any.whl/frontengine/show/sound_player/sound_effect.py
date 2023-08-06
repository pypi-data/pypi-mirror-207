import os
from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QWidget, QMessageBox


class SoundEffectWidget(QWidget):

    def __init__(self, sound_path: str, volume: int = 100):
        super().__init__()
        self.setWindowFlag(
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.sound_player = QSoundEffect()
        self.sound_path = Path(sound_path)
        if self.sound_path.exists() and self.sound_path.is_file():
            self.sound_player.setSource(QUrl.fromLocalFile(str(self.sound_path)))
            self.sound_player.setVolume(volume)
            # -2 means loop forever
            self.sound_player.setLoopCount(-2)
            self.sound_player.play()
        else:
            message_box = QMessageBox(self)
            message_box.setText("Sound file error")
            message_box.show()
        # Window setting
        self.setWindowTitle("Sound Wave")
        # Set Icon
        self.icon_path = Path(os.getcwd() + "/je_driver_icon.ico")
        if self.icon_path.exists() and self.icon_path.is_file():
            self.setWindowIcon(QIcon(str(self.icon_path)))

    def closeEvent(self, event):
        super().closeEvent(event)
        self.sound_player.stop()
