# restriction variables
A_ub = []
# restriction limits
b_ub = []

def add_restriction(df,column_id,flag):
    restrictions_list = df[column_id].array.tolist()
    if flag == '1':
        A_ub.append(restrictions_list)
        limit = int(input('Provide the Maximum quantity: '))
        b_ub.append(limit)
    elif flag == '2': 
        restrictions_list = [x * -1 for x in restrictions_list]
        A_ub.append(restrictions_list)
        limit = int(input('Provide the Minimum quantity: '))
        b_ub.append(limit*-1)

def add_restriction_file(df,column_id,flag,limit):
    restrictions_list = df[column_id].array.tolist()
    if flag == '1':
        A_ub.append(restrictions_list)
        b_ub.append(limit)
    elif flag == '2': 
        restrictions_list = [x * -1 for x in restrictions_list]
        A_ub.append(restrictions_list)
        b_ub.append(limit*-1)

def restrictions_from_file(df):
    column_headers = df.columns.values.tolist()
    # transform columns to dict and remove [0] Category
    column_headers_dict = {str(index): i for index, i in enumerate(column_headers) if index > 0}

    with open("restrictions.txt") as f:
        for line in f:
            text = line.split(" ")
            restriction_number = text[0]
            flag = text[1]
            limit = int(text[2])
            add_restriction_file(df,column_headers_dict[restriction_number],flag,limit)   
    return A_ub, b_ub

def menu(df):
    column_headers = df.columns.values.tolist()
    # transform columns to dict and remove [0] Category
    column_headers_dict = {str(index): i for index, i in enumerate(column_headers) if index > 0}

    print("---------- ADD RESTRICTION --------")
    for category in column_headers_dict:
        print(category, column_headers_dict[category])
    print('\n\nFor leaving this menu type l / L')

    while(True):

        restriction_number = input('\n\nPlease provide the resource number to add restriction: ')

        if restriction_number == 'l' or  restriction_number == 'L':
            break
        
        restriction_type = input("\n\nPlese provide the restriction type: \n 1- Maximum \t 2- Minimum\n")
        if restriction_type == '1' or restriction_type == '2':
            add_restriction(df,column_headers_dict[restriction_number],restriction_type)
        else: 
            print('Invalid restriction type')

    return A_ub, b_ub