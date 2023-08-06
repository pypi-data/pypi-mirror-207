import sys
sys.path.insert(0, "..")
import os
import numpy as np
import matplotlib.pyplot as plt

import dbdreader
import gliderflight
import fast_gsw
import time

pattern = os.path.expanduser("~/gliderdata/helgoland201407/hd/sebastian-2014-*.?bd")
selector = dbdreader.DBDPatternSelect()
fns = selector.select(pattern = pattern, from_date="6 8 2014", until_date="10 8 2014")
#fns = fns[:12]
dbd = dbdreader.MultiDBD(filenames=fns, complement_files=False, complemented_files_only=True)
_ = dbd.get_CTD_sync("m_ballast_pumped", "m_pitch")
tctd, C, T, P, m_ballast_pumped, m_pitch = _
density = fast_gsw.rho(C*10, T, P*10, 7.5, 54)

gf = gliderflight.DynamicCalibrate(rho0=1025, k1=0.2, k2=0.92, dt=0.5)
#gf = gliderflight.SteadyStateCalibrate(rho0=1025)
gf.define(mg=62.430, Cd0=0.159, Vg=61e-3) # Cd0 from dynamic_model
gf.set_input_data(tctd, P, m_pitch, m_ballast_pumped, density)
t0=time.time()
cr1 = gf.calibrate("Cd0")
t1=time.time()
print(t1-t0)
m = gf.solve()

#calibration_coefs = gf.calibrate("Cd0", "mg", verbose=True)
