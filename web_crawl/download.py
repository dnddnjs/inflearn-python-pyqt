import urllib.request as dw

img_url = "http://blogfiles.naver.net/data18/2006/10/17/154/coolads_1012_043-jwblues.jpg"
html_url = "http://google.com"

save_path1 = "./test1.jpg"
save_path2 = './index.html'

f = dw.urlopen(img_url).read()
f2 = dw.urlopen(html_url).read()

save_file1 = open(save_path1, 'wb')
save_file1.write(f)
save_file1.close()

with open(save_path2, 'wb') as save_file2:
	save_file2.write(f2)
	
print('download complete')