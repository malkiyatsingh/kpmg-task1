def get_nestedObj(nestedObj,key):
    keyVal = key.split("/")
    value_dict = nestedObj
    for k in keyVal:
        value_dict = value_dict.get(k, None)
        if value_dict is None:
            return None
    return value_dict



print(get_nestedObj({"a":{"b":{"c":"d"}}},"a/b/c"))
print(get_nestedObj({"x":{"y":{"z":"a"}}},"x/y/z"))