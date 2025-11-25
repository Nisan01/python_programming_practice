
from withoutbg import WithoutBG

clcoding=WithoutBG.opensource()
result=clcoding.remove_background("_programs/hiding.JPG")
result.save("output.png")

