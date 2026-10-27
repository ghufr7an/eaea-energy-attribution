"""Deterministic case study. Equipment parameters: published macro-BS model (605 W constant, 1067.7 W load-dependent at full load; EURASIP JWCN 2012:248, Table 1).
Service traffic shares are ILLUSTRATIVE ASSUMPTIONS (no public per-service ground truth exists). No randomness."""
import numpy as np
P0, PL = 605.0, 1067.7
share = {"eMBB": 0.70, "mMTC": 0.20, "URLLC": 0.10}
resv  = {"eMBB": 0.50, "mMTC": 0.20, "URLLC": 0.30}   # assumed reserved-capacity shares (URLLC reserves headroom)
for rho in (0.1, 0.3, 0.6):
    P = P0 + PL*rho; var = PL*rho; beta = P0/P
    print(f"\nload={rho}: P={P:.1f} W, baseline share={beta:.1%}, energy/h={P*3600/3.6e6:.3f} kWh")
    for s in share:
        v = var*share[s]
        pol_traffic = P*share[s]
        pol_equal   = v + P0/3
        pol_resv    = v + P0*resv[s]
        lo, hi = v, v + P0
        print(f"  {s:6s} traffic={pol_traffic:6.1f}  equal-base={pol_equal:6.1f}  reserved-base={pol_resv:6.1f}  bounds=[{lo:6.1f},{hi:6.1f}] W  max/min policy ratio={max(pol_traffic,pol_equal,pol_resv)/min(pol_traffic,pol_equal,pol_resv):.2f}")
# identifiability: meter-only regression E_t = b + sum_k a_k x_kt
t = np.arange(24); 
x1 = 0.5+0.4*np.sin(2*np.pi*t/24); x2 = 0.2+0.1*np.cos(2*np.pi*t/24+1.0); x3 = 0.5*x1       # x3 exactly proportional to x1
for name, X in (("independent loads", np.column_stack([np.ones(24), x1, x2, 0.1+0.05*np.sin(2*np.pi*t/8)])),
                ("service 3 proportional to service 1", np.column_stack([np.ones(24), x1, x2, x3]))):
    print(f"{name}: rank={np.linalg.matrix_rank(X)} of {X.shape[1]} columns, cond={np.linalg.cond(X):.3g}")
