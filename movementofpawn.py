import time
from tkinter import*
from tkinter import messagebox

class movement:
    def motion_of_coin(self,obj,counter_coin,specific_coin,number_label,number_label_x ,number_label_y,color_coin,path_counter):
        number_label.place(x=number_label_x,y=number_label_y)
        while True:
            if path_counter == 0:
                break
            elif (counter_coin == 51 and color_coin == "red") or (counter_coin==12 and color_coin == "green") or (counter_coin == 25 and color_coin == "yellow") or (counter_coin == 38 and color_coin == "blue") or counter_coin>=100:
                if counter_coin<100:
                    counter_coin=100

                counter_coin = obj.under_room_traversal_control(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin, color_coin)

                if  counter_coin == 106:
                    messagebox.showinfo("Destination reached","Congrats! You have reached at the destination")
                    if path_counter == 6:
                        obj.six_with_overlap = 1
                    else:
                        obj.timetaken -= 1
                break

            counter_coin += 1
            path_counter -=1
            number_label.place_forget()

            print(counter_coin) #position changes according to moves

            if counter_coin<=5:
                obj.excanvas.move(specific_coin, 40, 0)
                number_label_x+=40
            elif counter_coin == 6:
                obj.excanvas.move(specific_coin, 40, -40)
                number_label_x += 40
                number_label_y-=40
            elif 6< counter_coin <=11:
                obj.excanvas.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin <=13:
                obj.excanvas.move(specific_coin, 40, 0)
                number_label_x += 40
            elif counter_coin <=18:
                obj.excanvas.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin == 19:
                obj.excanvas.move(specific_coin, 40, 40)
                number_label_x += 40
                number_label_y += 40
            elif counter_coin <=24:
                obj.excanvas.move(specific_coin, 40, 0)
                number_label_x += 40
            elif counter_coin <=26:
                obj.excanvas.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin <=31:
                obj.excanvas.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif counter_coin == 32:
                obj.excanvas.move(specific_coin, -40, 40)
                number_label_x -= 40
                number_label_y += 40
            elif counter_coin <= 37:
                obj.excanvas.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin <= 39:
                obj.excanvas.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif counter_coin <= 44:
                obj.excanvas.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin == 45:
                obj.excanvas.move(specific_coin, -40, -40)
                number_label_x -= 40
                number_label_y -= 40
            elif counter_coin <= 50:
                obj.excanvas.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif 50< counter_coin <=52:
                obj.excanvas.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin == 53:
                obj.excanvas.move(specific_coin, 40, 0)
                number_label_x += 40
                counter_coin = 1

            number_label.place_forget()
            number_label.place(x=number_label_x, y=number_label_y)

            obj.window.update()
            time.sleep(0.2)

        return counter_coin
