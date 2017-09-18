import webbrowser

#webbrowser.open("https://www.python.org/", new=1)

# help(webbrowser)
# get will let you specify which browser to use
theFox = webbrowser.get(using='firefox')
theFox.open_new("https://www.python.org")

chrome = webbrowser.get(using='chromium-browser')
chrome.open_new("https://www.python.org")
