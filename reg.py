try:
    import pickle as pick
except ModuleNotFoundError:
    print('please, load module: "pickle" with hellping pip')
    exit(0)
    
path_data: str = 'data\\user_data\\accs'    

class User:
    def __init__(self, logs: str = None, pasws: str = None, nn: list = None):
        self.__logins: list = logs
        self.__nicknames: list = nn
        self.__passwords: list = pasws
        
        self.status_activity = False
        
    def entrance_account(self, login: str = None, nickname: str = None, password: str = None):
        status = False
         
        if self.status_activity == False:
            if type(login) is str and login in self.__logins: status = True
            else: status = False
            if type(nickname) is str and nickname in self.__nicknames: status = True
            else: status = False
            if type(password) is str and password in self.__passwords: status = True
            else: status = False
        
        self.status_activity = status
        return status
    
    def exit_account(self):
        self.status_activity = False
        
    def create_account(self, login: str = None, nickname: str = None, password: str = None):
        if type(login) is str: pick.dump(login, open(f'{path_data}\\logs.bin', 'wb'))
        if type(nickname) is str: pick.dump(nickname, open(f'{path_data}\\logs.bin', 'wb'))
        if type(password) is str: pick.dump(password, open(f'{path_data}\\pasws.bin', 'wb'))
    
if __name__ == '__main__':
    
    user = User(logs = pick.load(open(f'{path_data}\\logs.bin', 'rb')), nn = pick.load(open(f'{path_data}\\nn.bin', 'rb')), pasws = pick.load(open(f'{path_data}\\pasws.bin', 'rb')))
    print(user.f())