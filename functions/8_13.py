def build_profile(first, last, **user_info):
    """Cosntrói um dicionário contendo tudo que sabemos sobre um usuário"""
    profile={}
    
    profile['first_name']=first
    profile['last_name']=last
    
    for key,value in user_info.items():
        profile[key]=value
    
    return profile

user_profile = build_profile('Bruno','Pires',location = 'Joinville', age= '19', height='190cm')
print(user_profile)
    