
items = {
    'espresso':{
    'milk':50,
    'water':100,
    'coffee':12,
    'price':10
    },
    'latte':{
    'milk':100,
    'water':120,
    'coffee':18,
    'price':22
    },
    'cappucino':{
    'milk':120,
    'water':100,
    'coffee':28,
    'price':28
    }
}

resource ={
'milk':300,
'water':300,
'coffee':150,
'money':0
}

user_wants = ''
one = two = five = ten = 0
stop_machine = True


# get what user wants
def user_choice():
    return input('whats your choice a)espresso b)latte c)cappucino :')


# get conis
def get_money():
    global one,two,five,ten
    print(f"your selected beverage costs {items[user_wants]['price']} rupees please insert coins below")
    one =int(input('How many ones? '))
    two =int(input('How many twos? '))
    five =int(input('How many fives? '))
    ten =int(input('How many tens? '))

# compare money and give balance
def check_money():
    total = (one*1) + (two * 2) + (five * 5) + (ten * 10)
    if items[user_wants]['price'] == total:
        print('Thanks for providing the exact change ')
        return True
    elif items[user_wants]['price'] < total:
        print(f"collect your change {total - items[user_wants]['price'] } ones")
        return True
    else :
        print(f"you have to insert {items[user_wants]['price'] - total} rupees more \nCollect your cash and try again")
        return False

# check resources
def check_resource():
    if items[user_wants]['milk'] < resource['milk'] and items[user_wants]['water']< resource['water'] and items[user_wants]['coffee'] < resource['coffee']:
        print('your item is being prepared')
        return True
    else:
        print('sorry resource not available')
        return False


# prepare item reduce resource add money
def reduce_resource():
    resource['milk'] = resource['milk'] - items[user_wants]['milk']
    resource['water'] = resource['water'] - items[user_wants]['water']
    resource['coffee'] = resource['coffee'] - items[user_wants]['coffee']
    resource['money'] = resource['money'] + items[user_wants]['price']

    print(f"resources reduced {resource}")

# dispense item

def dispense():
    print(f"Your {user_wants} is ready please collect it")

def money_matters():
    global stop_machine
    if check_money():
        if check_resource():
            reduce_resource()
            dispense()
        else:
            stop_machine = False
            print('please refill resources')
            return 0
    else:
        get_money()
        money_matters()

def start_machine():
    global user_wants, stop_machine
    while stop_machine:
        user_wants = user_choice()
        get_money()
        money_matters()

start_machine()
