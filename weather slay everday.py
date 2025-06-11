weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in range(0,7):
        if(weather[i]==0):
                rainy+=1
        else:
                sunny+=1

if(sunny>rainy):
        print("Boy, you lucky ducky mucky lucky but also yucky musty echy micky.")
else:
        print("Where do you have a life beacause your weather is BAD! You unlucky ducky mucky lusty chusty guoompy looumpy boompy doompy humpohy koolcky unlucky bro.")