from graphics import *

def main():
    win = GraphWin("My Graphic's window", 500, 500)
    
    #Sky 
    skyPoint1 = Point(500, 300)
    skyPoint2 = Point(0, 0)
    sky = Rectangle(skyPoint1, skyPoint2)  
    sky.setFill("pink")
    sky.setOutline("turquoise")
    sky.setWidth(2)
    sky.draw(win)
    
    #Sun
    center = Point(250, 300)
    sun = Circle(center, 50)  
    sun.setFill("orange")  
    sun.setOutline("red")
    sun.setWidth(2)
    sun.draw(win)
    
    #Beach
    beachPoint1 = Point(500, 500)
    beachPoint2 = Point(0, 400)   
    beach = Rectangle(beachPoint1, beachPoint2)
    beach.setFill("tan")
    beach.setOutline("black")
    beach.setWidth(2)
    beach.draw(win)
    
    #Ocean
    oceanPoint1 = Point(500, 300)
    oceanPoint2 = Point(0, 400)
    ocean = Rectangle(oceanPoint1, oceanPoint2)   
    ocean.setFill("blue")
    ocean.setOutline("turquoise")
    ocean.setWidth(2)
    ocean.draw(win)

    #Light
    lightPoint1 = Point(300, 300)
    lightPoint2 = Point(200, 400)
    light = Rectangle(lightPoint1, lightPoint2)
    light.setFill("yellow")
    light.setOutline("orange")
    light.setWidth(2)
    light.draw(win)

    #Cloud One
    cloudOnePoint1 = Point(200, 100)
    cloudOnePoint2 = Point(100, 130)
    cloudOne = Rectangle(cloudOnePoint1, cloudOnePoint2) 
    cloudOne.setFill("white")
    cloudOne.setOutline("black")
    cloudOne.setWidth(2)
    cloudOne.draw(win)
    
    #Cloud Two
    cloudTwoPoint1 = Point(120, 140)
    cloudTwoPoint2 = Point(20, 110)
    cloudTwo = Rectangle(cloudTwoPoint1, cloudTwoPoint2) 
    cloudTwo.setFill("white")
    cloudTwo.setOutline("black")
    cloudTwo.setWidth(2)
    cloudTwo.draw(win)
    
    #Cloud Three
    cloudThreePoint1 = Point(300, 140)
    cloudThreePoint2 = Point(400, 110)
    cloudThree = Rectangle(cloudThreePoint1, cloudThreePoint2) 
    cloudThree.setFill("white")
    cloudThree.setOutline("black")
    cloudThree.setWidth(2)
    cloudThree.draw(win)
    
    #Cloud Four
    cloudFourPoint1 = Point(400, 80)
    cloudFourPoint2 = Point(475, 50)
    cloudFour = Rectangle(cloudFourPoint1, cloudFourPoint2) 
    cloudFour.setFill("white")
    cloudFour.setOutline("black")
    cloudFour.setWidth(2)
    cloudFour.draw(win)
    
    #Cloud Five
    cloudFivePoint1 = Point(250, 80)
    cloudFivePoint2 = Point(350, 50)
    cloudFive = Rectangle(cloudFivePoint1, cloudFivePoint2)
    cloudFive.setFill("white")
    cloudFive.setOutline("black")
    cloudFive.setWidth(2)
    cloudFive.draw(win)
    
    #Boat Base
    boatBasePoint1 = Point(30,300)
    boatBasePoint2 = Point(60, 290)  
    boatBase = Rectangle(boatBasePoint1, boatBasePoint2)  
    boatBase.setFill("brown")
    boatBase.setOutline("black")
    boatBase.setWidth(3)
    boatBase.draw(win)
    
    #Boat Post
    boatPostPoint1 = Point(40,280)
    boatPostPoint2 = Point(41, 290)
    boatPost = Rectangle(boatPostPoint1, boatPostPoint2)  
    boatPost.setFill("brown")
    boatPost.setOutline("black")
    boatPost.setWidth(3)
    boatPost.draw(win)
    
    #Boat Sail
    boatSailPoint1 = Point(35,270)
    boatSailPoint2 = Point(45, 280)
    boatSail = Rectangle(boatSailPoint1, boatSailPoint2)   
    boatSail.setFill("white")
    boatSail.setOutline("black")
    boatSail.setWidth(3)
    boatSail.draw(win)
    
main()
