from repo.city_repo import CityRepo
from ui.ui import UI

city_repo = CityRepo(0, 0, 100, 1000, 3, 200, 20, 2800)

ui = UI(city_repo)
ui.start()
