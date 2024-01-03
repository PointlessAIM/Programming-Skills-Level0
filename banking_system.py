'''
Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions. 
'''
class User:
    userid:str
    password:str
    balance:int

    def __init__(self, userid, password, balance=2000):
        self.userid = userid
        self.password = password
        self.balance = balance       

user_credentials = [User(userid="user", password="password"), User(userid="Mayber", password="codingchallenge")]
    
def create_account(userid,password):
    return {"Error": "El usuario ya existe"} if search_user(userid) else user_credentials.update({userid:password})
def menu(userid):
    control = "n"
    
    while control == "n":
        print("1. ver saldo.")
        print("2. depositar dinero.")
        print("3. retirar dinero.")
        print("4. transferir dinero.")
        opcion= int(input())

        match(opcion):
            case 1:
                print(view(userid))
            case 2:
                sum= int(input("ingrese monto a depositar.\n"))
                deposit(userid, sum)
            case 3:
                sum= int(input("ingrese monto a retirar.\n"))
                withdraw(userid,sum)
            case 4:
                dest_userid=input("ingrese el ID del usuario destino.\n")
                sum = int(input("ingrese monto a transferir.\n"))
                transfer(userid, sum, dest_userid)
            case _:
                print("Please insert a Valid option.")

        control=input("Desea salir? y/n\n")
        
        if control == 'y':
            print("Hasta luego. Vuelva pronto!")

def login(userid:str, password:str)->bool:
    '''
    User has three tries to log in. If failed three times, suspend user.

    :param: userid, password: str - user credentials.
    '''
    limit = 3

    while limit >0:
    
        if validate_credentials(userid,password):
            print("success.\n")
            return True
        else:
            print('wrong credentials.\n')
            limit -= 1
    if limit == 0: 
        print("sorry. You're suspended.\n")
        return False

def search_user(userid:str)->User or any:
    '''
    hace una búsqueda del usuario en las credenciales almacenadas si el usuario existe.
    
    :param: userid:str - ID proporcionado por el usuario.
    :return: object or error - objeto resultante contiene datos del usuario.

    '''
    user= filter(lambda user: user.userid == userid, user_credentials)
    try:
        return list(user)[0]
    except:
        return {"Error": "No se ha encontrado el usuario"}
    
def validate_credentials(userid:str, password:str)->bool:
    '''
    valida que las credenciales pertenezcan al usuario.

    :param: userid, password: str - ID y Password proporcionados por el usuario.
    :return: bool - son correctas ambas credenciales?
    '''
    user= search_user(userid)
    return True if userid == user.userid and password == user.password else False

def deposit(userid:str,sum):
    '''sumar cantidad actual mas deposito'''
    user=search_user(userid)
    if type(user) == User:
        user.balance += sum
        print("Success.\n")
        return 

def withdraw(userid,sum):
    '''restar cantidad actual menos deposito'''
    user=search_user(userid)
    if type(user) == User:
        if sum > user.balance:
            print("Not enough funds.")
            return
        user.balance -= sum
        print (f"success.\n {view(userid)}")
    return

def view(userid):
    '''mostrar cantidad actual'''
    user=search_user(userid)
    if type(user) == User:
        return f"Balance actual: {user.balance}"
    
def transfer(userid,sum, dest_userid):
    '''
    validar userid del cliente destino, 
    validar que la cantidad a transferir sea menor o igual a la disponible
    restar de la cantidad actual lo que se transfiere
    '''
    user=search_user(userid)
    dest_user=search_user(dest_userid)
    if type(user) == User and type(dest_user) == User:
        if 0 < sum <= user.balance:
            user.balance -= sum
            dest_user.balance += sum
            print(f"Success. {view(userid)}")
            return 
        print( "Operation Failed. Not enough funds.")
        return

def main():
    print("bienvenido! Por favor ingrese sus datos.")
    userid = input("ingrese su ID: ")
    password = input("ingrese su contraseña: ")

    if login(userid, password):
        menu(userid)


if __name__ == "__main__":
    main()
        