# the GUI for the final project in CS120-02 Fall 2019
# the game is subhunt
from graphics import *

class GUI:
   def __init__(self):
      # the window
      # open a window (1200x800 max) use autoflush=False
      # (You may modify the next line)
      self.win = win = GraphWin("Submarine Hunt - CS120 Fall 2019",1000,600,autoflush=False)
      win.setCoords(0,0,10,10)

      # instructions,score,time Texts
      # three to five text objects for score, time and insTructions
      # inital message should be "Click to Begin Game"
      
      # create lanes
      # horizontal stripes below the water line to deliniate the sub "lanes"
      stripe1=Rectangle(Point(0,0), Point(10,1))
      stripe1.setFill("dark blue")
      stripe1.setOutline("dark blue")
      stripe1.draw(win)

      stripe2=Rectangle(Point(0,1), Point(10,2))
      stripe2.setFill("#324AB2")
      stripe2.setOutline("#324AB2")
      stripe2.draw(win)

      stripe3=Rectangle(Point(0,2), Point(10,3))
      stripe3.setFill("#1164B4")
      stripe3.setOutline("#1164B4")
      stripe3.draw(win)
      
      stripe4=Rectangle(Point(0,3), Point(10,4))
      stripe4.setFill("#1974D2")
      stripe4.setOutline("#1974D2")
      stripe4.draw(win)

      stripe5=Rectangle(Point(0,4), Point(10,5))
      stripe5.setFill("#1CA9C9")
      stripe5.setOutline("#1CA9C9")
      stripe5.draw(win)

      stripe6=Rectangle(Point(0,5), Point(10,6))
      stripe6.setFill("#80DAEB")
      stripe6.setOutline("#80DAEB")
      stripe6.draw(win)

      stripe7=Rectangle(Point(0,6), Point(10,10))
      stripe7.setFill("white")
      stripe7.setOutline("white")
      stripe7.draw(win)

      self.Title = Text(Point(4.5,9.5),"Submarine Hunt")
      self.Message1 = Text(Point(4.5,8.5),"Click to Begin Game")
      self.Message2 = Text(Point(1.5,8.5),"Score: 0")
      self.Message3 = Text(Point(8,8.5),"Time Remaining: 0")
      self.Title.setStyle("bold")
      for x in [self.Message1,self.Message2,self.Message3,self.Title]:
         x.setSize(20)
         x.setFill("black")
         x.draw(win)
      
   # thicker line to delineate the water line/horizon
      stripe8=Rectangle(Point(0,6), Point(10,6.1))
      stripe8.setFill("white")
      stripe8.setOutline("white")
      stripe8.draw(win)


      update() # draw all your stuff
      win.getMouse() # begin game
      self.Message1.setText("Use arrow keys to move, 'p' to pause\n'q' to quit, space to shoot.")
      self.Message1.setSize(14)
      update()

   def close(self):
      # end gracefully
      self.Message1.setText("Game over\nClick to close")
      self.win.getMouse()
      self.win.close()

  


   def updateScore(self,score):
      # update the on-screen score
      self.Message2.setText("Score: "+str(score))
      

   def updateTimer(self,time):
      # update on-screen timer 
      self.Message3.setText("Time Remaining: {0:0.2f}".format(abs(time)))

   def pause(self):
      self.Message1.setText("Game is Paused\nPress a key to resume")
      self.win.getKey()
      self.Message1.setText("Use arrow keys to move, 'p' to pause\n'q' to quit, space to shoot.")
      
   
if __name__=="__main__":
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
