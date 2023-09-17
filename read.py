
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀完了．總共有', len(data), '筆資料.')


sum_len = 0
for d in data: #把每一個留言放到d裡，
	sum_len = sum_len + len(d) #把每一個留言的長度加總
print('留言的平均長度為:', sum_len/len(data)) #把加總的長度 / 留言總數(1000000)