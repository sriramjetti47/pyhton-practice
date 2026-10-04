
running = True
while running :
      user_name = input("enter username :")
      if user_name != "sriram":
          print("enter valid name")
          continue

      while running :
            password = input('enter your password: ')
            if password != 'don':
                print('wrong password')
                continue
            print('login succesfull')
            break
      continue

































