from numpy import *
from matplotlib.pyplot import *
import smithplot
rcParams['font.family'] = "Times New Roman"
rcParams['font.size'] = "12"

# Start figure
subplot(111, projection="smith")

# VSWR circle
G = 0.5*exp(2j*pi*linspace(0,1,100))
ZL = -(G+1)/(G-1)
plot(ZL, "k")

# Example points
plot(1+0j, marker="o", label="$1+0j$")
plot(1+1j, marker="o", label="$1+1j$")
plot(0.5-0.5j, marker="o", label="$0.5-0.5j$")

legend()
tight_layout()
savefig("example.pdf", bbox_inches='tight')
show()
