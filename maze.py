import os
import random
import readchar

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

NUM_OBJECTS_MAP = 11

my_position = [3,1]
tail = []
map_objects = []

while len(map_objects) < NUM_OBJECTS_MAP:
    new_position = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
    
    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)
    
    
print(map_objects)
while True:
    #Draw Map
    
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range (MAP_HEIGHT):
        print("|", end="")
        
        
        for coordinate_x in range(MAP_WIDTH):
            
            char_to_draw = " "
            object_in_cell = None
            
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object
                    
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y :
                char_to_draw = "@"  
                
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail += 1
                 
                
            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
   

    # Ask user where he wants to move

    direction = readchar.readchar()
    
    if direction == "w":                            # if direction == "w":
      tail.insert(0, my_position)
      my_position[POS_Y] -= 1                       #     my_position[POS_Y] -= 1
      my_position[POS_Y] %= MAP_HEIGHT              #     if my_position[POS_Y] < 0:
    elif direction == "s":                          #         my_position[POS_Y] = MAP_HEIGHT - 1
      tail.insert(0, my_position)
      my_position[POS_Y] += 1                       # elif direction == "s":
      my_position[POS_Y] %= MAP_HEIGHT              #     my_position[POS_Y] += 1
    elif direction == "a":                          #     if my_position[POS_Y] >= MAP_HEIGHT:
      tail.insert(0, my_position)
      my_position[POS_X] -= 1                       #         my_position[POS_Y] = 0
      my_position[POS_X] %= MAP_WIDTH               # elif direction == "a":
    elif direction == "d":                          #     my_position[POS_X] -= 1
      tail.insert(0, my_position)
      my_position[POS_X] += 1                       #     if my_position[POS_X] < 0:
      my_position[POS_X] %= MAP_WIDTH               #         my_position[POS_X] = MAP_WIDTH - 1
    else:                                           # elif direction == "d":
      if direction == "u":                          #     my_position[POS_X] += 1
        break                                       #     if my_position[POS_X] >= MAP_WIDTH:
                                                    #         my_position[POS_X] = 0
                                                    # else:
                                                    #     if direction == "u":
                                                    #         break
    
    os.system("cls")