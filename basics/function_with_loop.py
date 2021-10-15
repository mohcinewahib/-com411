def cross_bridge(distance):
    i = 0
    while distance > i:
        print("Crossed step")
        i +=1
if distance > 5:
    print("The bridge is collapsing!")
else:
    print("we must keep going!")
cross_bridge(3)
cross_bridge(6)