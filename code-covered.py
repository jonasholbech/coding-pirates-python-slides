import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

#teleporter spilleren til 0,0,0
mc.player.setTilePos(0,0,0)

#skriv en besked i chatten
mc.postToChat("Hej Verden")
            
#Sæt en træ-blok
mc.setBlock(x, y, z, block.WOOD.id)

#spawn en "entity"
mc.spawnEntity(0, 2, 0, entity.CHICKEN.id)

#lav en variabel (pos)
#der indeholder spillerens koordinater
pos = mc.player.getPos()

mc.setBlocks(x1, y1, z1, x2, y2, z2, block.WOOD.id)
     

while True:
      pos = mc.player.getPos()
      mc.setBlock(pos.x, pos.y, pos.z, block.TNT.id)
      time.sleep(0.1)

import random

myNumber = random.randint(1, 10)

age = 10
if age > 17:
      print("Du må køre bil")
elif age > 6:
      print("Du går nok i skole")
else:
      print("Børnehave?")