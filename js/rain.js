//credits to random guy at stackoverflow
var ctx;
var imgBg;
var imgDrops;
var x = 0;
var y = 0;
var noOfDrops = 100;
var fallingDrops = [];


    function drawBackground(){  
        ctx.drawImage(imgBg, 0, 0); //Background
    }

    function draw() {
        drawBackground();
        
        for (var i=0; i< noOfDrops; i++)
        {
        ctx.drawImage (fallingDrops[i].image, fallingDrops[i].x, fallingDrops[i].y); //The rain drop

        fallingDrops[i].y += fallingDrops[i].speed; //Set the falling speed
        if (fallingDrops[i].y > 600) {  //Repeat the raindrop when it falls out of view
        fallingDrops[i].y = -15 //Account for the image size
        fallingDrops[i].x = Math.random() * 600;    //Make it appear randomly along the width    
        }
        
        }
    }

    function setup() {
        var canvas = document.getElementById('klausRegn');

        if (canvas.getContext) {
                ctx = canvas.getContext('2d');
            
                    imgBg = new Image();
            imgBg.src = "";
        setInterval(draw, 36);
        for (var i = 0; i < noOfDrops; i++) {
            var fallingDr = new Object();
            fallingDr["image"] =  new Image();
        fallingDr.image.src = 'http://www.klauswunderlich.de/_pictures/startIndex/Index_1_05.gif';
                
            fallingDr["x"] = Math.random() * 1200;
            fallingDr["y"] = Math.random() * 5;
            fallingDr["speed"] = 5 + Math.random() * 5;
            fallingDrops.push(fallingDr);
            }

        }
    }
setup();
