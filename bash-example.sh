for i in `cut -d, -f2 B.txt | sort | uniq -c | sort -k1nr | awk '$1>100 && $8>0 {print $2}'`;do echo;echo $i;export a=`expr substr $i 1 7`;grep $a isdn_all.txt;done >test.txt


for i in `cut -d, -f2 B.txt | sort | uniq -c | sort -k1nr | awk '$1>100 && $8>0 {print $2}'`; do grep $i B.txt | awk -F, 'BEGIN {total=0;answer=0;} $8>0 {answer=answer+1;} total=total+1; END {print total;print answer;}';done



for i in `cut -d, -f2 B.txt | sort | uniq -c | sort -k1nr | awk '$1>100 && $8>0 {print $2}'`; do awk -v aa=$i -F, '$2==aa' B.txt | awk -F, 'BEGIN {total=0;answer=0;} $8>0 {answer=answer+1;} total=total+1; END {print total;print answer;}'; done; 


#找被叫号码归属
for i in `awk -F, '$2==17198899739 && $8>0 {print $3}' B.txt`;do a=${i:0:7};grep $a isdn_all.txt;done

    944 18680164263
    794 18675341857
    525 18676240517
    332 18664473263
    249 18664410269
    174 18676182769
    147 18664412625
     45 13169866891
for i in `awk -F, '$2==18680164263 && $8>0 {print($1,$3,$6)}' 12321_zs.txt`;do export aa=`cut -f2 $i`;export a=`wc -l $aa 12321_zs.txt`;print $i,$a;done

awk -F, '$2==18680164263 {print $1,$5,$6,$7,$8/60000}' 12321_zs.txt | sort -k6r | more


iconv -f GBK -t UTF-8 *.txt >tmp;rm *.txt;awk -F, '$1>0 && $2>0' tmp | sort | uniq | cut -d, -f2 | sort | uniq -c | sort -k2 >0620


## vlr
for line in `awk '{print $1$2}' output.txt | awk -F";" '$2>0 {print $1$2}'`;do isdn=${line:0:13};vlr=${line:13};xx=`grep $vlr GT`;echo $isdn,$vlr,$xx;done


### 问题号码
17170366833
17170364156
17170363255
17170361269
17170368013
17097157901
17170366510
13069705870
13069703359
13045110132
13069702937
13069705191
13069706985
13069701052
13069703607
18675617390
18675603547
18666967242
18675629357
18666967294
18689333870
13144022495
18593152683
18687454346
15532486525
15622560197
15631232843
15653581367
18676268447
18620258111
16607602548
18676458025
18676430083
17081839613