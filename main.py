import sys

import engine
import game

from engine import *
from game import *

def main(argc, argv):
    engine.init()
    game.init()

    #level.load("test.png")

    engine.run(GAME_NAME)
    
    #game.shutdown()
    engine.shutdown()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
