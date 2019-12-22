import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

import mcpi.block as block 
import time
import random
from threading import Thread

gameOver = False


ARENAX = 10
ARENAZ = 40
ARENAY = 4
arenaPos = mc.player.getTilePos()

def arena(pos):
    
    mc.setBlocks(pos.x - 1 , pos.y, pos.z - 1, pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1, 24)
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1, pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1, 95)
    mc.setBlocks(pos.x, pos.y + 1, pos.z, pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ, block.AIR.id)
    mc.setBlocks(pos.x+ARENAX-10,pos.y,pos.z+ARENAZ-5,pos.x+ARENAX,pos.y,pos.z+ARENAZ-1,0)
    mc.setBlocks(pos.x+ARENAX-10,pos.y,pos.z+ARENAZ-5,pos.x+ARENAX,pos.y,pos.z+ARENAZ-1,182)
    



def wall(arenaPos, wallZPos):
    wallPos =  minecraft.Vec3(arenaPos.x-7, arenaPos.y + 1, arenaPos.z + wallZPos)
    while not gameOver:
        wall = [0,1]
        for i in wall:
            mc.setBlocks(wallPos.x+1, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX+1, wallPos.y+ARENAY+1, wallPos.z+i, block.AIR.id) 
            mc.setBlocks(wallPos.x+2, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX+2, wallPos.y+ARENAY+1, wallPos.z+i, 103)   
            time.sleep(0.5)
        
        #подъем стен
        for i in wall:
            mc.setBlocks(wallPos.x+2, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX+2, wallPos.y+ARENAY+1, wallPos.z+i, block.AIR.id)
            mc.setBlocks(wallPos.x+1, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX+1, wallPos.y+ARENAY+1, wallPos.z+i, 103)  
            time.sleep(0.5)
        time.sleep(1)
def wall2(arenaPos,wallZPos):
    wallPos =  minecraft.Vec3(arenaPos.x+8, arenaPos.y + 1, arenaPos.z + wallZPos)
    while not gameOver:
        wall = [0,1]
        for i in wall:
            mc.setBlocks(wallPos.x-1, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX-1, wallPos.y+ARENAY+1, wallPos.z+i, block.AIR.id) 
            mc.setBlocks(wallPos.x-2, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX-2, wallPos.y+ARENAY+1, wallPos.z+i, 103)   
            time.sleep(0.5)
        
        
        for i in wall:
            mc.setBlocks(wallPos.x-2, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX-2, wallPos.y+ARENAY+1, wallPos.z+i, block.AIR.id)
            mc.setBlocks(wallPos.x-1, wallPos.y+1, wallPos.z+i, wallPos.x+ARENAX-1, wallPos.y+ARENAY+1, wallPos.z+i, 103)  
            time.sleep(0.5)
        time.sleep(1)


def bridge(arenaPos, riverZPos):
    RIVERWIDTH = 6
    BW = 1
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos, arenaPos.x + ARENAX, arenaPos.y, arenaPos.z + riverZPos + RIVERWIDTH - 1, block.AIR.id)
    mc.setBlocks(arenaPos.x, arenaPos.y - 3, arenaPos.z + riverZPos, arenaPos.x + ARENAX, arenaPos.y - 4, arenaPos.z + riverZPos + RIVERWIDTH - 1, 24)
    mc.setBlocks(arenaPos.x, arenaPos.y - 3, arenaPos.z + riverZPos, arenaPos.x + ARENAX, arenaPos.y - 3, arenaPos.z + riverZPos + RIVERWIDTH - 1, 198)
    bridgePos = minecraft.Vec3(arenaPos.x, arenaPos.y-1, arenaPos.z + riverZPos + 1)
    while not gameOver:
        #в одну сторону
        for i in range(1, ARENAX-1):
            mc.setBlocks(bridgePos.x+i-1, bridgePos.y, bridgePos.z, bridgePos.x+BW+i-1, bridgePos.y-1, bridgePos.z+1, block.AIR.id) 
            mc.setBlocks(bridgePos.x+i, bridgePos.y, bridgePos.z, bridgePos.x+BW+i, bridgePos.y-1, bridgePos.z+1, 181)   
            time.sleep(1)
            
        #в другую сторону
        for i in reversed(range(1, ARENAX-1)):
            mc.setBlocks(bridgePos.x+i+1, bridgePos.y, bridgePos.z, bridgePos.x+BW+i+1, bridgePos.y-1, bridgePos.z+1, block.AIR.id)
            mc.setBlocks(bridgePos.x+i, bridgePos.y, bridgePos.z, bridgePos.x+BW+i, bridgePos.y-1, bridgePos.z+1, 181)
            time.sleep(1)

