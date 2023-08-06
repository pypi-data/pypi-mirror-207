*
.option nomod ingold=2 warnlim=100
+       limpts=30000 itl5=0 lvltim=2 method=gear
+       tnom=25 measdgt=5
.option MODSRH=0 runlvl=6 accurate
*---------------------------------------

.temp ${temp}
.option brief=1
.lib 'mylib.spice' TT
.option brief=0
.param voltage=${voltage}
.param length=0.0060u

.option post

${circuit}

xmain ${main_type_name}

.tran 1p 10n

.end

