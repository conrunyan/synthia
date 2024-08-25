from pyo import Server
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from src.components import Keyboard


class SynthiaApp(App):
    CSS_PATH = "app.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Keyboard()


def main():
    serv = Server().boot()
    serv.start()
    app = SynthiaApp()
    app.run()


if __name__ == "__main__":
    main()
