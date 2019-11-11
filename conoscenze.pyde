def setup():
    size(420, 620)
    
def draw():
    global i,j,bravo
    
    background(255)
    frameRate(60)
    fill(0)
    noStroke()
    
    pushMatrix()
    translate (30,20)
            
    for i in range(0, 400, 70):
        for j in range(0, 200, 70):
            fill(0)
            bravo = 0.02
            ruotami()
            
    for i in range(0, 70, 70):
        for j in range (210, 280, 70):
            fill(0)
            ruotami()
            
    for i in range(0, 280, 70):
        for j in range(280, 350, 70):
            fill(60,0,0)
            bravo = 0.04
            ruotami()
            
    for i in range(0, 140, 70):
        for j in range(350, 420, 70):
            fill(120,0,0)
            bravo = 0.06
            ruotami()
            
    for i in range(0, 70, 70):
        for j in range(420, 490, 70):
            fill(180,0,0)
            bravo = 0.08
            ruotami()
            
    for i in range(0, 70, 70):
        for j in range(490, 560, 70):
            fill(240)
            bravo = 0
            ruotami()
    
    popMatrix()
    fill(0)
    textSize(14)
    textAlign(CENTER)
    text("\"Da 1 a 5 come valuti la tua conoscenza di Processing?\"", width/2, height-10)
    
    x = 30
    y = 0
    for i in range(0, 5, 1):
        
        fill(y, 0, 0)
        rect(x, 570, 20, 20)
        text(i+1, x+20, 575)
        x += 80
        y += 60
    
    ###if frameCount < 200 and frameCount % 40 == 0:
        ###saveFrame()
            
            

def ruotami():
    global i,j,bravo
    
    pushMatrix()
    rectMode(CENTER)
    translate(i, j)
    rotate(frameCount * bravo)
    gear()
    popMatrix()
    
    
def gear():
    ellipse(0, 0, 20, 20)
    pushMatrix()
    for a in range(3):
        translate(0, 0)
        rotate(PI/3)
        rect(0, 0, 28, 6)
    popMatrix()
    fill(255)
    ellipse(0, 0, 8, 8)
