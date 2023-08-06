*
* 0.75V_Standard_Vt Ring net list
.option nomod ingold=2 warnlim=100
+       limpts=30000 itl5=0 lvltim=2 method=gear
+       tnom=25 measdgt=5
.option MODSRH=0 runlvl=6 accurate
*---------------------------------------
.temp 105
.option brief=1
.lib '/usr/local/tsmc/7nm/Local/pdk/spice/tn07clsp001_1_1_2p3/cln7_1d8_sp_v1d1_2p3_usage.l' TTMacro_MOS_MOSCAP
.lib '/usr/local/tsmc/7nm/Local/pdk/spice/tn07clsp001_1_1_2p3/cln7_1d8_sp_v1d1_2p3_usage.l' pre_simu
.option brief=0
.param voltage=0.75
.param length=0.008u

.option post

.subckt Main 
xWchb_inst_0 UNC UNC UNC p.vdd p.gnd UNC UNC UNC Wchb
xvdd p.vdd p.gnd Supply
.ends


.subckt Supply p.vdd p.gnd
.measure TRAN supplycurrent0 avg i(Vvdd_vdd)  
.measure TRAN supplypower0 PARAM='-supplycurrent0*0.75'
.measure TRAN supplypower_direct0 AVG P(Vvdd_vdd)  
Vvdd_vss p.gnd 0 0.0
Vvdd_vdd p.vdd 0 0.75
.ends


.subckt Wchb l.t l.f l.e p.vdd p.gnd r.t r.f r.e
xCelement2_inst_1 l.f r.e r.f p.vdd p.gnd Celement2
xCelement2_inst_0 l.t r.e r.t p.vdd p.gnd Celement2
xNor2_inst_0 r.t r.f l.e p.vdd p.gnd Nor2
.ends


.subckt Celement2 i[0] i[1] o p.vdd p.gnd
xmn0 t104_0 i[0] p.gnd p.gnd nch_svt_mac nfin=2 l=0.008u
xmn1 _o i[1] t104_0 p.gnd nch_svt_mac nfin=2 l=0.008u
xmp0 p.vdd i[1] _o p.vdd pch_svt_mac nfin=2 l=0.008u
xmp1 p.vdd i[0] _o p.vdd pch_svt_mac nfin=2 l=0.008u
xmp2 t130_0 i[1] p.gnd p.vdd pch_svt_mac nfin=2 l=0.008u
xmp3 d_0 i[0] p.gnd p.vdd pch_svt_mac nfin=2 l=0.008u
xmn2 _o o t130_0 p.gnd nch_svt_mac nfin=2 l=0.008u
xmp4 t144_0 i[1] _o p.vdd pch_svt_mac nfin=2 l=0.008u
xmp5 d_1 i[0] _o p.vdd pch_svt_mac nfin=2 l=0.008u
xmp6 p.vdd o t144_0 p.vdd pch_svt_mac nfin=2 l=0.008u
xInv_inst_0 _o o p.vdd p.gnd Inv
.ends


.subckt Inv inp out p.vdd p.gnd
xmn3 out inp p.gnd p.gnd nch_svt_mac nfin=2 l=0.008u
xmp7 p.vdd inp out p.vdd pch_svt_mac nfin=2 l=0.008u
.ends


.subckt Nor2 a[0] a[1] b p.vdd p.gnd
xmn8 b a[1] p.gnd p.gnd nch_svt_mac nfin=2 l=0.008u
xmn9 b a[0] p.gnd p.gnd nch_svt_mac nfin=2 l=0.008u
xmp16 t237_0 a[0] b p.vdd pch_svt_mac nfin=2 l=0.008u
xmp17 p.vdd a[1] t237_0 p.vdd pch_svt_mac nfin=2 l=0.008u
.ends



xmain Main

.tran 1p 10n

.end

