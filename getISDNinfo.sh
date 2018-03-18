while read aa
do
	url="http://haoma.baidu.com/phoneSearch?search="$aa"&position=&request_page=1"
	curl -s $url | grep "upper_text" | while read line
	do
		bb=${line:24} 
		echo $aa $bb
		break
	done
	sleep 2s
done < isdn
