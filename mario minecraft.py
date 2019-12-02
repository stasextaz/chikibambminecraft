import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Hello")
import random
import mcpi. block as block
import keyboard
import time
import sys
import os

pos = mc.player.getPos()
blockType = mc.getBlock(pos.x,pos.y,pos.z)


xStart = pos.x
yStart = pos.y
zStart = pos.z


mc.setBlocks(xStart ,yStart-1,zStart,xStart+50,yStart-1,zStart + 50,45)


while True:
      pos = mc.player.getPos()
      
      
      
      mc.setBlock(xStart + random.randint(0,50),yStart,zStart + random.randint(0,50),41)
      time.sleep(5)
      
      x = pos.x
      y = pos.y
      z = pos.z
      blockType = mc.getBlock(pos.x,pos.y-1,pos.z)
      if (blockType == 41):
            mc.postToChat("zyzb")
            if keyboard.is_pressed('space'):
                        
                  mc.setBlock(x,y-1,z,0)
                  mc.setBlock(x,y-2,z,0)
                  mc.setBlock(x,y-2,z,45)
                  continue
            
      


