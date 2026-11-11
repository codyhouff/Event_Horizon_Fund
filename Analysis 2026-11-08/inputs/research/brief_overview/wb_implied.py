import sys
sys.stdout.reconfigure(encoding="utf-8")
Y=list(range(2023,2031))
cowos=[2.5317e6,7.076e6,1.59732e7,2.55571e7,4.07317e7,6.8218e7,1.13355e8,1.7788e8]
cshare=[0.60625,0.813333,0.9,0.9,0.9,0.95,1,1]
hbm=[1.875e6,4.56e6,8.06364e6,1.21277e7,2.12777e7,3.22199e7,5.61598e7,9.40561e7]
hsh=[0.8,0.95,0.95,0.98,0.98,0.98,0.98,0.98]
waf=[2.52e6,3.18e6,3.879e6,4.309e6,4.908e6,5.658e6,6.30405e6,7.1276e6]
cpw=[24,26,14,15,12.5,14,12,13]
tot=[1.5e6,4.332e6,7.66045e6,1.18851e7,2.08521e7,3.15755e7,5.50366e7,9.2175e7]
mkt=[50,144.4,255.348,396.171,695.071,1052.52,1834.55,3072.5]
hbm_mkt=[2.5,6.688,12.5469,20.6203,40.7184,71.4787,148.765,306.425]
hbm_waf=[660000,1.884e6,3.0144e6,4.82304e6,7.71686e6,1.2347e7,1.97552e7,3.16083e7]
cow_waf=[144000,348000,1.044e6,1.7748e6,3.01716e6,5.12917e6,8.71959e6,1.48233e7]
wpc=[1000,1000,1667,1667,2600,2600,2400,2400]
aishare=[0.0248016,0.0523948,0.141061,0.183881,0.339888,0.39862,0.72753,0.994779]
print("Year | binding | CoWoS(dbl) | CoWoS(single) | HBM | wafers | total chips | chip mkt $B | HBM $B | HBM flat-3% $B | AI share <=5nm | new-chip GW | 4yr-cohort GW")
flat=[None]*8
for i,y in enumerate(Y):
    c2=cowos[i]*cshare[i]; c1=cowos[i]; h=hbm[i]*hsh[i]; w=waf[i]*cpw[i]
    b=min(("CoWoS",c2),("HBM",h),("Wafers",w),key=lambda t:t[1])[0] if i>=2 else "-"
    b1=min(("CoWoS",c1),("HBM",h),("Wafers",w),key=lambda t:t[1])[0] if i>=2 else "-"
    newgw=tot[i]*wpc[i]/1e9
    coh=sum(tot[j]*wpc[j] for j in range(max(0,i-3),i+1))/1e9
    fl = hbm_mkt[3]*(hbm[i]/hbm[3])*1.03**(i-3) if i>=3 else None
    print(y,"|",b,"/",b1,"|",f"{c2/1e6:.1f}M",f"{c1/1e6:.1f}M",f"{h/1e6:.1f}M",f"{w/1e6:.1f}M","|",f"{tot[i]/1e6:.1f}M",f"{mkt[i]:.0f}",f"{hbm_mkt[i]:.0f}", f"{fl:.0f}" if fl else "-", f"{aishare[i]*100:.0f}%", f"{newgw:.1f}", f"{coh:.0f}")
g=lambda a,i,j:(a[j]/a[i])**(1/(j-i))
print("\n2026->2030 multiples: chips %.1fx, chip $ %.1fx, HBM units %.1fx, HBM $ %.1fx, HBM wafers %.1fx, CoWoS wafers %.1fx, <=5nm wafers %.2fx, AI wafers %.1fx"%(tot[7]/tot[3],mkt[7]/mkt[3],hbm[7]/hbm[3],hbm_mkt[7]/hbm_mkt[3],hbm_waf[7]/hbm_waf[3],cow_waf[7]/cow_waf[3],waf[7]/waf[3],(aishare[7]*waf[7])/(aishare[3]*waf[3])))
print("CAGRs 2026-30: chip $ %.0f%%, HBM units %.0f%%, CoWoS wafers %.0f%%"%((g(mkt,3,7)-1)*100,(g(hbm,3,7)-1)*100,(g(cow_waf,3,7)-1)*100))
print("HBM wafers/yr 2030 %.1fM vs ~21M/yr total DRAM industry wafers today (~1.75M wspm)"%(hbm_waf[7]/1e6))
