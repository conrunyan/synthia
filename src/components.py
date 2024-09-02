import logging

from textual.widgets import Static, Button, Select
from textual import events

from src.sound import Synth, LFOTypes

logger = logging.getLogger(__name__)


class ControlPanel(Static):
    def __init__(self, *args, synth: Synth, **kwargs):
        super().__init__(*args, **kwargs)
        self.synth = synth

    def compose(self):
        lfo_types = [(name, key) for name, key in LFOTypes.__members__.items()]
        yield Select(
            lfo_types,
            prompt="Synth Type",
            value=LFOTypes.SAW_DOWN,
            id="select-lfo-type",
        )

    def on_select_changed(self, event: Select.Changed):
        logger.info(f"Event {event.select.id} - {event.__dict__}")
        if event.select.id == "select-lfo-type":
            self.synth.update_synths(lfo_type=event.value)


class KeyboardKey(Button):
    def __init__(self, *args, synth: Synth, **kwargs):
        super().__init__(*args, **kwargs)
        self.synth = synth

    @property 
    def key_id(self) -> str:
        return self.id.split("-")[1].upper()

    async def _on_mouse_down(self, event: events.MouseDown):
        print("Mouse down on the button!", self.key_id)
        self.synth.play_key(self.key_id)

    async def _on_mouse_up(self, event: events.MouseDown):
        print("Mouse down on button!", self.key_id)
        self.synth.stop_key(self.key_id)


class Keyboard(Static):
    def __init__(self, *args, synth: Synth, **kwargs):
        super().__init__(*args, **kwargs)
        self.synth = synth

    def _make_key_button(self, key: str, classes: str): 
        return KeyboardKey(
            label=key, id=f"note-{key.lower()}", classes=classes, synth=self.synth
        )

    def compose(self):
        key_classes = "keyboard-button"
        for key_name in self.synth.key_configs.keys():
            yield self._make_key_button(key_name, key_classes)
