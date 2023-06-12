import uuid
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


class Food:
    def __init__(self, title, weight):
        self.title = title
        self.weight = weight
        self.id = str(uuid.uuid4())


class Training:
    def __init__(self, name, phase, repeat, quantity):
        self.phase = name
        self.phase = phase
        self.repeat = repeat
        self.quantity = quantity
        self.id = str(uuid.uuid4())


class Measure:
    def __init__(self, name, date, value):
        self.phase = name
        self.date = date
        self.value = value
        self.id = str(uuid.uuid4())


food = [Food("Овсянка", 50), Food("Овощи", 150)]
training = [Training("Выпады", 4, 15, 5), Training("Подтягивание", 3, 15, 95)]
measure = [Measure("Вес тела", "01.05.2023", 75)]

app = FastAPI()


@app.get("/api/food")
def get_food():
    return food

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")

