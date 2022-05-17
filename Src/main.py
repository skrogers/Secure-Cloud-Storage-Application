import googleDriveAPI
import users
import menuTypes
import encryption
import eel

eel.init('web')

loop = False


def main():
    
    print("starting")       #prints starting on the terminal
    global loop
   
    u = users

    try:
        
        while True:
            
            if(u.status == 1):          #user status is confirmed
                eel.loginSuccess()          #js func
                
                if(u.privilege == True):        #if privilege value is true, open privilege menu
                    eel.privMenu()
                    
                    while True:
                        
                        if not loop:
                            eel.sleep(1)        #sleep timer of one second
                        
                        else:
                            loop = False
                            break
                

                else:               #if not admin menu, give standard menu
                    eel.standardMenu()
                    
                    while True:
                        
                        if not loop:
                            eel.sleep(1)
                        else:
                            loop = False
                            break
            
            elif(u.status == -1):
                eel.loginTry()
                  

            eel.sleep(1)      
    
    except Exception:
        pass


@eel.expose
def loopBreak():
    global loop 
    loop = True

@eel.expose
def printToConsole(string):
    print(string)

eel.start('index.html', block=False)
if __name__ == '__main__':
    main()