import time
import pychromecast
from pychromecast.controllers import BaseController

APP_ID = "8B0C0E45"
CAST_NAME = "Diele"
NAMESPACE = "urn:x-cast:com.jarvis.receiver"


class JarvisController(BaseController):
    def __init__(self):
        super().__init__(NAMESPACE)

    def receive_message(self, message, data):
        print("Receiver:", data)
        return True

    def send(self, data):
        self.send_message(data)


print(f'Suche Chromecast "{CAST_NAME}"...')
chromecasts, browser = pychromecast.get_chromecasts()

try:
    cast = next(
        (
            c for c in chromecasts
            if c.cast_info.friendly_name.lower() == CAST_NAME.lower()
        ),
        None
    )

    if cast is None:
        raise RuntimeError("Chromecast nicht gefunden.")

    cast.wait()

    controller = JarvisController()
    cast.register_handler(controller)

    print("Starte JARVIS Receiver...")
    cast.start_app(APP_ID, force_launch=True)
    time.sleep(4)

    print("Sende Testansicht...")
    controller.send({
        "type": "SHOW_IDEAS",
        "title": "Was möchtest du kochen?",
        "subtitle": "JARVIS Receiver Test",
        "items": [
            {"title": "Carbonara", "description": "Cremig, herzhaft und schnell."},
            {"title": "Schweinefilet", "description": "Mit Pilzrahmsoße und Kartoffeln."},
            {"title": "Chili con Carne", "description": "Kräftig, würzig und unkompliziert."},
            {"title": "Flammkuchen", "description": "Knusprig mit Speck und Zwiebeln."}
        ]
    })

    time.sleep(20)

finally:
    pychromecast.discovery.stop_discovery(browser)
