data = [
{"id":1,"name":"Product A","category":"Electronics","status":"active"},
{"id":2,"name":"Product B","category":"Clothing","status":"inactive"},
{"id":3,"name":"Product C","category":"Electronics","status":"active"},
{"id":4,"name":"Product D","category":"Electronics","status":"inactive"},
{"id":5,"name":"Product E","category":"Clothing","status":"active"},
{"id":6,"name":"Product F","category":"Electronics","status":"active"}
]
page = 1
page_size = 2
filters = {"category":"Electronics", "status":"active"}


def paginate_with_filters(data, page, page_size, filters):

# filtering
    filtered_data = []
    for item in data:
        match = True
        for key, value in filters.items():
            if key not in item or item[key] != value:
                match = False
                break
        if match:
            filtered_data.append(item)
    print(f"Total count of filtered data:{len(filtered_data)}")
    print(f"filtered data :{filtered_data}")

#  sorting
    sort_item_1 = input("enter the item to sort(id/name/category/status):")
    order = input("Enter the order(asc/desc):")
    if order == "asc":
        sorted_data = sorted(filtered_data, key=lambda x: x[sort_item_1], reverse=False)
    elif order == "desc":
        sorted_data = sorted(filtered_data, key=lambda x: x[sort_item_1], reverse=True)

#    ------> based on name
#     sorted_data = sorted(filtered_data, key=lambda x: x["name"],reverse=True)
#    ------> based on id
#     sorted_data = sorted(filtered_data, key=lambda x: x["id"],reverse=False)
#    ------> based on multiple keys
#     sorted_data = sorted(filtered_data, key=lambda x: (x["category"],x["status"]), reverse=True)

# paginate
    start = (page - 1) * page_size
    end = start + page_size
    # return filtered_data[start:end]

# invalid page_num
    if start >= len(sorted_data) or page <= 0:
        return []
    return sorted_data[start:end]

result = paginate_with_filters(data, page, page_size, filters)
print(result)