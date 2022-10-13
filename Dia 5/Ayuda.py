dic = {'clave':100,'clave2':500}
print(dic)
d = dic.popitem()
print(d)
print(dic)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
print(marcas_smartphones.isdisjoint(marcas_tv))
