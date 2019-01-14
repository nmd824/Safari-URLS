from appscript import app
from datetime import datetime

# To Do: Check if multiple windows are opened
# To Do: Check if > 50 && > 100 tabs are opened
# To Do: Check if file exists & if file exists, append
# To Do: Custom export name

# Export all URLS to a markdown file
def export(urls_list):
	filename = 'URLS_' + str(datetime.now().day) + '-' + str(datetime.now().month) + '-' + str(datetime.now().year) + '.md'
	file = open(filename, 'w')
	index = 1
	for i in urls_list:
		file.write(str(index) + ': ' + i + '\n')
		index += 1
	file.close()


if __name__ == '__main__':
	# Get all URLS from opened windows
	urls = app('Safari').windows.tabs.URL()

	''' 
	Split into individual URLS
	Since URLS are stored in a list (with all the URLs from each window an item in list)
	'''
	urls_list = str(urls).strip('[]').split(', ')

	export(urls_list)
