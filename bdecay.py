
import matplotlib.pyplot as plt
from feynman import Diagram

fig = plt.figure(figsize=(10.,10.))
ax = fig.add_axes([0,0,1,1], frameon=False)

diagram = Diagram(ax)


in1 = diagram.vertex(xy=(.05,.5), marker='')
in2= diagram.vertex(xy=(.35,.25), marker='')
v1 = diagram.vertex(xy=(.25,.5), marker='')
v2 = diagram.vertex(xy=(.50,.6), marker='')
lep1 = diagram.vertex(xy=(.75,.7), marker='')
lep2 = diagram.vertex(xy=(.75,.55), marker='')




q1 = diagram.line(in1, v1,arrow = False)
q2 = diagram.line(v1, in2,arrow = False)
w = diagram.line(v1, v2, style='wiggly',nwiggles=4, marker='')
mu = diagram.line(v2, lep2,arrow = False)
nu = diagram.line(lep1,v2,arrow = False)


#wb1 = diagram.line(w1,t1, style='wiggly',nwiggles=4, marker='')
#bjet1 = diagram.line(t1, b1,arrow = False)
#wb2 = diagram.line(t2, w2, style='wiggly',nwiggles=4, marker='')
#bjet2 = diagram.line(b2,t2,arrow = False)

q1.text("b",t=0.5,y=+0.05,fontsize=30)
q2.text("c",t=0.5,y=-0.05,fontsize=30)
w.text(r"$W^{-}$",t=0.5,y=0.1,fontsize=30)
mu.text(r"$\mu^{-}$",t=0.5,y=-0.05,fontsize=30)
nu.text(r"$\bar{\nu}$",t=0.5,y=-0.05,fontsize=30)


#diagram.plot() 0.5,0.55,0.69,0.35,  ,t=0.5,y=-0.08,

#f = plt.figure()
#f.set_figwidth(4)
#f.set_figheight(4)
diagram.scale(1.)
diagram.plot()

#plt.show()
#plt.SaveAs("diagram1.eps")
plt.savefig('bdecay.eps', format='eps')

