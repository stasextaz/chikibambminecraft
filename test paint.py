from mcpi.minecraft import Minecraft
mc = Minecraft.create()


import time
import random
import keyboard
from threading import Thread
import mcpi.block as block

pos = mc.player.getTilePos()



mc.setBlocks(pos.x+8,pos.y,pos.z-20,pos.x+8,pos.y+40,pos.z+40,block.WOOD_PLANKS.id)
mc.setBlocks(pos.x+8,pos.y+1,pos.z-19,pos.x+8,pos.y+39,pos.z+39,block.WOOL.id)
hits = mc.events.pollBlockHits()
    
        
   
    
    
while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
                
        blockHitType =  mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
        if blockHitType == block.WOOL.id:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 222)
            


        break
    for hit in hits:
    
        if blockHitType == 222:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 223)
        
        break
    for hit in hits:
    
        if blockHitType == 223:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 224)
        
    for hit in hits:
    
        if blockHitType == 224:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 225)

        break
    for hit in hits:
    
        if blockHitType == 225:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 226)

        break
    for hit in hits:
    
        if blockHitType == 226:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 221)

        break
    for hit in hits:
    
        if blockHitType == 221:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 227)

        break
    for hit in hits:
    
        if blockHitType == 227:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 228)

        break
    for hit in hits:
    
        if blockHitType == 228:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 229)

        break
    for hit in hits:
    
        if blockHitType == 229:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 230)

        break
    for hit in hits:
    
        if blockHitType == 230:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 231)

        break
    for hit in hits:
    
        if blockHitType == 231:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 232)

        break
    for hit in hits:
    
        if blockHitType == 232:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 233)

        break
    for hit in hits:
    
        if blockHitType == 233:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, 234)

        break
    for hit in hits:
    
        if blockHitType == 234:
            mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, block.WOOL.id)

        break




            
