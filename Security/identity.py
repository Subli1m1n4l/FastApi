import models.identity.User as us
import Security.Token.jwt_manager as jwt



identities:dict=[
    {
        'userAdmin':'johan.ageof@gmail.com',
        'passwordAdmin':'12345'
    },
    {
        'userAdmin':'pruebas@gmail.com',
        'passwordAdmin':'aaa12546'
    }
]
def valid_user(user:us.User) -> bool:
    identity:list=[item for item in identities if item["userAdmin"]==user.email and item["passwordAdmin"]== user.password]
    if len(identity) > 0:
        return True
    else:
        return False
    
    
def get_token(user:us.User) -> str:
    token=jwt.create_token(user.model_dump())
    return token

