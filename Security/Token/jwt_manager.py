from jwt import encode,decode


key_secret:str='MyClaveSecretaEnPython'
def create_token(data:dict):
    token:str=encode(payload=data,key=key_secret,algorithm='HS256')
    return token

def validate_token(token:str)->dict:
    print(token)
    data:dict=decode(token,key=key_secret,algorithms=['HS256'])
    return data