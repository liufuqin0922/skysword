# iconv -f GBK -t UTF-8 A* >B.txt
# rm A*
# awk -F',' '$3~/^1/ {print $3}' B.txt | awk '!a[$0]++' >isdn.txt
# grep -f shbj.txt isdn.txt >xxhh.txt
# grep -f xxhh.txt B.txt >>result.txt

awk -F, '$2>0 && $8>0 {print $2}' B.txt | sort | uniq -c | sort -k1nr | awk '$1>100' >tmp
while read num line
do
	isdn=${line:0:7}
	aa=`grep $isdn isdn_all.txt`
	awk -F, '$2=="'$line'" && $8>0 {print $3,$6,$8/60000}' B.txt | while read other calltype dur
	do
		others=${other:0:7}
		bb=`grep $others isdn_all.txt`
		echo $num $line ${aa:8} $other ${bb:8} $calltype $dur
	done 
done < tmp
