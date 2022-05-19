
import matplotlib.pyplot as plt
from feynman import Diagram

fig = plt.figure(figsize=(10.,10.))
ax = fig.add_axes([0,0,1,1], frameon=False)

diagram = Diagram(ax)
#diagram.text(.4,0.9,"Associated Vector Boson", fontsize=40)
#diagram.text(.6,0.83,"(VH or 'Higgs Strahlung')", fontsize=40)
in1 = diagram.vertex(xy=(.05,.75), marker='')
in2= diagram.vertex(xy=(.05,.25), marker='')
v1 = diagram.vertex(xy=(.30,.5))
v2 = diagram.vertex(xy=(.60,.5))
higgsout = diagram.vertex(xy=(.8,.65))
out1 = diagram.vertex(xy=(.8,.35),marker='')
c1 = diagram.vertex(xy=(.9,.75),marker='')
c2 = diagram.vertex(xy=(.9,.55),marker='')
l1 = diagram.vertex(xy=(.9,.25),marker='')
l2 = diagram.vertex(xy=(.9,.45),marker='')

q1 = diagram.line(in1, v1)
q2 = diagram.line(v1, in2)
wz1 = diagram.line(v1, v2, style='wiggly',nwiggles=6)
wz2 = diagram.line(v2, out1, style='wiggly',nwiggles=6)
higgs = diagram.line(v2, higgsout, arrow=False, style='dashed')
charm1 = diagram.line(c1,higgsout)
charm2 = diagram.line(higgsout, c2)
lep1 = diagram.line(out1, l1)
lep2 = diagram.line(out1, l2)

q1.text("q",fontsize=30)
q2.text(r"$\bar{\mathrm{q}}$",fontsize=30)
wz1.text("$Z/W^\pm$",t=0.5,y=0.1,fontsize=30)
wz2.text("$Z/W^\pm$",t=0.5,y=-0.15,fontsize=30)
higgs.text("H",fontsize=30)
charm2.text("c",fontsize=30)
charm1.text(r"$\bar{\mathrm{c}}$",fontsize=30)
lep1.text(r"$\mathcal{l}^{\pm}/\mathcal{l}^{\pm}$",t=0.5,y=-0.1,fontsize=30)
lep2.text(r"$\mathcal{l}^{\mp}/\nu$",t=0.5,y=0.1,fontsize=30)
#diagram.plot() 0.5,0.55,0.69,0.35,

#f = plt.figure()
#f.set_figwidth(4)
#f.set_figheight(4)
diagram.scale(0.6)
diagram.plot()

#plt.show()
#plt.SaveAs("diagram1.eps")
plt.savefig('vbh_hcc.eps', format='eps')

