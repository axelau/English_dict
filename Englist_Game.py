import random

list = []

with open('english_words.csv', 'r', encoding='utf-8') as f:
	for words in f:
		english, chinese, fonttype = words.strip().split(',')
		eng = [english, chinese, fonttype]
		#print(eng[0])
		#測試第一個值
		#print(eng[1])
		#測試第二個值

		english_list = {}
		english_list['english']=eng[0]
		english_list['chinese']=eng[1]
		english_list['fonttype']=eng[2]
		list.append(english_list)


# ----------------

print('開始選擇題：')
print('全部共有',len(list),'題')

count = 0

while count < 10:
	r = random.randint(0,len(list)-1)
	print(list[r]['english'], ':')
	ans=input()
	if ans == 'quit':
		break
	else:
		count += 1
		print('詞性為:',list[r]['fonttype'],'語')
		print(list[r]['english'],'的翻譯為:',list[r]['chinese'])
		print('下一題')
		print('----------')

print('可以休息一下了')

# 印出指定對應字
#print(elist[0]['english'])


#Example
# p0 = {
# 'english':'adapt',
# 'chinese':'合適'
# }
# print(p0['english'])

# food = {
#  'ramen': '拉麵',
#  'pasta': '義大利麵'
# }

# print(food['ramen'])