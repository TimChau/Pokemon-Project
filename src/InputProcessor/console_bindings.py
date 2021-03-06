import commands

from kao_console.ascii import *

keyBindings = {KAO_UP:commands.UP,
               ord("w"):commands.UP,
               ord("W"):commands.UP,
               KAO_DOWN:commands.DOWN,
               ord("s"):commands.DOWN,
               ord("S"):commands.DOWN,
               KAO_LEFT:commands.LEFT,
               ord("a"):commands.LEFT,
               ord("A"):commands.LEFT,
               KAO_RIGHT:commands.RIGHT,
               ord("d"):commands.RIGHT,
               ord("D"):commands.RIGHT,
               ESCAPE:commands.EXIT,
               ENDL:commands.SELECT}
               
keyStrings = {KAO_UP:"UP ARROW",
              ord('W'):"W",
              ord('w'):"w",
              KAO_DOWN:"DOWN ARROW",
              ord('S'):"S",
              ord('s'):"s",
              KAO_LEFT:"LEFT ARROW",
              ord('A'):"A",
              ord('a'):"a",
              KAO_RIGHT:"RIGHT ARROW",
              ord('D'):"D",
              ord('d'):"d",
              ESCAPE:"ESCAPE",
              ENDL:"ENTER"}