list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge(dict1, dict2):
    return(dict1.update(dict2))


def merge_lists(list_1, list_2) -> list:
    list3=[]
    idInd={}
    for i in range(0,len(list_1)):
    	list3.append(list_1[i])
    	idInd[list_1[i]["id"]]=i
    
    for i in range(0,len(list_2)):
    	if list_2[i]["id"] in idInd:
    		ind=idInd[list_2[i]["id"]]
    		merge(list3[ind],list_2[i])
    	else :
    		list3.append(list_2[i])
    
    return list3

list_3 = merge_lists(list_1, list_2)