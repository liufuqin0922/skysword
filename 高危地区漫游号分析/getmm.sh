rm 高危地市漫游号码.txt

for file in `ls roam*.txt`
do 
	mv ${file} ${file}.bak
done

sed -i 's///g' output.txt
grep -f Location_GuangDongMaoMing.txt output.txt | cut -c3-13 | sort >roam_GuangDongMaoMing.txt
grep -f Location_GuangXiNanNing.txt output.txt | cut -c3-13 | sort >roam_GuangXiNanNing.txt
grep -f Location_HaiNanHaiKou.txt output.txt | cut -c3-13 | sort >roam_HaiNanHaiKou.txt
grep -f Location_FuJianLongYan.txt output.txt | cut -c3-13 | sort >roam_FuJianLongYan.txt
grep -f Location_HuBeiXianTao.txt output.txt | cut -c3-13 | sort >roam_HuBeiXianTao.txt
grep -f Location_HuNanLouDi.txt output.txt | cut -c3-13 | sort >roam_HuNanLouDi.txt
grep -f Location_GuangXiBeiHai.txt output.txt | cut -c3-13 | sort >roam_GuangXiBeiHai.txt

#sed -i 's/$//g' roam_*

for file in `ls roam*.txt`
do
	total=`cat ${file}.bak | wc -l`
	add=`comm -23 ${file} ${file}.bak | wc -l`
	#let result=${add}/${total}*100
	result=`echo ${add} ${total} | awk '{printf("%0.2f\n",100*$1/$2)}'`
	echo ${file} "add" ${result}"%" >>高危地市漫游号码.txt
done

more roam_*.txt >>高危地市漫游号码.txt
sed -i 's/$//g' 高危地市漫游号码.txt
