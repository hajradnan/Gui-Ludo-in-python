import time
from startposition import start
from tkinter import *
from movementofpawn import movement
from tkinter import messagebox

class game:
    def main_controller(self,obj, color_coin, coin_number):
        processing_result = obj.input_filtering(coin_number)# Value filtering
        if processing_result is True:
            pass
        else:
            messagebox.showerror("Wrong input","Please input the coin number between 1 to 4") #if player enters coin number other than 1,2,3 or 4
            return

        if  color_coin == "red":
            obj.rolldice[0][3]['state'] = DISABLED  #move button disabled after clicking on it
            if obj.move_red_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif obj.red_coin_position[int(coin_number)-1] == -1 and obj.move_red_counter == 6: 
                re=start()
                re.red_circle_start_position(obj,coin_number)
                obj.red_coord_store[int(coin_number) - 1] = 1

            elif obj.red_coin_position[int(coin_number)-1] > -1:
                take_coord = obj.excanvas.coords(obj.redcoin[int(coin_number)-1])
                red_start_label_x = take_coord[0] + 10
                red_start_label_y = take_coord[1] + 5
                obj.redlabel[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if obj.red_coin_position[int(coin_number)-1]+obj.move_red_counter<=106:
                   mo=movement()
                   obj.red_coin_position[int(coin_number)-1] = mo.motion_of_coin(obj,obj.red_coin_position[int(coin_number) - 1],obj.redcoin[int(coin_number)-1],obj.redlabel[int(coin_number)-1],red_start_label_x,red_start_label_y,"red",obj.move_red_counter)
                else:
                   messagebox.showerror("Not possible","No path available")
                   obj.rolldice[0][3]['state'] = NORMAL
                   return
                
                #if coin reaches at any of the stop or start of any team
                if  obj.red_coin_position[int(coin_number)-1]==22 or obj.red_coin_position[int(coin_number)-1]==9 or obj.red_coin_position[int(coin_number)-1]==48 or obj.red_coin_position[int(coin_number)-1]==35 or obj.red_coin_position[int(coin_number)-1]==14 or obj.red_coin_position[int(coin_number)-1]==27 or obj.red_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if obj.red_coin_position[int(coin_number) - 1] < 100:
                        obj.coord_overlap(obj.red_coin_position[int(coin_number)-1],color_coin, obj.move_red_counter)

                obj.red_coord_store[int(coin_number)-1] = obj.red_coin_position[int(coin_number)-1]

            else:
                messagebox.showerror("Choice Error","Sorry, Your coin is not permitted to travel")
                obj.rolldice[0][3]['state'] = NORMAL
                return

            obj.rolldice[0][1]['state'] = NORMAL



         #*************************************************************************************************************************************************************************


        elif color_coin == "blue":
            obj.rolldice[1][3]['state'] = DISABLED
            if obj.move_red_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif obj.blue_coin_position[int(coin_number) - 1] == -1 and obj.move_blue_counter == 6:
                bl=start()
                bl.blue_circle_start_position(obj,coin_number)
                obj.blue_coord_store[int(coin_number) - 1] = 40

            elif obj.blue_coin_position[int(coin_number) - 1] > -1:
                take_coord = obj.excanvas.coords(obj.bluecoin[int(coin_number) - 1])
                blue_start_label_x = take_coord[0] + 10
                blue_start_label_y = take_coord[1] + 5
                obj.bluelabel[int(coin_number) - 1].place(x=blue_start_label_x, y=blue_start_label_y)

                if  obj.blue_coin_position[int(coin_number) - 1] + obj.move_blue_counter <= 106:
                    mo=movement()
                    obj.blue_coin_position[int(coin_number) - 1] = mo.motion_of_coin(obj,obj.blue_coin_position[int(coin_number) - 1], obj.bluecoin[int(coin_number) - 1], obj.bluelabel[int(coin_number) - 1], blue_start_label_x, blue_start_label_y, "blue", obj.move_blue_counter)
                else:
                   messagebox.showerror("Not possible","No path available")
                   obj.rolldice[1][3]['state'] = NORMAL
                   return

                if  obj.blue_coin_position[int(coin_number)-1]==22 or obj.blue_coin_position[int(coin_number)-1]==9 or obj.blue_coin_position[int(coin_number)-1]==48 or obj.blue_coin_position[int(coin_number)-1]==35 or obj.blue_coin_position[int(coin_number)-1]==1 or obj.blue_coin_position[int(coin_number)-1]==14 or obj.blue_coin_position[int(coin_number)-1]==27:
                    pass
                else:
                    if obj.blue_coin_position[int(coin_number) - 1] < 100:
                        obj.coord_overlap(obj.blue_coin_position[int(coin_number) - 1],color_coin, obj.move_blue_counter)

                obj.blue_coord_store[int(coin_number) - 1] = obj.blue_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin is not permitted to travel")
                obj.rolldice[1][3]['state'] = NORMAL
                return

            obj.rolldice[1][1]['state'] = NORMAL
        
        #*************************************************************************************************************************************************************************


        elif color_coin == "yellow":
            obj.rolldice[2][3]['state'] = DISABLED

            if obj.move_yellow_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif obj.yellow_coin_position[int(coin_number) - 1] == -1 and obj.move_yellow_counter == 6:
                ye=start()
                ye.yellow_circle_start_position(obj,coin_number)
                obj.yellow_coord_store[int(coin_number) - 1] = 27

            elif obj.yellow_coin_position[int(coin_number) - 1] > -1:
                take_coord = obj.excanvas.coords(obj.yellowcoin[int(coin_number) - 1])
                yellow_start_label_x = take_coord[0] + 10
                yellow_start_label_y = take_coord[1] + 5
                obj.yellowlabel[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

                if  obj.yellow_coin_position[int(coin_number) - 1] + obj.move_yellow_counter <= 106:
                    mo=movement()
                    obj.yellow_coin_position[int(coin_number) - 1] = mo.motion_of_coin(obj,obj.yellow_coin_position[int(coin_number) - 1], obj.yellowcoin[int(coin_number) - 1], obj.yellowlabel[int(coin_number) - 1], yellow_start_label_x, yellow_start_label_y, "yellow", obj.move_yellow_counter)
                else:
                    messagebox.showerror("Not possible","No path available")
                    obj.rolldice[2][3]['state'] = NORMAL
                    return

                if  obj.yellow_coin_position[int(coin_number)-1]==22 or obj.yellow_coin_position[int(coin_number)-1]==9 or obj.yellow_coin_position[int(coin_number)-1]==48 or obj.yellow_coin_position[int(coin_number)-1]==35 or obj.yellow_coin_position[int(coin_number)-1]==1 or obj.yellow_coin_position[int(coin_number)-1]==14 or obj.yellow_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if obj.yellow_coin_position[int(coin_number) - 1] < 100:
                        obj.coord_overlap(obj.yellow_coin_position[int(coin_number) - 1],color_coin, obj.move_yellow_counter)

                obj.yellow_coord_store[int(coin_number) - 1] = obj.yellow_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                obj.rolldice[2][3]['state'] = NORMAL
                return

            obj.rolldice[2][1]['state'] = NORMAL        



         #*************************************************************************************************************************************************************************
            
        elif color_coin == "green":
            obj.rolldice[3][3]['state'] = DISABLED

            if obj.move_green_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif obj.green_coin_position[int(coin_number) - 1] == -1 and obj.move_green_counter == 6:
                gr=start()
                gr.green_circle_start_position(obj,coin_number)
                obj.green_coord_store[int(coin_number) - 1] = 14

            elif obj.green_coin_position[int(coin_number) - 1] > -1:
                take_coord = obj.excanvas.coords(obj.greencoin[int(coin_number) - 1])
                green_start_label_x = take_coord[0] + 10
                green_start_label_y = take_coord[1] + 5
                obj.greenlabel[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)


                if  obj.green_coin_position[int(coin_number) - 1] + obj.move_green_counter <= 106:
                    mo=movement()
                    obj.green_coin_position[int(coin_number) - 1] = mo.motion_of_coin(obj,obj.green_coin_position[int(coin_number) - 1], obj.greencoin[int(coin_number) - 1], obj.greenlabel[int(coin_number) - 1], green_start_label_x, green_start_label_y, "green", obj.move_green_counter)
                else:
                   messagebox.showerror("Not possible","No path available")
                   obj.rolldice[3][3]['state'] = NORMAL
                   return


                if  obj.green_coin_position[int(coin_number)-1]==22 or obj.green_coin_position[int(coin_number)-1]==9 or obj.green_coin_position[int(coin_number)-1]==48 or obj.green_coin_position[int(coin_number)-1]==35 or obj.green_coin_position[int(coin_number)-1]==1 or obj.green_coin_position[int(coin_number)-1]==27 or obj.green_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if obj.green_coin_position[int(coin_number) - 1] < 100:
                        obj.coord_overlap(obj.green_coin_position[int(coin_number) - 1],color_coin, obj.move_green_counter)

                obj.green_coord_store[int(coin_number) - 1] = obj.green_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                obj.rolldice[3][3]['state'] = NORMAL
                return

            obj.rolldice[3][1]['state'] = NORMAL


        

        print(obj.red_coord_store)
        print(obj.green_coord_store)
        print(obj.yellow_coord_store)
        print(obj.blue_coord_store)

        permission_granted_to_proceed = True

        if  color_coin == "red" and obj.red_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = obj.check_winner_and_runner(color_coin)
        elif  color_coin == "green" and obj.green_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = obj.check_winner_and_runner(color_coin)
        elif  color_coin == "yellow" and obj.yellow_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = obj.check_winner_and_runner(color_coin)
        elif  color_coin == "blue" and obj.blue_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = obj.check_winner_and_runner(color_coin)

        if permission_granted_to_proceed:# if that is False, Game is over and not proceed more
            obj.make_command()
