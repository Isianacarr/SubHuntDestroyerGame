# sub manager
# the submanager is the liaison between the various subs and the game engine 
from submarine import Submarine
from random import random
from graphics import *

class SubManager:
   def __init__(self,win):
      # remember the window for later
      self.win = win
      self.makeProb = .0125
      
      
      # make lanes empty
      self.lanes = [None]*6

   # make the subs and undraw them if they move off screen   
   def moveSubs(self,timeStep):
      for i in range(len(self.lanes)):
         y = i
         if self.lanes[i] == None:
           if random()< self.makeProb:
              self.lanes[i] = Submarine(y,self.win)
         elif self.lanes[i].offscreen() == True:
            self.lanes[i].undraw()
            self.lanes[i] = None
         else:
            self.lanes[i].move(timeStep)
   #Check if there is a sub in the lane, check hita undraw if both are true
   def checkHits(self, d):
      hits = 0
      for i in range(len(self.lanes)):
         if self.lanes[i] is not None and self.lanes[i].checkHit(d):
            self.lanes[i].undraw()
            self.lanes[i] = None
            hits += 1

      return hits

   
   
            

      
      
if __name__=="__main__":
   from subhuntGUI import GUI
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
