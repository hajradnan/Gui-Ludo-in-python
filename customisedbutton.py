from tkinter import *


class btn:
    def instructionalandcustomisedbutton(self,obj,color_indicator,permanent_block_number,block_value_predict):
        if color_indicator == "red":
            temp_coin_position = obj.red_coin_position
        elif color_indicator == "green":
            temp_coin_position = obj.green_coin_position
        elif color_indicator == "yellow":
            temp_coin_position = obj.yellow_coin_position
        elif color_indicator == "blue":
            temp_coin_position = obj.blue_coin_position

        all_in = 1
        for i in range(4):
            if temp_coin_position[i] == -1:
                all_in = 1
            else:
                all_in = 0
                break

        if  permanent_block_number == 6:
            obj.six_counter += 1
        else:
            obj.six_counter = 0

        if ((all_in == 1 and permanent_block_number == 6) or (all_in==0)) and obj.six_counter<3:
            permission = 1
            if color_indicator == "red":
                temp = obj.red_coord_store
            elif color_indicator == "green":
                temp = obj.green_coord_store
            elif color_indicator == "yellow":
                temp = obj.yellow_coord_store
            else:
                temp = obj.blue_coord_store

            if  permanent_block_number<6:
                if obj.six_with_overlap == 1:
                    obj.timetaken-=1
                    obj.six_with_overlap=0
                for i in range(4):
                    if  temp[i] == -1:
                        permission=0
                    elif temp[i]>100:
                        if  temp[i]+permanent_block_number<=106:
                            permission=1
                            break
                        else:
                            permission=0
                    else:
                        permission=1
                        break
            else:
                for i in range(4):
                    if  temp[i]>100:
                        if  temp[i] + permanent_block_number <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            if permission == 0:
                obj.make_command()
            else:
                block_value_predict[3]['state'] = NORMAL# Move button activation
                block_value_predict[1]['state'] = DISABLED# Roll button deactivation

        else:
            block_value_predict[1]['state'] = NORMAL # Roll button activation
            if obj.six_with_overlap == 1:
                obj.timetaken -= 1
                obj.six_with_overlap = 0
            obj.make_command() 

        if  permanent_block_number == 6 and obj.six_counter<3 and block_value_predict[3]['state'] == NORMAL: 
            obj.timetaken-=1
        else:
            obj.six_counter=0
