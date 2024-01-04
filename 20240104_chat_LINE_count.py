# 對話紀錄統計_LINE

import os

# 讀取檔案
def read_file(filename):
	text = [] # 儲存讀取的內容
	with open(filename, 'r', encoding='utf-8-sig') as f: # -sig去除讀檔產生的編碼紀錄文字
		for line in f:
			text.append(line.strip('\n').split(' ')) # 去除分行、依空格切割
	return text

# 統計對話內容字數、貼圖數、圖片數
def count(text):
	
	Allen_sticker = 0
	Allen_image = 0
	Allen_word = 0

	Viki_sticker = 0
	Viki_image = 0
	Viki_word = 0

	# 對話紀錄格式為 時間 說話者 內容，分別統計各說幾個字、傳幾張貼圖、圖片
	for line in text:
		if line[1] == 'Allen':
			if line[2] == '貼圖':
				Allen_sticker += 1
			elif line[2] == '圖片':
				Allen_image += 1
			else:
				for word in line[2:]: # [2:]表示從第2個取到最後
					Allen_word += len(word)
		elif line[1] == 'Viki':
			if line[2] == '貼圖':
				Viki_sticker += 1
			elif line[2] == '圖片':
				Allen_image += 1
			else:
				for word in line[2:]:
					Viki_word += len(word)
	print('Allen說了', Allen_word, '個字，傳了', Allen_sticker, '張貼圖、', Allen_image, '張圖片')
	print('Viki說了', Viki_word, '個字，傳了', Viki_sticker, '張貼圖、', Viki_image, '張圖片')

# 主程式
def main():
	filename = 'LINE-Viki.txt'
	if os.path.isfile(filename): # 檢查檔案是否存在
		text = read_file(filename) # 紀錄讀取檔案後的內容
		new_chat = count(text) # 紀錄格式轉換後的內容
		print('計算完成！')
	else:
		print('檔案不存在')

main()


