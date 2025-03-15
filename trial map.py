from kivy.garden.mapview import MapView, MapSource
from kivy.app import App

class MapboxMapView(MapView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.map_source = MapSource(
            url="https://api.mapbox.com/styles/v1/shufla/cm7w6m8em00o301scf10zdpm9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic2h1ZmxhIiwiYSI6ImNtN3ZoNDI1eDBiczIybnNhbm9raHVrNnIifQ.T4bkVKCXu_t09rIOiTurmQ",
            attribution="© Mapbox",
            min_zoom=1,
            max_zoom=20
        )

class MapApp(App):
    def build(self):
        return MapboxMapView(zoom=10, lat=50.4501, lon=30.5234)  # Київ

if __name__ == "__main__":
    MapApp().run()
