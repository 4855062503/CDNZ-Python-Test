large_dict_list = [{"brand" : "Ferrari"}, {"brand" : "Lambo"}, {"brand" : "Ferrari"}]
ferrari_list = []
for car_dict in large_dict_list:
    if car_dict["brand"] == "Ferrari":
        ferrari_list.append(car_dict)
print(ferrari_list)
