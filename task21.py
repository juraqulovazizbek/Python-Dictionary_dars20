def count_name( names: list [ str  ]) -> dict [str , int ]:
    unique_names = set()


    for name in names:
        unique_names.add(name)


    result = {}    
    for name in unique_names:
     result[name] = 0


     for name in result.keys():
        result[name] = names.count(name)


    return result


name = ["ali" , "valiz" , "g'ani" , "sami", "ali " , "vali"]
result = count_name(name)
print(result)
