ialt=float(input())
ivel=float(input())
mass=float(input())
talt=float(input())
thrust=float(input())
t=0.0
g=9.81
v=ivel
alt=ialt
print(f"{t:.1f}, {alt:.1f}, {v:.1f}")
if talt==ialt:
    print("Simulation ended without reaching the target altitude.")

else:
    t=0.0
    
    while True:
        a=(thrust-mass*g-v*0.1)/mass
        v=v+a
        alt=alt+v
        t+=1.0
        print(f"{t:.1f}, {alt:.1f}, {v:.1f}")
        if alt>=talt:
            print("Rocket reached the target altitude.")
            break
        if alt<ialt:
            print("Rocket crashed.")
            break
