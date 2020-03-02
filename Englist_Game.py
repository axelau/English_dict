import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#color dome
#print(color.BLUE + 'Hello World !' + color.END)

list = []

with open('text/english_words.csv', 'r', encoding='utf-8') as f:
	for words in f:
		english, chinese, fonttype , relation, relative_mean, sound, ex1, ex2= words.strip().split(',')
		eng = [english, chinese, fonttype, relation, relative_mean, sound, ex1, ex2]
		#print(eng[0])
		#測試第一個值
		#print(eng[1])
		#測試第二個值

		english_list = {}
		english_list['english']=eng[0]
		english_list['chinese']=eng[1]
		english_list['fonttype']=eng[2]
		english_list['relation']=eng[3]
		english_list['relative_mean']=eng[4]
		english_list['sound']=eng[5]
		english_list["ex1"]=eng[6]
		english_list["ex2"]=eng[7]
		list.append(english_list)

# ----------------
# 以下為輸入測試

print('開始選擇題：')
print('全部共有',len(list),'題')

count = 0

while count < 15:
	r = random.randint(0,len(list)-1)
	print('----------')
	
	#選擇英文還字解釋在先
	coin = random.randint(0,1)
	if coin == 1:
		print(list[r]['english'], ':')
	else:
		print(list[r]['chinese'], '的英文', '的',list[r]['fonttype'],'是？')
	print()

	ans=input()
	if ans == 'quit':
		break
	else:
		count += 1
		#選擇英文還字解釋在先
		if coin == 1:
			print('翻譯為:',list[r]['chinese'])
		else:
			print('英文翻譯為',list[r]['english'])
		#------------------
		print('詞性為:',list[r]['fonttype'])
		print('翻譯為:',list[r]['chinese'])
		print('關連字為:',list[r]['relation'])
		#如果字首有意思、則輸出
		# #--------------------------
		# if list[r]['relative_mean'] == 'none':
		# 	pass
		# else:
		# 	print('其意思為:',list[r]['relative_mean'])
		# --------------------------
		#如果有讀音、則輸出
		if list[r]['sound'] == 'none':
			pass
		else:
			print('讀音為:',list[r]['sound'])
		#--------------------------
		please=input()
		print('exmple A:')
		print(list[r]["ex1"])
		# if list[r]["ex2"] == 'none':
		# 	pass
		# else:
		# 	print(list[r]["ex2"])
		print('----------')
		print()
		print('下一題')

print('辛苦啦、')
print('可以休息一下了啦。')



# 印出指定對應字
#print(elist[0]['english'])


# #reference
# while count < 15:
# 	r = random.randint(0,len(list)-1)
# 	print('----------')
# 	print(list[r]['english'], ':')
# 	ans=input()
# 	if ans == 'quit':
# 		break
# 	else:
# 		count += 1
# 		print('詞性為:',list[r]['fonttype'],'詞')
# 		print('翻譯為:',list[r]['chinese'])
# 		print('關連字為:',list[r]['relation'])
# 		#如果字首有意思、則輸出
# 		if list[r]['relative_mean'] == 'none':
# 			continue
# 		else:
# 			print('關連字意思為:',list[r]['relative_mean'])
# 		#如果有讀音、則輸出
# 		if list[r]['sound'] == 'none':
# 			continue
# 		else:
# 			print('關連字意思為:',list[r]['sound'])
# 		print('----------')
# 		print()
# 		print('下一題')