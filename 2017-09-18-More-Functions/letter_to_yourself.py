def print_edge():
    print('+',end='')
    print(50*'-',end='')
    print('+')

def print_stamp():
    print('|',end='')
    print(45*' ',end='')
    print('#### |')
    
def print_blank():
    print('|',end='')
    print(50*' ',end='')
    print('|')

def print_name(name):
    print('|',end='')
    print(20*' ',end='')
    print(name,end='')
    print((30-len(name))*' ',end='')
    print('|')


    
print_edge()
print_stamp()
print_stamp()
print_stamp()
print_blank()
print_blank()
print_name('Bill Gates')
print_name('1 Microsoft Way')
print_name('Redmond, WA 98104')
print_blank()
print_edge()