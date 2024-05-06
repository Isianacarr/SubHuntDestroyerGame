# submarine class
from graphics import *
from random import *
from depthcharge import *

   
class Submarine:
   def __init__(self,y,win):
      # remember a few window parameters
      self.rightEdge = win.width
      self.win=win
      self.lvelocity = random()* .5 + 1.5
      self.rvelocity = -1.5 - random()* .5
      self.velocity = 0
      b = choice([-1,11])
      x = b
      


      #set a velocity for sub
      if b == -1:
         self.velocity = self.lvelocity
         self.sub = Image(Point(x,y-.5),"subl.png")
         
      else:
         self.velocity = self.rvelocity
         self.sub = Image(Point(x,y-.5),"subr.png")
      
      self.sub.draw(win)
         

      
   #Move sub
   def move(self,timeStep):
         self.sub.move(timeStep*self.velocity,0)
   
   def undraw(self):
         self.sub.undraw()
   def offscreen(self):
      x = self.sub.getAnchor().getX()
      if self.velocity > 0 and x >10:
         return True
      elif self.velocity < 0 and x <0:
         return True
      else:
         return False

   #Get range of the sub   
   def interior(self, point):
      sX = self.sub.getAnchor().getX()
      sY = self.sub.getAnchor().getY()
      swRan = (self.sub.getWidth() / 2)/ 1000 * 10
      shRan = (self.sub.getHeight() / 2)/ 1000 * 10
      lPoint = sX - swRan
      tPoint = sY + shRan
      rPoint =  sX + swRan
      bPoint = sY - shRan
      x,y = point

      return lPoint <= x <= rPoint and bPoint <= y <= tPoint

   #Check if charge hit sub   
   def checkHit(self, d):
      for point in d.getRange():
         if self.interior(point):
            d.hit()
            return True
            
      return False

     
if __name__=="__main__":
   from subhuntGUI import GUI
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
