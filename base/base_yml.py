import yaml



def base_yml(path,key):
    with open("../data/%s"%path,"rb") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data[key]


def read_data(path,key):
    data = base_yml(path,key)
    case_data = data.values()
    data_list = list()
    for testData in case_data:
        data_list.append(testData)

    return data_list
# def read_data(path,key):
#     datas = base_yml(path,key)
#     login_data = []
#     for i in datas:
#         username = i["userName"]
#         password = i["password"]
#         data ="(" +username+","+password+")"
#         login_data.append(data)
#     return login_data
#
if __name__ == '__main__':
    t = read_data("login.yml","test_login")
    print(t)