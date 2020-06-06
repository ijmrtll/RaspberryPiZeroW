from SimpleCV import Image, DrawingLayer, Color
from time import sleep

#open the image
raspberryImage = Image("raspberry.jpg")

#creates the layer to draw on
myDrawingLayer = DrawingLayer((raspberryImage.width, raspberryImage.height))

#drawings
myDrawingLayer.rectangle((50,20),(250,60),filled=True)
myDrawingLayer.setFontSize(45)
myDrawingLayer.text("Raspberry!", (50,20),color=Color.WHITE)

#overlay
raspberryImage.addDrawingLayer(myDrawingLayer)
raspberryImage.applyLayers()

#save
raspberryImage.save("raspberry-tittled.jpg")
