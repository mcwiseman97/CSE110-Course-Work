"""
Author: Michael Wiseman
Assignment: Project - Adventure Game
Date: 1/9/26
"""

"""
Requirements
*1. At leaste 3 levels of scenarios with possible options
*2. Use nested if statements ( I dont know what the instructions mean here)
*3. At leaste one scene should must have two or more possible choices4. Any time there is a choice to be made, the "choice" should be written in caps. ex. MATCHES
*5. Answers must be strings and not numbers
*6. Answers should not be case sensative
*7. Differant choices should lead the player down differant scenarios
*8. No other answers should be accessable than the ones presented in the current scene
*9. every question should have an else statement to catch answers that ar not listed as possible choices
"""

print("Alien Invasion")
print("by: Michael Wiseman")
print()
print("It is January of 2026, static on the TV turns to an emergency broadcast.")
print("It reads, 'THIS IS NOT A TEST! ALIENS HAVE TOUCHED EARTH AND HAVE COME TO DESTROY! DO WHATEVER IT TAKES TO STAY ALIVE!'")
print("You can either run or shelter in place.")
print()
choice = input("Do you wish to RUN or SHELTER?: ").lower()
print()
# SCENE ONE
while True:
    if choice == "run" or choice == "shelter":
        if choice == "run":
            print()
            print("The front door is just 10 feet away. You run full speed grasping for the handle and yank it open. While standing")
            print("in the yard, you see Aliens off in the distance. Your car is parked in the driveway. A creek entrance leads")
            print("behind your house.")
            print()
            choice = input("Do you wish to enter your CAR or flee to the CREEK?: ").lower()
            while True:
                if choice == "car" or choice == "creek":
                    if choice == "car":
                        print()
                        print("Quicky, you hop into your car. Your keys frenticly searching for the key slot. You see a large shadow")
                        print("cast over the hood of your car. Through your sunroof, massive alien spacecraft encrouch on your location.")
                        print("Where can you go now? Drive to military base or to the unknown.")
                        print()
                        choice = input("You can choose BASE or UNKNOWN.").lower()
                        while True:
                            if choice == "base" or choice == "unknown":
                                if choice == "base":
                                    print()
                                    print("You get to the army base. Thousands of cars make a massive line. All with the same intent of entering the base")
                                    print("for protection. One by one, car start lifting. Massive ships with tenticle like appendages and claws at the end.")
                                    print("Your hear a crunch and feel a jolt. You car has now been taken with you in it. Instantainiusly you are beemed into")
                                    print("space. Carnage, distruction, and death are not what you see. A planet like ours but full of activity and life greet")
                                    print("you. Over a masive speaker you here a voice in your own language. It invites you to a glactic party. A celebration")
                                    print(" to welcome us to live with them in cohabitation of their planet. (Turns out the invsasion, while real, was not a")
                                    print("hostile take over persay. It was humanity itself that cause the distruction and chaos.)")
                                    print()
                                    print("THE END!")
                                    break
                                else:
                                    print()
                                    print("Your drove until you hit empty on gas. Farmland as far as the eyes can see. Out here, there is not commotion.")
                                    print("Actually, there is no one at all. No cars, bikes, people, or ALIENS. THe ALIENS had alread passed through and this")
                                    print("land was now open and available for occupancy. Days, weeks, and months passed and no sign of humanity or aliens.")
                                    print("You are the last person on earth. You live out you remaining day living off the land you had settle in. No desire to")
                                    print("find remanant of a past life. Farm life was all you desired at this point.")
                                    print()
                                    print("THE END!")
                                    break
                            else:
                                print()
                                print("The time provided is invalid. Please try again.")
                                choice = input("You can choose BASE or UNKNOWN.").lower()
                                break
                    else:
                        print()
                        print("The creek stretches for miles in either direction. Trails like the curve of the creek. Trees are the only")
                        print("coverage you have, but they are far and dew in-between. Their are hills to the right and an ocean to the left.")
                        print("You take the risk of staying on the creek, but where to now?")
                        print()
                        choice = input("To the HILLS or the OCEAN?:").lower()
                        while True:
                            if choice == "hills" or choice == "ocean":
                                if choice == "hills":
                                    print()
                                    print("From the highest hills you overlook the chaos that is underway in the cities blow. You see space craft beeming people")
                                    print("up on mass. Lines forming below, where aliens create single filed groups of people being taken from their homes. You")
                                    print("watch in aw. Screaming and crying echo through the hills with an eary screech. A sigh of relief rolls over you as you")
                                    print("assume your safety is garenteed. When things become to hard to bare watching below, you turn to go down the hill side")
                                    print("for protection in the valley below. Unexpectedly, an alien stand there ready to take you in. You didnt make it, and too")
                                    print("joined the rest being beemed up into the space craft. Each person is greeted by the head of the spacecraft wehere they")
                                    print("are assigned meaningless tasks that make you burn enery, as that what the ships run off of.")
                                    print()
                                    print("THE END!")
                                    break
                                else:
                                    print()
                                    print("The sound of the wave crashing on the beach and feeling of wind blowing through your hair. You cant help but find peace")
                                    print("amongs the chaos. The sounds of people, cars, and distruction are now just white noise. A jetski lay alone in the distance.")
                                    print("You hop on and take off into the sunset. Three minutes in, you crash. We random wall painted to look like the horizeon of a")
                                    print("ocean.. Mirrors line the bottom to mimic the waves, and a light blue wall arching into an incredibly large dome shape. The aliens")
                                    print("must have place this down to fool the puplic. As a last effort to escape you dive into the water to find that the dome does")
                                    print("not go all the way down. Before you could resurface on the other end, a shark ate you.")
                                    print()
                                    print("THE END!")
                                    break
                            else:
                                print()
                                print("The time provided is invalid. Please try again.")
                                choice = input("You can choose HILL or OCEAN.").lower()
                                break                        
                        break
                else:
                    print()
                    print("The time provided is invalid. Please try again.")
                    choice = input("You can choose CAR or CREEK.").lower()
            break
        else:
            print()
            print("Your mind races to think of the safest place in the house. From outside, you hear spacecraft landing in your cul de sac.")
            print("You only have so much time before they enter your home. The attic could work as well secret room behind the bookshelf.")
            print()
            choice = input("Will you choose ATTIC or ROOM?: ").lower()

            while True:
                if choice == "attic" or choice == "room":
                    if choice == "attic":
                        print()
                        print("In the middle of the hallway, a string hangs from the ceiling. Pulling it draws down a ladder to the attic.")
                        print("A puff of dust and insullation blow into your face, Temperarily putting you in a coughing fit. Immediately, you")
                        print("hear pounding at the front door. Windows shattering. As fast as possible, you make it up the ladder, closing")
                        print("the attic behind you. Pitch black, you whip out your phones flash light to see only insulation and one plywood sheet.")
                        print("Sitting in the open or hidng behind the plywood seem to be the only options.")
                        print()
                        choice = input("Will you choose to sit in the OPEN or hide behind the PLYWOOD?: ").lower()
                        while True:
                            if choice == "open" or choice == "plywood":
                                if choice == "open":
                                    print()
                                    print("While stting in the open, you couldnt help but notice the sound of alients, doors or windows had all come to and end.")
                                    print("You decide to lower the ladder. Just as you suspected, no aliens were in sight. More estonishing is the doors and windows")
                                    print("were not broken. Everything was as it were before the invasion occured. Yoou decided to get some fresh air after all panic")
                                    print("and worry were over. It is then that you relaized you home in not your home. The town you grew up in was not there either.")
                                    print("You run around trying to make sense of what is going on, when in the distance you hear a noise. That noise seemed to be")
                                    print("familair. It echod through the streets, getting louder and louder. That is when you woke up from you nightmare. Sweat")
                                    print("dripping from your face and heart racing. A sigh of releaf and and a little chuckle were all you could muster.")
                                    print()
                                    print("THE END!")
                                    break
                                else:
                                    print()
                                    print("Crouched behind the plywood, a light bean to show forom around side. The roof has disapeared, and you feel more exposed than")
                                    print("ever. One by one, each component of the house began to vanish until the very ceiling you where perched on dropped and you")
                                    print("began to fall 9 feet down. A sharp pain run from your heal to you mid shin. That is when you, yourself dissappeared. You find")
                                    print("yourself in a void, bodyless. The only thing present was your conceousness.")
                                    print()
                                    print("THE END!")
                                    break
                            else:
                                print()
                                print("The time provided is invalid. Please try again.")
                                choice = input("You can choose OPEN or PLYWOOD.").lower()
                                break
                        break
                    else:
                        print()
                        print("You pull a book out from the random bookshelf in the livingroom. Slowly the bookshelf start moving, seeminly into the wall.")
                        print("An opening presents itself. Just as it opened, it then closes behind you Walking around the room you notice a hollow sound") 
                        print("under the run inm the middle of the room. The rest of the room is well decorated. A huge table sits at one end of the room,")
                        print("while a couch is on the either. You investigate while there is a hollow sound under the rug. A hidden pannel that is connected")
                        print("to a stair case downward.")
                        print()
                        choice = input("Do you wish to STAY in the room or EXPLORE the staircase: ").lower()
                        while True:
                            if choice == "stay" or choice == "explore":
                                if choice == "stay":
                                    print("")
                                    print("As you sit on the couch, you cant help but wonder how long you will have to be in this room. It comfortable enought")
                                    print("to stay a while. This room was meant for instances where you needed to hide. Food, clean water, and other necessities")
                                    print("are at your disposal. But nothing prepared you for what was next. All power to the house was cut. The one thing you failed")
                                    print("to prapare with was a backup genorator or solar power. You find yourself trapped by your own sesign. No way in or out but")
                                    print("by way of the hidden underground staircase. However, the staircase was never meant to take you anywhere. You built it")
                                    print("too as a trap, inspired by the Winchester masion. Stairs and doors to nothing, windows that look only at a wall. Any and")
                                    print("Who sought to get you would be stuck for as long as they lived. Now you find yourself in your own trap.")
                                    print()
                                    print("THE END!")
                                    break
                                else:
                                    print()
                                    print("The hidden staircase is illuminated by lights that follow the stairs all the way down. The stairs went down forever. Only")
                                    print("after 20 minutes of going down did there begin to be a sign of something new. The stairs turned into a a bunker. A bunker you")
                                    print("seemingly forgot about making. Inside was a lab, kitchen, a study, and several other rooms. You explored the rooms one by one")
                                    print("until you got to the ende of the hollway. A massive double door sat weiting to be opened. When opened, you are greeted with a")
                                    print("control panel that have many lights flickering at any given time. Past the panel, a large glass wall overlooks a cilendrical")
                                    print("void. When right infront of it, you begin to see a point of a rocket poking up. An aw-ha moment hits as you realized you built")
                                    print("this station prior to a major accident leaving some of your memory wiped. Needles to say, you launched yourself into space and")
                                    print("navigated yourself to the nearest inhabitable plannet where you lived your last days.")
                                    print()
                                    print("THE END!")
                                    break
                            else:
                                print()
                                print("The time provided is invalid. Please try again.")
                                choice = input("You can choose STAY or EXPLORE.").lower()
                                break
                        break
                else:
                    print()
                    print("The time provided is invalid. Please try again.")
                    choice = input("You can choose ATTIC or ROOM.").lower()
            break
    else:
        print()
        print("The time provided is invalid. Please try again.")
        choice = input("You can choose RUN or SHELTER.").lower()

print()
print("Thank you for playing!")