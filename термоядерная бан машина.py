from mcpi.minecraft import Minecraft

mc = Minecraft.create()
import keyboard
import sys
import mcpi.block as block

pos = mc.player.getPos()

x = round(pos.x)
y = round(pos.y)
z = round(pos.z)

myBlock = block.TNT.id

mc.setBlocks(x,y,z,x+10,y,z-10,myBlock)
mc.setBlocks(x,y,z,x-10,y,z+10,myBlock)
mc.setBlocks(x+10,y,z-10,x,y,z+10,myBlock)
mc.setBlocks(x-10,y,z+10,x,y,z-10,myBlock)

#fire

myBlock = block.FIRE.id
mc.setBlocks(x,y+1,z,x+10,y+1,z-10,myBlock)
mc.setBlocks(x,y+1,z,x-10,y+1,z+10,myBlock)
mc.setBlocks(x+10,y+1,z-10,x,y+1,z+10,myBlock)
mc.setBlocks(x-10,y+1,z+10,x,y+1,z-10,myBlock)
while True:
      
      
      
      if keyboard.is_pressed('l'):
            sys.exit()
