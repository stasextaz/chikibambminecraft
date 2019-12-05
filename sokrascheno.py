from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import keyboard
import random


def teleport():
    distance = random.randint(5, 50)
    direction = mc.player.getDirection()
    pos = mc.player.getTilePos()
    x = round(pos.x + distance*direction.x)
    y = round(pos.y + distance*direction.y)
    z = round(pos.z + distance*direction.z)
    mc.player.setTilePos(x, y, z)
    mc.postToChat("distance: "+str(distance)+" x: "+str(x)+" y: "+str(y) +" z: "+str(z))


while True:
    if keyboard.is_pressed('r'):
        teleport()
        time.sleep(1)
        

