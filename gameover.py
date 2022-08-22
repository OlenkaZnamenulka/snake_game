import sqlite3
from turtle import Turtle

ALIGMENT = "left"
ALIGMENT2 = "center"
FONT = ("Arial", 24, "normal")


class GameOver(Turtle):
    def __init__(self, user_name, user_score):
        super().__init__()

        db = sqlite3.connect('Database.db')
        self.cursor = db.cursor()
        # Создание БД и запись результа игры
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Sql_Database
                               (name text, score int)""")
        self.cursor.execute("INSERT INTO Sql_Database VALUES (?,?)", (user_name, user_score))

        # Сортировка по убыванию sql-таблицы и выгрузка первых трех записей в переменные
        self.cursor.execute("""SELECT * FROM Sql_Database ORDER BY score DESC""")
        records = self.cursor.fetchall()
        one = records[0]
        two = records[1]
        three = records[2]
        db.commit()
        self.cursor.close()
        # вывод результатов игры
        self.color("white")
        self.hideturtle()
        self.goto(0, 180)
        self.write("Конец игры!", align=ALIGMENT2, font=FONT)
        self.goto(0, 100)
        self.write("Таблица рекордов:", align=ALIGMENT2, font=FONT)
        self.goto(-100, 0)
        self.write((one[0] + " " + str(one[1])), align=ALIGMENT, font=FONT)
        self.goto(-100, -100)
        self.write((two[0] + " " + str(two[1])), align=ALIGMENT, font=FONT)
        self.goto(-100, -200)
        self.write((three[0]+" " + str(three[1])), align=ALIGMENT, font=FONT)
