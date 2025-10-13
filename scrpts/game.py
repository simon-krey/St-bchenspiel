stäbeLeft = 0

def game(StäbeNehmen, startingStäbe=None, startingPlayer=None):

    global stäbeLeft
    if startingStäbe:
        stäbeLeft=startingStäbe
    print(f"Stäbe: {stäbeLeft}")

    def chooseAlgorithm(stäbeLeft):
        StäbeNehmen = (stäbeLeft-1)%4

        print(StäbeNehmen)
        return StäbeNehmen
    
    if(startingPlayer):
        chooseAlgorithm(stäbeLeft)
        
    StäbeNehmen