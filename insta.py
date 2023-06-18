from instabot import Bot

bot = Bot()


user_name = input("enter username: ")
passw = input("enter password: ")
bot.login(username = user_name, password = passw)

name = input("enter username of person you want to follow")
bot.follow(name)

def follow(person):
    bot.follow(person)

print("Type Y if you want to follow someone")
ask = input("Type Y if you want to follow someone: ", )
if (ask == "Y" or ask == "y"):
    print("enter username of person you want to follow")
    name = input("Enter username of person you want to follow ")
    follow(name)

# bot.upload_photo('give the path',caption = "give the caption you want")

# bot.unfollow(username)

bot.send_message('I love python', "username")
