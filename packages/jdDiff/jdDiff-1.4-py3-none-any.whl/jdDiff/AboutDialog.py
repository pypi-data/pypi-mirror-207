from .ui_compiled.AboutDialog import Ui_AboutDialog
from PyQt6.QtWidgets import QDialog
import webbrowser


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, env):
        super().__init__()

        self.setupUi(self)

        self.icon_label.setPixmap(env.icon.pixmap(64, 64))
        self.version_label.setText(self.version_label.text().replace("{{version}}", env.version))

        self.button_view_source.clicked.connect(lambda: webbrowser.open("https://codeberg.org/JakobDev/jdDiff"))
        self.button_close.clicked.connect(self.close)
