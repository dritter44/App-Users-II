# your improved User class goes here



class User:
    
    user_posts = {}
    # user_posts = {'alice':['str1','str2','str3'],
    #                'carrol':['str1','str2']}
    
    def __init__(self,name,email_address,Dr_Lic_Num):
        self.name = name
        self.email_address = email_address
        self.Dr_Lic_Num = Dr_Lic_Num
        self.user_post = []

    
    def __str__(self):
        return f"{self.name} has email {self.email_address} and license # {self.Dr_Lic_Num}."

    #def the new user post method
    
    def update_user_post(self, user_post):
        self.user_post.append(user_post)
        User.user_posts[self.name] = self.user_post
        # print(self.name,'this is self')

    def delete_user_post(self, user_post):
        user_post_list =[]
        for value in User.user_posts[self.name]:
            if value != user_post:
                user_post_list.append(value)
        User.user_posts[self.name] = user_post_list
        self.user_post = user_post_list

        

#sample new user post 'Hello! Excited to be on this app!'

alice = User('Alice', 'alice.doe@gmail.com','asdfjkl;')
bob = User('Bob','bob.smith@mail.mil','qwrttty')
carrol = User('Carrol','carrol.johnson@att.com', 'zxcvnm,')

alice.update_user_post('1st')
alice.update_user_post('2nd')
#print(alice,'\n',bob,'\n',carrol)
print(alice.user_post)
print(User.user_posts)
alice.delete_user_post('2nd')
print(User.user_posts)
print(alice.user_post)

# d = {}
# d['key'] = 'str'
# print(d)