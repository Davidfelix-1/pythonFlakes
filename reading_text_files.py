
with open("account,txt",mode="r")as account:
    print(f'{"Account":<}{"Name":,10}{"Balance":>10}')
    for record in account:
        account, name, balance =record.split()
        print(f'{account:<10}{name:<10}{balance:>10}')