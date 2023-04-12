winner = 'placeholder'

def result(elementP1, elementP2):
    global resultText, winner
    if elementP1 == elementP2:
        resultText = "Égalité"
        winner = 'None'
    if elementP1 == 1:
        if elementP2 == 2:
            #P1 win
            resultText = 'La feuille recouvre la pierre'
            winner = 'P1'
        elif elementP2 == 3:
            #P2 win
            resultText = 'Les ciseaux coupent la feuille'
            winner = 'P2'
        #BBT
        if elementP2 == 4:
            #P2 win
            resultText = 'Le lézard mange la feuille'
            winner = 'P2'
        if elementP2 == 5:
            #P1 win
            resultText = 'La feuille discrédite Spock'
            winner = 'P1'
    if elementP1 == 2:
        if elementP2 == 1:
            #P2 win
            resultText = 'La feuille recouvre la pierre'
            winner = 'P2'
        elif elementP2 == 3:
            #P1 win
            resultText = 'La pierre émousse les ciseaux'
            winner = 'P1'
        #BBT
        if elementP2 == 4:
            #P1 win
            resultText = 'La pierre écrase le lézard'
            winner = 'P1'
        if elementP2 == 5:
            #P2 win
            resultText = 'Spock vaporise la pierre'
            winner = 'P2'
    if elementP1 == 3:
        if elementP2 == 1:
            #P1 win
            resultText = 'Les ciseaux coupent la feuille'
            winner = 'P1'
        if elementP2 == 2:
            #P2 win
            resultText = 'La pierre émousse les ciseaux'
            winner = 'P2'
        #BBT
        if elementP2 == 4:
            #P1 win
            resultText = 'Les ciseaux décapitent le lézard'
            winner = 'P1'
        if elementP2 == 5:
            #P2 win
            resultText = 'Spock casse les ciseaux'
            winner = 'P2'
    #BBT
    if elementP1 == 4:
        if elementP2 == 1:
            #P1 win
            resultText = 'Le lézard mange la feuille'
            winner = 'P1'
        if elementP2 == 2:
            #P2 win
            resultText = 'La pierre écrase le lézard'
            winner = 'P2'
        if elementP2 == 3:
            #P2 win
            resultText = 'Les ciseaux décapitent le lézard'
            winner = 'P2'
        if elementP2 == 5:
            #P1 win
            resultText = 'Le lézard empoisonne Spock'
            winner = 'P1'
    if elementP1 == 5:
        if elementP2 == 1:
            #P2 win
            resultText = 'La feuille discrédite Spock'
            winner = 'P2'
        if elementP2 == 2:
            #P1 win
            resultText = 'Spock vaporise la pierre'
            winner = 'P1'
        if elementP2 == 3:
            #P1 win
            resultText = 'Spock casse les ciseaux'
            winner = 'P1'
        if elementP2 == 4:
            #P2 win
            resultText = 'Le lézard empoisonne Spock'
            winner = 'P2'


def resultRetrieve():
    return[resultText, winner]