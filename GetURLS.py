from appscript import app
import easygui

# TODO: Extract tab name
# TODO: If file exists, append


# Export all URLS to a markdown file
def export(urls_list):
    filename = easygui.enterbox('File name')
    filename = filename + '.md'
    file = open(filename, 'w')
    for i in urls_list:
        file.write(i.strip("''") + '\n' + '\n')
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
    app('Safari').quit()
