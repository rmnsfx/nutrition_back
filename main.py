import uuid
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from base64 import b64encode


class Food:
    def __init__(self, title, weight, foodid):
        self.title = title
        self.weight = weight
        self.foodid = foodid
        self.id = str(uuid.uuid4())


class Training:
    def __init__(self, title, repeat, quantity, day):
        self.title = title
        self.repeat = repeat
        self.quantity = quantity
        self.day = day
        self.id = str(uuid.uuid4())


class Measure:
    def __init__(self, name, date, value):
        self.phase = name
        self.date = date
        self.value = value
        self.id = str(uuid.uuid4())


food = [Food("Каша", 50, "завтрак"),  Food("Овощи", 150, "завтрак"), Food("Коктейль", 15, "завтрак"),
        Food("Суп", 150, "перекус_1"), Food("Макароны", 50, "перекус_1"),
        Food("Щи", 150, "обед"), Food("Компот", 150, "обед"),
        Food("Печенье", 150, "перекус_2"),
        Food("Чай", 150, "ужин"), Food("Кефир", 150, "ужин"), ]

training = [Training("Выпады", 4, 15, 'пн'), Training("Подтягивание", 3, 15, 'вт')]
measure = [Measure("Вес тела", "01.05.2023", 75)]

app = FastAPI()


@app.get("/api/food")
def get_food():
    return food

@app.get("/api/training")
def get_training():
    return training

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")
