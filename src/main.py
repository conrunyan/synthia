import logging

from pyo import Server
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from src.components import Keyboard, ControlPanel
from src.sound import Synth

logging.basicConfig(
    filename="app.log",  # Log file name
    filemode="a",  # Append mode (use 'w' to overwrite)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    level=logging.DEBUG,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)


class SynthiaApp(App):
    CSS_PATH = "app.tcss"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.synth = Synth()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ControlPanel(synth=self.synth)
        yield Keyboard(synth=self.synth)


def main():
    serv = Server().boot()
    serv.start()
    app = SynthiaApp()
    app.run()


if __name__ == "__main__":
    main()
