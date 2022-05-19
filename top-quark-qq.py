
import matplotlib.pyplot as plt
from feynman import Diagram

fig = plt.figure(figsize=(10.,10.))
ax = fig.add_axes([0,0,1,1], frameon=False)

diagram = Diagram(ax)
#diagram.text(.4,0.9,"Associated Vector Boson", fontsize=40)
#diagram.text(.6,0.83,"(VH or 'top2 Strahlung')", fontsize=40)
in1 = diagram.vertex(xy=(.05,.75), marker='')
in2= diagram.vertex(xy=(.05,.25), marker='')
v1 = diagram.vertex(xy=(.20,.5), marker='')
v2 = diagram.vertex(xy=(.50,.5), marker='')
t1 = diagram.vertex(xy=(.6,.65), marker='')
t2 = diagram.vertex(xy=(.6,.35), marker='')

w1 = diagram.vertex(xy=(.8,.75), marker='')
b1 = diagram.vertex(xy=(.8,.55), marker='')
w2 = diagram.vertex(xy=(.8,.25), marker='')
b2 = diagram.vertex(xy=(.8,.45), marker='')

q1 = diagram.line(in1, v1,arrow = False)
q2 = diagram.line(v1, in2,arrow = False)
g = diagram.line(v1, v2, style='loopy',nloops=7,yamp=0.02)
top1 = diagram.line(v2, t2,arrow = False)
top2 = diagram.line(t1,v2,arrow = False)
wb1 = diagram.line(w1,t1, style='wiggly',nwiggles=4, marker='')
bjet1 = diagram.line(t1, b1,arrow = False)
wb2 = diagram.line(t2, w2, style='wiggly',nwiggles=4, marker='')
bjet2 = diagram.line(b2,t2,arrow = False)

q1.text("q",t=0.5,y=-0.1,fontsize=30)
q2.text(r"$\bar{q}$",t=0.5,y=-0.1,fontsize=30)
g.text("g",t=0.5,y=0.1,fontsize=30)
top2.text("t",t=0.5,y=-0.1,fontsize=30)
top1.text(r"$\bar{\mathrm{t}}$",t=0.5,y=-0.1,fontsize=30)
bjet1.text("b",fontsize=30)
wb1.text("$W^{+}$",fontsize=30,t=0.5,y=-0.1,)
wb2.text("$W^{-}$",t=0.5,y=-0.14,fontsize=30)
bjet2.text(r"$\bar{\mathrm{b}}$",fontsize=30)
#diagram.plot() 0.5,0.55,0.69,0.35,  ,t=0.5,y=-0.08,

#f = plt.figure()
#f.set_figwidth(4)
#f.set_figheight(4)
#diagram.scale(0.6)
diagram.plot()

#plt.show()
#plt.SaveAs("diagram1.eps")
plt.savefig('topquark-qq.eps', format='eps')

