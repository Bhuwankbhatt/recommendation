def recomendation(request):
    print(request.user)
    ## You need to implement the necessary database models##
    ##Cluster below be the model where clustering is done
"""user = Cluster.objects.get(user=request.user)


print(user)
print(user.cluster_name)
print(Cluster.objects.filter(cluster_name=Cluster.objects.get(user=request.user)))
neighbour_users = Cluster.objects.filter(cluster_name=Cluster.objects.get(user=request.user).cluster_name)
list = []
for i in neighbour_users:
    saman = Record.objects.filter(user=i.user)
    for i in saman:
        list.append(i.item.id)
        """
mylist = set(list)

countlist = []

for i in mylist:
    a = []
    a.append(i)
    a.append(list.count(i))
    countlist.append(a)


def sortSecond(val):
    return val[1]


# print(countlist)
countlist.sort(key=sortSecond, reverse=True)
# print(countlist)
countlist = countlist[0:10]
print(countlist)
item_id_list = []
for i in countlist:
    item_id_list.append(i[0])
print(item_id_list)
recomended_item = []
"""for i in item_id_list:
    each_item = content.objects.get(id=i)
    print(each_item.item_name)
    recomended_item.append(each_item)
print("hello", recomended_item)
categories = Category.objects.all()

companies = company.objects.all()

return render(request, 'supermarket/home2.html',
              {'post': recomended_item, 'categories': categories, 'companies': companies})
"""