import os
from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QWidget, QMessageBox


class SoundPlayer(QWidget):

    def __init__(self, sound_path: str, volume: int = 100):
        super().__init__()
        self.setWindowFlag(
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.sound_path = Path(sound_path)
        if self.sound_path.exists() and self.sound_path.is_file():
            self.media_player = QMediaPlayer()
            self.media_player_audio = QAudioOutput()
            self.media_player.setAudioOutput(self.media_player_audio)
            self.media_player_audio = self.media_player.audioOutput()
            # QUrl non ascii path encode, Avoid read wrong path and file name
            source = QUrl.fromLocalFile(str(self.sound_path).encode())
            source = source.fromEncoded(source.toEncoded())
            self.media_player.setSource(source)
            self.media_player_audio.setVolume(volume)
            self.media_player.setLoops(-1)
            self.media_player.play()
        else:
            message_box = QMessageBox(self)
            message_box.setText("Sound file error")
            message_box.show()
        # Window setting
        self.setWindowTitle("Sound")
        # Set Icon
        self.icon_path = Path(os.getcwd() + "/je_driver_icon.ico")
        if self.icon_path.exists() and self.icon_path.is_file():
            self.setWindowIcon(QIcon(str(self.icon_path)))

    def closeEvent(self, event):
        super().closeEvent(event)
        self.media_player.stop()
