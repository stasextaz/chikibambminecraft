from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import sys
import keyboard
import time
import mcpi.block as Block

def house():
    pos = mc.player.getPos()

    x = round(pos.x + 5)
    y = round(pos.y)
    z = round(pos.z + 5)
    #очитска
    blockId = Block.AIR.id
    mc.setBlocks(x,y,z,x+10,y,z-10,blockId)
    

    #cozdanie sten
    blockId = Block.STONE.id

    mc.setBlocks(x,y,z,x,y+4,z-10,blockId)
    mc.setBlocks(x,y,z-10,x+10,y+4,z-10,blockId)
    mc.setBlocks(x+10,y,z-10,x+10,y+4,z,blockId)
    mc.setBlocks(x,y,z,x+10,y+4,z,blockId)
    
    #okno
    blockId = Block.GLASS.id
    mc.setBlocks(x,y+1,z-7,x,y+2,z-8,blockId)
    mc.setBlocks(x,y+1,z-2,x,y+2,z-3,blockId)

    mc.setBlocks(x+2, y+1,z-10,x+3,y+2,z-10,blockId)
    mc.setBlocks(x+7,y+1,z-10,x+8,y+2,z-10,blockId)

    mc.setBlocks(x+10,y+1,z-7,x+10,y+2,z-8,blockId)
    mc.setBlocks(x+10,y+1,z-2,x+10,y+2,z-3,blockId)

    mc.setBlocks(x+2,y+1,z,x+3,y+2,z,blockId)
    mc.setBlocks(x+7,y+1,z,x+8,y+2,z,blockId)
    
    

    

    #krysha
    blockId = Block.WOOD_PLANKS.id
    mc.setBlocks(x-1, y + 5, z+1, x+11, y + 5, z-11, blockId)
    mc.setBlocks(x, y + 5 + 1, z, x+10, y + 5, z-10, blockId)
    mc.setBlocks(x+1, y + 5 + 2, z-1, x+9, y + 5, z-9,blockId)
    mc.setBlocks(x+2, y +5 + 3, z-2, x+8, y + 5, z-8, blockId)
    mc.setBlocks(x+3, y + 5 + 4, z-3, x+7, y + 5, z-7,blockId)
    mc.setBlocks(x+4, y + 5 + 5, z-4, x+6, y + 5, z-6, blockId)

    #pol
    mc.setBlocks(x, y -1, z, x+10, y -1, z-10, blockId)

    
    
    
    
    
house()
    
