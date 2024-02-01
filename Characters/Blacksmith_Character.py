from Characters.Story_Character import StoryCharacter

class Blacksmith_Character(StoryCharacter):
    BSQ1, BSQ2, BSQ3, BSQ4 = False, False, False, False # blacksmith quesion
    lCrafter = False
    def __init__(self, name):
        super().__init__(name)
        
    def Blacksmith_dialogue(self, traveler, haveOre, haveSand, haveOil, tookCoin):
        print("You walk over to the Blacksmith. They put their hammer down and say,\nWhat do you want to know?")

        decision=""
        while decision != 5:
            print("What do you want to ask:\n1 "+("*"if Blacksmith_Character.BSQ1 else"-")+" Who are you?\n2 "+("*"if Blacksmith_Character.BSQ2 else"-")+" What is this place?\n3 "+("*"if Blacksmith_Character.BSQ3 else"-")+" Is it always this cold?\n4 "+("*"if Blacksmith_Character.BSQ4 else"-")+" May you craft me the latern?\n5 - Leave\n")
            decision=int( input("User: ") )
            if(decision==1):
                Blacksmith_Character.BSQ1 = True
                print("\nI am a blacksmith. Used to work for a village, however, I'm about all that's left.\nNow I work here just to hone my craft. It's simple but plesant work.\n")
            elif(decision==2):
                Blacksmith_Character.BSQ2 = True
                print("\nThis place is my home. I was just a bit west from here and remember playing a kid here and on the lake.\nNow this hut is the last safe heaven in the area.\n")
            elif(decision==3):
                Blacksmith_Character.BSQ3 = True
                print("\nNo. This all started once that time wizard took power. Everything you see here was once a flourishing town with bolstering crops.\nAll of it was slowly wilted away once the snow arrived.\n")
            elif(decision==4):
                if(haveOre and haveSand and haveOil):
                    if(tookCoin):
                        print("\nSure the Blacksmith said, he gets to crafting. Heating up the ore and blowing the glass.\nOnce it's complete he begrudingly hands you the latern and says,\nDo it for those for those who already fell.\n")
                    else:
                        print("\nGladly the Blacksmith said, he gets to crafting. Heating up the ore and blowing the glass.\nOnce it's complete he places in in your hads and says,\nThank you "+(traveler.name)+" and good luck!\n")
                    Blacksmith_Character.lCrafter=True
                else:
                    print("\nI will make it for you once you have the materials for it.\n")
            elif(decision==5):
                print("\nBye\n")
            else:
                print("\nSadly you can't do that\n")
            
    def get_latern_status():
        return Blacksmith_Character.lCrafter