 # subhunt game
from graphics import *
from destroyer import Destroyer
from submanager import SubManager
from random import *
from depthcharge import *


class Game:
   #Draw the destroyer the sub and the charge
   def __init__(self,gui):
      self.gui = gui
      self.destroyer = Destroyer(gui.win)
      self.manager = SubManager(gui.win)
      self.charge = []
   #See if the sub and the charge Hit
   #Undraw charge and remove if hit
   def checkHits(self):
      hits = 0
      for i in range(len(self.charge)):
         hit = self.manager.checkHits(self.charge[i])
         hits += hit
         self.charge[i] = self.charge[i].explode()
            
      if None in self.charge:
         self.charge.remove(None)

      return hits
   
         
   #Buttons    
   def checkKeyBoard(self):
   
      ch = self.gui.win.checkKey()
      
      if ch == 'Left':
         self.destroyer.moveLeft()
      elif ch == 'Right':
         self.destroyer.moveRight()
      elif ch == 'p':
         self.gui.pause()   
      elif ch == 'q':
         self.done=True
      elif  ch == 'space' and len(self.charge) < 5:
         self.charge.append(DepthCharge(self.destroyer.getCenter(), self.gui.win))
         
      
      
   def play(self):
      self.done=False
      #self.pause=False
      
      fps = 30            # frames per second
      timeRemaining = 60  # seconds in game
      score = 0           # initial score

      #  MAIN EVENT LOOP, everything happens from here
      score = 0
      while timeRemaining >= 0:
         
         #Update score based on hits
         score += self.checkHits() * 100

         self.gui.updateScore(score)

         # update the time remaining
         timeRemaining -= 1/fps
         self.gui.updateTimer(timeRemaining)
         
         # update screen and control loop speed
         #End gracefully
         
         #Move the subs
         self.manager.moveSubs(1/fps)

         #Remove charge if Past Bottom
         for i in range(len(self.charge)):
            self.charge[i].move(1/fps)
            if self.charge[i].pastBottom():
               self.charge[i].undraw()
               self.charge[i] = None
         if None in self.charge:
            self.charge.remove(None)

         self.checkKeyBoard()
         if self.done:
            self.gui.close()
            break
         
         update(fps)

      self.gui.close()

     
      
     

      



if __name__=="__main__":
   from subhuntGUI import GUI
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
