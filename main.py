#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pylab import *

C_array = [1.0*10**-6,10.0*10**-6,100.0*10**-6,1000.0*10**-6] #[F]
# C_array = [100.0*10**-6] #[F]
# C = 1.0**(-6) # [Ω]
R = 1000.0 #[Ω]
f = 100 # [Hz], 100 pulse per sec
omega = f / (2.0*pi) #[rad/s]

yscale('log')
for C in C_array:
    response = [] 
    k = 1/(C*R)
    t = arange(0,10,0.001)
    response = k*(omega**2-k**2)*(exp(-1.0*k*t) - cos(omega*t) - k*sin(omega*t))
    plot(t,response)

show()
