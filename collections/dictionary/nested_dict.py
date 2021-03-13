employee={
    1001:{"id":1001,"name":"Aswani","gender":"F","salary":50000,"exp":2},
    1002:{"id":1002,"name":"Abhinav","gender":"M","salary":50000,"exp":2},
    1003:{"id":1003,"name":"Shibin","gender":"M","salary":60000,"exp":3}

}
def print_info(**kwargs):
    print(kwargs)
    prop=kwargs["prop"]
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"],employee[id][prop])
print_info(id=1001,prop="salary")