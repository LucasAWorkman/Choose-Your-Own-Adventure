playing = True
def getgame():
    return {
        "start": ["You are on your spacecraft when an alarm starts going off.", "1) Check the alarm", "check", "2) continue to your destination", "fly"],
        "check": ["You find out the glass in the cockpit is about to break. What will you do?", "1) Emergency land", "land", "2) continue to your destination", "continue"],
        "fly": ["The glass broke, making a vacuum that sucked you into space. Game over.", "1) Start over", "start", "2) Quit", "quit"],
        "land": ["You land on the nearest planet Agros. What will you do first?", "1) Repair ship", "repair", "2) Find help", "help"],
        "continue": ["You run out of fuel and get stranded in space. Game over.", "1) Start over", "start", "2) Quit", "quit"],
        "repair": ["You try to repair the ship by looking at the manual, but the glass shatters in your face, killing you. Game over.", "1) Start over", "start", "2) Quit", "quit"],
        "help": ["A local bar was close to your landing site, and you walk in. What will you do now?", "1) Ask the locals for a mechanic", "ask", "2) Sit down for a drink", "drink"],
        "ask": ["After asking, you found there were two mechanics in the bar. Which one will you ask for help?", "1) Arneed", "arneed", "2) Micha", "micha"],
        "drink": ["You had fun but get back on track. What will you do now?", "1) Steal a ship", "ship", "2) Call your friends", "friends"],
        "arneed": ["Arneed tricks you and kills you. Game over.", "1) Start over", "start", "2) Quit", "quit"],
        "micha": ["Micah is the best mechanic on the planet and fixes your ship. You won!", "1) Start over", "start", "2) Quit", "quit"],
        "ship": ["You overheard a drunk space pilot talking about his military base. What will you do?", "1) Steal his plane keys", "keys", "2) Go to the military base", "base"],
        "friends": ["You use your signal transmitter to call your friends, and they rescue you. You win!", "1) Start over", "start", "2) Quit", "quit"],
        "base": ["You find the base. Which way do you try to enter?", "1) Front entrance", "front", "2) Climb the side gate", "gate"],
        "front": ["The front gate was heavily guarded! You got caught.", "1) Start over", "start", "2) Quit", "quit"],
        "gate": ["Climbing the gate was perfect. Nobody saw you, but what now?", "1) Go into the front hangar", "hangarfront", "2) Go into the back hangar", "hangarback"],
        "hangarfront": ["Nobody was inside the hangar, and you find a spacecraft which you take off in. You won!", "1) Start over", "start", "2) Quit", "quit"],
        "hangarback": ["This hangar had several guards in it which kill you. You lose!", "1) Start over", "start", "2) Quit", "quit"]
    }


def playNode(node):
    dict = getgame()
    dict_info = dict[node]
    
    Desc = dict_info[0]
    MenuA = dict_info[1]
    NodeA = dict_info[2]
    MenuB = dict_info[3]
    NodeB = dict_info[4]

    print(Desc)
    print(MenuA)
    print(MenuB)

    next_choice = int(input("Your Choice: "))

    if next_choice == 1:
        return NodeA
    if next_choice == 2:
        return NodeB
    else:
        print("select choice 1 or 2")
        return node
def main():
    playernode = "start"
    global playing
    while playing:
       playernode = playNode(playernode)
       if playernode == "quit":
           playing = False
           return playing

main()



