import wikipedia as wk 
import csv
with open('data.csv', 'a') as csvfile:
	# fieldnames = ['topic', 'info']
	writer = csv.writer(csvfile)
	#writer.writeheader()
	while (True):
		search = input("New topic(n for exit) ")
		if search == "n":
			print("bye")
			break
		for page in wk.search(search):
			try:
				info = wk.page(page).content 
				info = info[:info.index("\n")]
				writer.writerow([page,info])
				print(page)
			except Exception as e:
				print(e)