from User_Objects.Armor import Armor
from User_Objects.Latern import Latern

from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant
from Characters.Blacksmith_Character import Blacksmith_Character


class winter_scene:
    inspectedHut, inspectedLake, inspectedShipwreck, inspectedPort, inspectedVillage, inspectedHouse, inspectedGraveyard, inspectedCoin, inspectedCave = False, False, False, False, False, False, False, False, False
    traveledHut, traveledLake, traveledVillage, traveledCave = False, False, False, False
    skeletonFelled, zombieFelled, bossFelled = False, False, False
    haveOre, haveSand, haveOil = False, False, False
    obtainedLatern = False
    enteredCave = False


    def run_scene(self, traveler: MainCharacter): # intro
        print("As you rush down the path, the snow seems to be unleashing a heavy flurry apon you.\nHowever you spot a light in the distance. As you close in you see the light is coming from a old circular hut made of jointed stone with a roof of tightly knitted hay.\n")
        print("Due to the cold, you walk through the door wihtout a second thought. You first see a blacksmith working away on a anvil, sparks causing a bright light and skrieking sound.\nYou then spot a familier merchant on the other side of the hut. The blacksmith the yells out directed towards you.\n")
        # incentive
        print("If you're headed towards the tower you're going to need to go through frostbitten cavrern.\nYou'll need me to craft you a latern powerful enough to take you through, else you'd be lukcy to get 20 feet.\n")
        # materials
        print("The iron and sand for one should be at the old lake, however, I think you'll need an oil wick. That should be in what's left of the village.\n")
        winter_scene.hut_decision(traveler)

    # travel scene functions
    def travelTo(traveler, currentLocation): # h = hut, l = lake, v = village, c = cave
        if(currentLocation=='h'):
            print("Where do you want to go:\n1 "+("*"if winter_scene.traveledLake else"-")+(" Frozen Lake"if winter_scene.traveledLake else" Old Lake")+"\n2 "+("*"if winter_scene.traveledVillage else"-")+" Village\n3 "+("*"if winter_scene.traveledCave else"-")+" Frostbitten Cavern\n")
            decision = int( input("User: ") )
            if(decision==1):
                print("\n")
                winter_scene.lake_scene(traveler, winter_scene.traveledLake)
            elif(decision==2):
                print("\n")
                winter_scene.village_scene(traveler, winter_scene.traveledVillage)
            elif(decision==3):
                print("\n")
                winter_scene.cave_scene(traveler, winter_scene.traveledCave)
            else:
                print("\nSadly you can't do that\n")
                winter_scene.travelTo(traveler, 'h')
        if(currentLocation=='l'):
            print("Where do you want to go:\n1 "+("*"if winter_scene.traveledHut else"-")+" Blacksmith's hut\n2 "+("*"if winter_scene.traveledVillage else"-")+" Village\n3 "+("*"if winter_scene.traveledCave else"-")+" Frostbitten Cavern\n")
            decision = int( input("User: ") )
            if(decision==1):
                print("\n")
                winter_scene.hut_scene(traveler, False)
            elif(decision==2):
                print("\n")
                winter_scene.village_scene(traveler, winter_scene.traveledVillage)
            elif(decision==3):
                print("\n")
                winter_scene.cave_scene(traveler, winter_scene.traveledCave)
            else:
                print("\nSadly you can't do that\n")
                winter_scene.travelTo(traveler, 'l')
        if(currentLocation=='v'):
            print("Where do you want to go:\n1 "+("*"if winter_scene.traveledHut else"-")+" Blacksmith's hut\n2 "+("*"if winter_scene.traveledLake else"-")+(" Frozen Lake"if winter_scene.traveledLake else" Old Lake")+"\n3 "+("*"if winter_scene.traveledCave else"-")+" Frostbitten Cavern\n")
            decision = int( input("User: ") )
            if(decision==1):
                print("\n")
                winter_scene.hut_scene(traveler, False)
            elif(decision==2):
                print("\n")
                winter_scene.lake_scene(traveler, winter_scene.traveledLake)
            elif(decision==3):
                print("\n")
                winter_scene.cave_scene(traveler, winter_scene.traveledCave)
            else:
                print("\nSadly you can't do that\n")
                winter_scene.travelTo(traveler, 'v')
        if(currentLocation=='c'):
            print("Where do you want to go:\n1 "+("*"if winter_scene.traveledHut else"-")+" Blacksmith's hut\n2 "+("*"if winter_scene.traveledLake else"-")+(" Frozen Lake"if winter_scene.traveledLake else" Old Lake")+"\n3 "+("*"if winter_scene.traveledVillage else"-")+" Villagen\n")
            decision = int( input("User: ") )
            if(decision==1):
                print("\n")
                winter_scene.hut_scene(traveler, False)
            elif(decision==2):
                print("\n")
                winter_scene.lake_scene(traveler, winter_scene.traveledLake)
            elif(decision==3):
                print("\n")
                winter_scene.village_scene(traveler, winter_scene.traveledVillage)
            else:
                print("\nSadly you can't do that\n")
                winter_scene.travelTo(traveler, 'c')
        
    # merchant scene
    def merchant_scene(traveler):
        # Creates items for the character to buy
        steelSwaord = Weapon("Steel Sword", "A weapon that deals damage to enemies.", True, 40, 50)
        helmet = Armor("Helmet", "Adds protection to any danger that approaches", True, 35, "head", 50)
        chestplate = Armor("Chestplate", "Adds protection to any danger that approaches", True, 50, "head", 75)

        merchant_store_list = [steelSwaord, helmet, chestplate]
        fall_scene_merchant = Merchant(merchant_store_list)
        fall_scene_merchant.merchant_dialogue(traveler)

        print(f"\nMain character's backpack: {traveler.backpack.backpack_storage}\n")
        print(f"Main character's coin storage: {traveler.coin_storage} coins\n")

    # functions for the hut scene
    def hut_scene(traveler, unconscious):
        if(unconscious):
            print("The Blacksmith sees that you are awake and smiles.\nGlad you're back on your feet.\n")
        else:
            print("You see the Blacksmith hammering away, he askes,\nWhat do you want?\n")
        winter_scene.hut_decision(traveler)

    def hut_decision(traveler):
        print(f"What do you want to do:\n1 "+("*"if winter_scene.inspectedHut else"-")+" Inspect Blacksmith's hut\n2 - Talk to Blacksmith\n3 - Talk to Merchant\n4 - Travel\n")
        decision = int( input("User: ") )
        if(decision==1):
            print("\nYou look around the small hut. On one side there is a small bed amd a hardy, wooden table. On the other is a small forge with a clearly used anvil next to it. The heat from the forge while hot left a happy,fuzzy feeling compared to the blistering cold outside.\n")
            winter_scene.hut_decision(traveler)
        elif(decision==2):
            blacksmith = Blacksmith_Character("Blacksmith")
            print("\n")
            blacksmith.Blacksmith_dialogue(traveler=traveler, haveOre=winter_scene.haveOre, haveSand=winter_scene.haveSand, haveOil=winter_scene.haveOil, tookCoin=winter_scene.inspectedCoin )
            winter_scene.hut_decision(traveler)
        elif(decision==3):
            print("\n")     
            winter_scene.merchant_scene(traveler)
            winter_scene.hut_decision(traveler)
        elif(decision==4):
            print("\n")
            winter_scene.travelTo(traveler, 'h')
        else:
            print("\nSadly you can't do that\n")
            winter_scene.hut_decision(traveler)

    # enemy fight scene
    def enemy_fight(traveler, enemy_name, enemy_health):
        print("Your health:\n")
        traveler.print_health_bar()

        print("The "+(enemy_name)+" with "+(str(enemy_health))+" health points, has challenged you to a battle.\n")

        if traveler.get_weapon()[1] < enemy_health :
            print("You lost the battle with the "+(enemy_name)+". You wake up at the Blacksmith's hut.\n")
            winter_scene.hut_scene(traveler, True)
            return False
        else:
            print("Congratulations, you beat the "+(enemy_name)+"!\nYou are awarded with 20 gold.\n")
            print("Your health:\n")
            traveler.print_health_bar()
            winter_scene.skeletonFelled=True
            traveler.coin_storage+=20
            return True


    # functions for the lake scene
    def lake_scene(traveler, firstTime):
        if(firstTime):
            winter_scene.traveledLake=True
            print("You look out over what the Blacksmith called the Old Lake. It looks much more like a desert of ice\nYou look around, seeing the remains of what looks like a small dock and some desolite ship sticking out of the ice.\n")
        else:
            print("You look back over the frozen shore, wondering if you missed something.\n")
        winter_scene.lake_decision(traveler)

    def lake_decision(traveler):
        print("What do you want to do:\n1 "+("*"if winter_scene.inspectedShipwreck else"-")+" Inspect Shipwreck\n2 "+("*"if winter_scene.inspectedPort else"-")+" Inspect Port\n3 "+("*"if winter_scene.inspectedLake else"-")+" Inspect Lake\n4 - Travel\n")
        decision=int( input("User: ") )
        if(decision==1):
            winter_scene.inspectedShipwreck=True
            print("\n")     # inspect shipwreck
            winter_scene.inspect_shipwreck(traveler)
            winter_scene.lake_decision(traveler)
        elif(decision==2):
            winter_scene.inspectedPort=True
            print("\n")     
            winter_scene.inspect_port(traveler)
            winter_scene.lake_decision(traveler)
        elif(decision==3):
            winter_scene.inspectedLake=True
            print("\nThe Lake looks completely frozen\nIt looks like a white desest with gusts of snow instead of sand.\n")
            winter_scene.lake_decision(traveler)
        elif(decision==4):
            print("\n")
            winter_scene.travelTo(traveler, 'l')
        else:
            print("\nSadly you can't do that\n")
            winter_scene.lake_decision(traveler)

    def inspect_shipwreck(traveler):
        print("The ship looked as if it was struck down the middle. It's main mast was cracked in half with its top being under the ice.\nHowever, you continue towards it and see that the Captain's Quarters are still intact.\nYou jump on the ship")

        if(not winter_scene.skeletonFelled):
            print(", however, as you do a skeleton lunges towards you.\n")
            winter_scene.skeletonFelled=winter_scene.enemy_fight(traveler,"Skeleton", 30)
        else:
            print(".\n")
        
        if not winter_scene.haveOre & winter_scene.skeletonFelled:
            print("After defeating the Skeleton, you journy on. And as you enter the Captain's Quarter, you notice a rock in the middle of the captain's desk.\nYou pick it up, it seems to be Iron. Good for the latern.\n")
            print("With not much else there to do you leave the ship.\n")
            winter_scene.lake_decision(traveler)
        
    def inspect_port(traveler):
        print("The port was small. Seemed to only be a small fishing port with some broken barrels and ripped net frozen to the ice and it's deck.\nIt's calm here. ")
        if not winter_scene.haveSand:
            print("You notice a small leather bag on one of the barrels. You pick it up, look inside, and feel coarse sand.\nThis will be good for the latern.\n")
        else:
            print("\n")


    # functions for the village scene
    def village_scene(traveler, firstTime):
        if firstTime:
            winter_scene.traveledVillage=True
            print("You look at what the Blacksmith called the village. It barely resembled one from what was left.\nThere stood one house with a what looked like a door way. However, the house's second story was leaning against the firsts side\nAside from the rubble and few standing structures. There was what looked to be a graveyard.\n")
        else:
            print("You look over the remain of the village and get a sense of dread. You want to get what you need so you can leave.\n")
        winter_scene.village_decision(traveler)

    def village_decision(traveler):
        print("What do you do:\n1 "+("*"if winter_scene.inspectedHouse else"-")+" Inspect Decrepit House\n2 "+("*"if winter_scene.inspectedGraveyard else"-")+" Inspect Graveyard\n3 "+("*"if winter_scene.inspectedVillage else"-")+" Inspect Village\n4 - Travel\n")
        decision=int( input("User: "))
        if(decision==1):
            print("\n")     
            winter_scene.inspect_house(traveler)
            winter_scene.village_decision(traveler)
        elif(decision==2):
            winter_scene.inspectedGraveyard=True
            if(not winter_scene.inspectedCoin):
                print("\nThere were a few piles of black, with specs of brown, rubble evenly space out from one another. While each covered in a layer snow, it was clear this debris were homes or houses.\nThere are flowers on the ground with a gold coin next to it.\n Do you take it?\n1 - yes\n2 - no\n")
                decisionC = int(input("User: "))
                if( decisionC==1):
                    winter_scene.inspectedCoin=True
                    print("You pick up the coin.")
                    traveler.coin_storage+=1
                    # give player a coin
                elif(decisionC==2):
                    print("You leave the coin.")
                winter_scene.village_decision(traveler)
            else:
                print("\nThere were a few piles of black, with specs of brown, rubble evenly space out from one another. While each covered in a layer snow, it was clear this debris were homes or houses.\nThere are flowers on the ground.\n")
                winter_scene.village_decision(traveler)
        elif(decision==3):
            print("\nThe village was nothing more than rubble. The houses were all burnt but also frozen over.\nIt is clear something bad happened here.\n")
            winter_scene.village_decision(traveler)
        elif(decision==4):
            print("\n")
            winter_scene.travelTo(traveler, 'v')
        else:
            print("\nSadly you can't do that\n")
            winter_scene.village_decision(traveler)

    def inspect_house(traveler):
        print("The house looks like a blackish-brown color, not natural but burnt. As to almost contrast that dark, there was a layer of snow covering the house.\nThere was no door, at least not anymore.") 
             
        if not winter_scene.zombieFelled:
            print(" As you walk in a zombie walks dives at you. Luckly you're able to avoid its attack but must fight back.\n")
            winter_scene.zombieFelled=winter_scene.enemy_fight(traveler,"Zombie", 35)
        
        if not winter_scene.haveOil & winter_scene.zombieFelled:
            print("After defeating the Zombie, you journy on. You see something on the dinner table. It's a peice of oil paper.\nPerfect for lighting the Latern.\n")
            winter_scene.haveOil=True
            print("With not much else there to do you leave the house.\n")
            winter_scene.village_decision(traveler)
        

    # functions for the cave scene
    def cave_scene(traveler, firstTime):
        if firstTime:
            print("You walk up to the cave. The mouth of the cave is covered in ice and feels as a colder blast of air emits from it.\n")
        else:
            print("You walk towards tha cave ready for what will happen.\n")
        winter_scene.cave_decision(traveler)
        

    def cave_decision(traveler):
        print("What do you want to do:\n1 "+("*"if winter_scene.inspectedShipwreck else"-")+" Inspect Cave\n2 "+("*"if winter_scene.inspectedPort else"-")+" Enter Cave\n3 - Travel\n")
        decision=int( input("User: ") )
        if(decision==1):
            print("\nThe cave looked like a dark blue. It felt sharp, as if the ice on its was was reaching out to you.\n")
            winter_scene.cave_decision(traveler)
        elif(decision==2):
            print("\n") 
            if(winter_scene.obtainedLatern):
                winter_scene.final_scene(traveler)
            else:
                print("You try to enter the cave, 7 steps in and you are freezing to your core.\nWithout the latern, it is clear this will not work.\n")
        elif(decision==3):
            print("\n")
            winter_scene.travelTo(traveler, 'c')
        else:
            print("\nSadly you can't do that\n")
            winter_scene.cave_decision(traveler)

    def final_scene(traveler):
        print()
        if not winter_scene.enteredCave:
            winter_scene.enteredCave=True
            print("As you enter the cave with the latern in hand, you feel the wind around you grow stronger and sharper.\nAs you continue down the cave you hear a sharp hissing. You look up to see a Ice Hydra. Each head spewing what look like thousands of small ice particles.\nThe ground around it shinned like pure glass, this beast stands in your way.\nYou ready your weapon.\n")
        else:
            print("You enter the cave ready to finish off what you had started. Hopefully you brought your sword.\n")

        winter_scene.enemy_fight(traveler,"Ice Hydra",50)

        print("You continue on your journy, over joyed from your successful battle and excited for what happens next.\n")
