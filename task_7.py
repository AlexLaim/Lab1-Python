# links = ['www.google.com', 'www.google', 'google.com', 'google']


# def func(str):
#     if str.endswith('.com'):
#         return "http://"+str
#     else:
#         return "http://"+str+".com"


# newLinks = [func(link) for link in links if link.startswith('www')]

# print(newLinks)


links = [(lambda i: "http://" + i if i.endswith('.com') else "http://" + i + ".com")(i) 
         for i in ['www.google.com', 'www.vk', 'google.com', 'google'] if i.startswith('www')]

print(links)