# -*- coding: UTF-8 -*- 
#生成import文件

import re
import sys
reload(sys)  
sys.setdefaultencoding('utf8')


#读取import-before.txt
try:
	f=open('import-before.txt')
	content=f.read()
except Exception as e:
	print e
else:
	pass
finally:
	f.close()
#print content
items=re.compile(r'(.*?)\r\n(.*?)\r\n答案:(\d)').findall(content)
#print items[0][2]
out=''
for itme in items:
	options=itme[1].split(' ')
	correctIndex=int(itme[2])-1
	correct=options[correctIndex]
	#交换第一个和正确选项的位置
	options[correctIndex]=options[0]
	options[0]=correct
	ans='<br>'.join(list(options))
	#替换答案中的括号为anki填空模板
	question=itme[0].replace('（\t）',r'{{c1::'+correct+r'}}')

	if not out:
		out=question+'\t'+ans
	else:
		out+='\n'+question+'\t'+ans
print out

#替换掉选项号
out=re.sub(r'\d\)','',out)
#保存为import-after.txt
try:
	f=open('import-after.txt','w')
	f.write(out)
	print '保存为 import-after.txt 成功'
except Exception as e:
	print e
else:
	pass
finally:
	f.close()