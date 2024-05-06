# destroyer class
from graphics import *

 
# the water line for the destroyer is at y = 150 and it can
   
   
class Destroyer:
   def __init__(self,win):
      # set up some constants
      self.step = 20                             # pixels to move each move
      centerX = self.X = win.getWidth()/2
      self.win = win
      # center of window

      # draw a destroyer centered in window
      self.destroyers = [Image(Point(5,6.63), "boatflippedresized2.png"),
                         Image(Point(5,6.63), "boatresized2.png")]
      self.destroyer = 0
      #self.destroyer.flipboat()
      self.destroyers[self.destroyer].draw(win)

   def getCenter(self):
      return self.destroyers[self.destroyer].getAnchor()
         
   def moveLeft(self):
      # move destroyer one step left AND adjust centerX
      if self.destroyer == 1:
         self.destroyers[1].undraw()
         self.destroyers[0].draw(self.win)
      self.destroyer = 0
      dx = -.2
      for destroyer in self.destroyers:
         destroyer.move(dx, 0)
      
            
   def moveRight(self):
      # move destroyer one step right AND adjust centerX
      if self.destroyer == 0:
         self.destroyers[0].undraw()
         self.destroyers[1].draw(self.win)
      self.destroyer = 1
      dx= .2
      for destroyer in self.destroyers:
         destroyer.move(dx, 0)

   #def flipBoat(self):
    #  if dx < 0:
     #    self.destroyer = Image(Point(5,7.65), "boatflippedresized2.png")
      #else:
       #   self.destroyer = Image(Point(5,7.65), "boatflipped.png")
         
if __name__=="__main__":
   from subhuntGUI import GUI
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()