def anvils(arenaPos, anvilsZPos):  
    ANVILS = 30
    HOLESWIDTH = 4
    
    while not gameOver:
        
        anvils = []
        for count in range(0,ANVILS):
            x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
            z = random.randint(arenaPos.z + anvilsZPos, arenaPos.z + anvilsZPos + HOLESWIDTH)
            anvils.append(minecraft.Vec3(x, arenaPos.y, z))
        
        for anvil in anvils:
            mc.setBlock(anvil.x, anvil.y+10, anvil.z, block.WOOL.id, 12)
        time.sleep(0.5)
 
        for anvil in anvils:
            mc.setBlocks(anvil.x, anvil.y+10, anvil.z, anvil.x, anvil.y+10, anvil.z,145 )
        time.sleep(1)

        for anvil in anvils:
            mc.setBlocks(anvil.x, anvil.y+1, anvil.z, anvil.x, anvil.y+1, anvil.z, block.AIR.id)
            time.sleep(0.01)


def lava(arenaPos,lavaZPos):
    LW = 1
    LAVALAKEWIDH = 5
    lavaLakePos = minecraft.Vec3(arenaPos.x, arenaPos.y-1, arenaPos.z + lavaZPos + 1)
    mc.setBlocks(arenaPos.x, arenaPos.y, arenaPos.z + lavaZPos-1, arenaPos.x + ARENAX, arenaPos.y, arenaPos.z + lavaZPos + LAVALAKEWIDH - 1+1, 0)
    while not gameOver:
        for i in range(1):
            mc.setBlocks(arenaPos.x, arenaPos.y-1, arenaPos.z + lavaZPos, arenaPos.x + ARENAX, arenaPos.y-1, arenaPos.z + lavaZPos + LAVALAKEWIDH - 1, 0)
            time.sleep(5) 
            mc.setBlocks(arenaPos.x, arenaPos.y-1, arenaPos.z + lavaZPos, arenaPos.x + ARENAX, arenaPos.y-1, arenaPos.z + lavaZPos + LAVALAKEWIDH - 1, 11)
            time.sleep(5)
                 
        

def cake(arenaPos, number):
    for diamond in range(0, number):
        x = random.randint(arenaPos.x+1, arenaPos.x + ARENAX-1)
        z = random.randint(arenaPos.z+1, arenaPos.z + ARENAZ-8)
        mc.setBlock(x, arenaPos.y + 1, z, 92)

arena(arenaPos)


WALLZ=16
thread1 = Thread(target = wall, args=(arenaPos, WALLZ))
WALLZ=16
thread2 = Thread(target = wall2, args = (arenaPos, WALLZ))
RIVERZ = 6
thread3 = Thread (target = bridge, args = (arenaPos,RIVERZ))
ANVILSZ = 35
thread4 = Thread(target = anvils, args = (arenaPos,ANVILSZ))
LAVAZ = 27
thread5 = Thread(target = lava, args = (arenaPos,LAVAZ))


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()



LEVELS = 3
CAKES = [3,5,9]
TIMEOUTS = [40,57,68]
level = 0
points = 0
#game loop
while not gameOver:
    cake(arenaPos, CAKES[level])
    cakesLeft = CAKES[level]
    mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)
    start = time.time()
    levelComplete = False
    #level loop
    while not gameOver and not levelComplete:

        pos = mc.player.getTilePos()
        if pos.y+1 < arenaPos.y:
            mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)

            
        blockType = mc.getBlock(pos.x,pos.y,pos.z)

        
        if blockType == 11:
            mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)

        blockType = mc.getBlock(pos.x,pos.y,pos.z)
        if blockType == 145:
            mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)
            
        if pos.z == arenaPos.z + ARENAZ-1 and cakesLeft == 0:
             levelComplete = True
         
        secondsLeft = TIMEOUTS[level] - (time.time() - start)
        if secondsLeft < 0:
            gameOver = True
            mc.postToChat("Out of time...")
            
        time.sleep(0.1)
        hits = mc.events.pollBlockHits()
        for hit in hits:
            blockHitType =  mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
            if blockHitType == 92:
                mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, block.AIR.id)
                cakesLeft = cakesLeft - 1

    if levelComplete:
        points = points + (CAKES[level] * int(secondsLeft))
        mc.postToChat("Level Complete! Points = " + str(points))
        level = level + 1
        if level == LEVELS:
            gameOver = True
            mc.postToChat("Congratulations - All levels complete")
            thread1.join()
            thread2.join()
            thread3.join()
            thread4.join()
            thread5.join()
mc.postToChat("Game Over - Points = " + str(points))

