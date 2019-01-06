p = open("/Users/architdwivedi/Documents/a.csv").read().split("\n")[:-1]
ar = {}
for e in p:
    title, url = e.split("@@")
    l = url.rfind('/')
    url = url[l+1:]
    ar[url] = True
print(ar)
