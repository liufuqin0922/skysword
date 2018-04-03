# -*- utf-8 -*-

a = {}
for line in open("aaa"):
    cc = line.split()
    if len(cc) == 3:
        isdn, other, call_type = line.split()
    elif len(cc) == 2:
        isdn, call_type = line.split()

    if isdn in a:
        if call_type in a[isdn]:
            a[isdn][call_type] += 1
        else:
            a[isdn][call_type] = 1
    else:
        b = {}
        b[call_type] = 1
        a[isdn] = b

for aa in a:
    if '1' in a[aa]:
        zj = a[aa]["1"]
    else:
        zj = 0

    if '2' in a[aa]:
        bj = a[aa]["2"]
    else:
        bj = 0

    if (bj+zj)>10:
    	if (100*bj/(bj+zj)) > 80:
            print aa, zj, bj
