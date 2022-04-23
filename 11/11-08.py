link = input()
print(link[link.find("?q=") + 3:link.find("&")])
