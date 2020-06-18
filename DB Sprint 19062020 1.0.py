import random
class main:
    def generate(self):
        pw = ''
        #random.SystemRandom.choice(string) does not work, TypeError: choice() missing 1 required positional argument: 'seq'
        for i in range(12):
            pw = pw + random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+§-=[];\,./{}:"|<>?')
        print ('Your new secure password is:  ' + pw)                            
run = main()
run.generate()
