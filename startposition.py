import time
from tkinter import *

class start:
    def red_circle_start_position(self,obj,coin_number): #it basically changes position of coin from home to position at start of team
        obj.excanvas.delete(obj.redcoin[int(coin_number)-1])
        obj.redcoin[int(coin_number)-1] = obj.excanvas.create_oval(140, 255, 180, 295, fill="red", width=2, outline="black")

        obj.redlabel[int(coin_number)-1].place_forget()
        red_start_label_x = 150
        red_start_label_y = 260
        obj.redlabel[int(coin_number)-1].place(x=red_start_label_x, y=red_start_label_y)

        obj.red_coin_position[int(coin_number)-1] = 1 #sets to 1 when pawn is outside
        obj.window.update()
        time.sleep(0.2)


    def green_circle_start_position(self,obj,coin_number):
        obj.excanvas.delete(obj.greencoin[int(coin_number)-1])
        obj.greencoin[int(coin_number)-1] = obj.excanvas.create_oval(420,55,460,95, fill="green", width=2)

        obj.greenlabel[int(coin_number)-1].place_forget()
        green_start_label_x = 430
        green_start_label_y = 60
        obj.greenlabel[int(coin_number)-1].place(x=green_start_label_x, y=green_start_label_y)

        obj.green_coin_position[int(coin_number)-1] = 14
        obj.window.update()
        time.sleep(0.2)


    def yellow_circle_start_position(self,obj,coin_number):
        obj.excanvas.delete(obj.yellowcoin[int(coin_number)-1])
        obj.yellowcoin[int(coin_number)-1] = obj.excanvas.create_oval(620, 335, 660,375, fill="yellow", width=2)

        obj.yellowlabel[int(coin_number)-1].place_forget()
        yellow_start_label_x = 630
        yellow_start_label_y = 340
        obj.yellowlabel[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

        obj.yellow_coin_position[int(coin_number) - 1] = 27
        obj.window.update()
        time.sleep(0.2)


    def blue_circle_start_position(self,obj,coin_number):
        obj.excanvas.delete(obj.bluecoin[int(coin_number)-1])
        obj.bluecoin[int(coin_number)-1] = obj.excanvas.create_oval(340,535,380,575,fill="blue",width=2)

        obj.bluelabel[int(coin_number)-1].place_forget()
        blue_start_label_x = 100+240 + 10
        blue_start_label_y = 340+(40*5)-5 + 5
        obj.bluelabel[int(coin_number) - 1].place(x=blue_start_label_x, y=blue_start_label_y)

        obj.blue_coin_position[int(coin_number) - 1] = 40
        obj.window.update()
        time.sleep(0.2)
