
# coding: utf-8

# In[1]:


import csv
CDRFile = open("B.txt")

imeiFile = open("imei.txt")
imeiDict = []
for line in imeiFile:
    imeiDict.append(line.strip())
imeiFile.close()

abnormal_ci_file = open("mm_abnormal_ci.txt")
ciDict = []
for line in abnormal_ci_file:
    ciDict.append(line.strip())
abnormal_ci_file.close()

zs_isdn_file = open("zsall.txt")
zs_isdn_dict = []
for line in zs_isdn_file:
    zs_isdn_dict.append(line.strip()[2:])
zs_isdn_file.close()

mm_isdn_file = open("mmall.txt")
mm_isdn_dict =[]
for line in mm_isdn_file:
    mm_isdn_dict.append(line.strip()[2:])
mm_isdn_file.close()

zs_mm_abnormal_isdn_file = open("zs_mm_abnormal_imei_isdn.txt","w")

zs_mm_CI_file = open("zs_mm_abnormalCI_call.txt","w")

zs_mm_Model_file = open("zs_mm_Model.txt","w")

zs_mm_call_top_file = open("zs_mm_call_top.txt","w")

ab_imei = {}
ab_ci = {}
ab_top = {}
ab_model = {}

CDR = csv.DictReader(CDRFile)
for row in CDR:
    isdn = row[u'用户号码']
    called_num = row[u'对端号码']
    imei = row['IMEI/IMEISV']
    calltype = row[u'呼叫类型']
    CGI = row[u'CGI/SAI']
    CallTime = row[u'通话时长(ms)']
    
    if isdn[:7] in zs_isdn_dict:
        if isdn not in ab_top:
            ab_top[isdn] = [1,0]
            if len(CallTime)>0:
                ab_top[isdn][1]+=1
        else:
            ab_top[isdn][0]+=1
            if len(CallTime)>0:
                ab_top[isdn][1]+=1
            
        if imei in imeiDict:
            if isdn not in ab_imei:
                ab_imei[isdn] = [1,0]
                if len(CallTime)>0:
                    ab_imei[isdn] = [1,1]
            else:
                ab_imei[isdn][0]+=1
                if len(CallTime)>0:
                    ab_imei[isdn][1]+=1
                    
        if CGI in ciDict:
            if isdn not in ab_ci:
                ab_ci[isdn] = [1,0]
                if len(CallTime)>0:
                    ab_ci[isdn][1]=1
            else:
                ab_ci[isdn][0]+=1
                if len(CallTime)>0:
                    ab_ci[isdn][1]+=1
        
        if isdn not in ab_model:
            ab_model[isdn]=[called_num]
        else:
            ab_model[isdn].append(called_num)
CDRFile.close()         

for isdn, called in ab_model.items():
    flag = True
    for ss in called:
        if (ss[:7] in mm_isdn_dict or ss[:4] in ['0688']):
            flag = False
            break
    if flag:
        if len(called)>10:
            zs_mm_Model_file.write(isdn+' '+str(ab_top[isdn][0])+' '+"%.2f" % (ab_top[isdn][1]/ab_top[isdn][0])+'\n')
zs_mm_Model_file.close()

for isdn,calling in ab_imei.items():
    zs_mm_abnormal_isdn_file.write(isdn+' '+str(calling[0])+' '+"%.2f" % (calling[1]/calling[0])+'\n')
zs_mm_abnormal_isdn_file.close()

for isdn,calling in ab_ci.items():
    zs_mm_CI_file.write(isdn+' '+str(calling[0])+' '+"%.2f" % (calling[1]/calling[0])+'\n')
zs_mm_CI_file.close()

for isdn,calling in ab_top.items():
    zs_mm_call_top_file.write(isdn+' '+str(calling[0])+' '+"%.2f" % (calling[1]/calling[0])+'\n')
zs_mm_call_top_file.close()

