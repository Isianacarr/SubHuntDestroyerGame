# class for depth charges
# phase four will introduce depth charges
from graphics import *
from destroyer import Destroyer

class DepthCharge:
   # a depthcharge starts at the point given and falls at a constant rate.
   def __init__(self,center,win):
      # remember win
      self.win = win
      self.x = center.getX()
      self.y = 6.63
      #draw charge
      self.charge = Image(Point(self.x,self.y),"missile.png")
      self.charge.draw(win)
      # set velocity  
      self.velocity = -1.5
      self.exploded = False
      self.lagtime = 30
      
   def move(self,timeStep):
      # the depthcharge drops by timeStep*velocity
      self.charge.move(0, timeStep*self.velocity)

   #see if charge has moved off screen
   def pastBottom(self):
      if self.charge.getAnchor().getY() < 0:
         return True
   
   def undraw(self):
      self.charge.undraw()
      
   def getCenter(self):
      return self.charge.getAnchor()

   def getX(self):
      return self.charge.getAnchor().getX()

   def getY(self):
      return self.charge.getAnchor().getY()

   #Range of charge in GUI
   def getRange(self): 
      dX = self.charge.getAnchor().getX()
      dY = self.charge.getAnchor().getY()
      dRan = (self.charge.getWidth() / 2)/1000 * 10
      dhRan = (self.charge.getHeight() / 2)/1000 * 10
      lPoint = (dX - dRan, dY + dhRan)
      tPoint = (dX + dRan,dY + dhRan)
      rPoint = (dX + dRan, dY - dhRan)
      bPoint = (dX - dRan, dY - dhRan)

      return lPoint, tPoint, rPoint, bPoint

   def hit(self):
      self.exploded = True
   
   def explode(self):
      if self.exploded and self.lagtime == 30:
         self.charge.undraw()
         self.charge = Image(self.getCenter(), "explosion.png")
         self.velocity = 0
         self.charge.draw(self.win)
         self.lagtime -= 1
      elif self.exploded and self.lagtime > 0 :
         self.lagtime -= 1
      elif self.exploded:
         self.charge.undraw()
         return None
      
      return self

   

   
      
