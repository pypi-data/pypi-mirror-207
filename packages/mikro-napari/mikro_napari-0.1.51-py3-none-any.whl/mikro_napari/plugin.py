from arkitekt.builders import publicqt
from mikro_napari.widgets.main_widget import MikroNapariWidget

identifier = "github.io.jhnnsrs.mikro-napari"
version = "latest"


class ArkitektPluginWidget(MikroNapariWidget):
    def __init__(self, viewer: "napari.viewer.Viewer") -> None:
        print("ArkitektPluginWidget.__init__")
        super(ArkitektPluginWidget, self).__init__(
            viewer, publicqt(identifier, version, parent=viewer.window.qt_viewer)
        )
        self.app.enter()
