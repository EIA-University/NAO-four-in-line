import getImagePhoto as take
import sendText as talk
import convertirImgToMatrix as conv
import time
from naoqi import ALProxy
import Fourinline as games
#desktop-keel9jm.local.:54103
#nao.local 9559
if __name__ == '__main__':
    IP = "nao.local"  # Replace here with your NaoQi's IP address.
    PORT = 9559
    
    while True:
        path = take.sinNAO(IP, PORT)
        #print path
        matrix = conv.ejecutar(path)
        print matrix
        if matrix != False:
            jugada = games.play(matrix)
            talk.talkSinNAO("I am going to play in the colum:" + jugada, IP, PORT)
            talk.talkSinNAO("It is your turn", IP, PORT)
            time.sleep(10)
        else:
            talk.talkSinNAO("I can't see right the game", IP, PORT)
            time.sleep(10)
    
    
    
