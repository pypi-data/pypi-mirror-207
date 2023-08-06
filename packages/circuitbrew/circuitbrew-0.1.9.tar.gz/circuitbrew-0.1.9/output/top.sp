*
.option brief=1
.lib "/Users/virantha/dev/circuitbrew/skywater-pdk-libs-sky130_fd_pr/models/sky130.lib.spice" tt
.option brief=0
.option scale=1e-6
*xm1 d1 g1 0 0 sky130_fd_pr__nfet_01v8_lvt w=1 l=0.5
*vgs g1 0 dc=0.9
*vds d1 0 dc=0.9
*---------------------------------------
.temp 85
.param voltage=1.8
.option post

.subckt Main 
Vpwlpreset _pR p.gnd PWL (0n 0 4n 0 4.5n 1.8)
Vpwlsreset _sR p.gnd PWL (0n 0 4n 0 4.5n 1.8)
xbuc _pR _sR r.t r.f r.e VerilogBucketE1of2_0
xwchb_0 _pR l.t l.f l.e p.vdd p.gnd r_0 r_1 r_2 Wchb
xwchb_1 _pR r_0 r_1 r_2 p.vdd p.gnd r_3 r_4 r_5 Wchb
xwchb_2 _pR r_3 r_4 r_5 p.vdd p.gnd r_6 r_7 r_8 Wchb
xwchb_3 _pR r_6 r_7 r_8 p.vdd p.gnd r.t r.f r.e Wchb
xsrc _pR _sR l.t l.f l.e VerilogSrcE1of2_0
xvdd p.vdd p.gnd Supply
.ends


.subckt Supply p.vdd p.gnd
.measure TRAN supplycurrent0 avg i(Vvdd_vdd)  
.measure TRAN supplypower0 PARAM='-supplycurrent0*1.8'
.measure TRAN supplypower_direct0 AVG P(Vvdd_vdd)  
Vvdd_vss p.gnd 0 0.0
Vvdd_vdd p.vdd 0 1.8
.ends


.subckt Wchb _pReset l.t l.f l.e p.vdd p.gnd r.t r.f r.e
xCelement2_inst_1 l.f r.e r.f p.vdd p.gnd Celement2
xCelement2_inst_0 l.t r.e r.t p.vdd p.gnd Celement2
xInv_p_strength_2_n_strength_2_vt_svt_inst_0 _pReset mypreset p.vdd p.gnd Inv_p_strength_2_n_strength_2_vt_svt
xNorN_N_3_inst_0 r.t r.f mypreset l.e p.vdd p.gnd NorN_N_3
.ends


.subckt Celement2 i[0] i[1] o p.vdd p.gnd
xmn0 t218_0 i[0] p.gnd p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmn1 _o i[1] t218_0 p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmp0 d_0 i[0] _o p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
xmp1 p.vdd i[1] d_0 p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
xmn2 t245_0 i[1] p.gnd p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmn3 d_1 i[0] p.gnd p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmn4 _o o t245_0 p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmp2 d_2 o _o p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
xmp3 d_3 i[0] d_2 p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
xmp4 p.vdd i[1] s_4 p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
xInv_p_strength_2_n_strength_2_vt_svt_inst_1 _o o p.vdd p.gnd Inv_p_strength_2_n_strength_2_vt_svt
.ends


.subckt Inv_p_strength_2_n_strength_2_vt_svt inp out p.vdd p.gnd
xmn0 p.gnd inp out p.gnd sky130_fd_pr__nfet_01v8_lvt w=2 l=0.5
xmp0 p.vdd inp out p.vdd sky130_fd_pr__pfet_01v8_lvt w=2 l=0.5
.ends


.subckt NorN_N_3 a[0] a[1] a[2] b p.vdd p.gnd
xmn0 b a[1] p.gnd p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmn1 b a[0] p.gnd p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmn2 b a[2] p.gnd p.gnd sky130_fd_pr__nfet_01v8_lvt w=1.0 l=0.5
xmp0 d_0 a[0] b p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
xmp1 d_1 a[1] d_0 p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
xmp2 p.vdd a[2] d_1 p.vdd sky130_fd_pr__pfet_01v8_lvt w=1.0 l=0.5
.ends


.hdl template_0_hspice_src_1of2.va


.hdl template_0_hspice_bucket_1of2.va



xmain Main

.tran 1p 10n

.end

