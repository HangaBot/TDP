import numpy as np
import matplotlib.pyplot as plt

Tc = 1    # 1us
N = 100000  # Numero id copioni


#base dei tempi in us
t = np.linspace(0, N*Tc, N)

x = 1 * np.sin(2*np.pi* 0.4 * t )  #Volt

plt.figure(1)

plt.plot(t, x)

#base delle frequenze
span = N
b = 0
f = np.arange(span)/(N*Tc)  + b / Tc# MHz

print("center frequency: {:f}".format((b+1) / (2*Tc)))

Xc =  Tc*np.sinc(f*Tc)*np.fft.fft(x,span)

X = np.sqrt(2) * Xc / (N*Tc)

plt.figure(2)
plt.plot(f, 10*np.log10(((np.abs(X)**2)/50)/(10**-3)))

plt.show()

