v = float(input("Uma distancia em metros: "))

km = v/1000
hm = v/100
dam = v/10
dm = v*10
cm = v*100
mm = v*1000

print("A medida de {} corresponde a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm" .format(v, km, hm, dam, dm, cm, mm))