class HighscoreDict(dict):
    def __init__(self,**kwargs):
        super(HighscoreDict,self).__init__(**kwargs)
        for i in range(1,11):
            self[str(i)]=('Kivyator',30)              
    
    def put(self,val):
        key=None
        for i in range(1,11):
            if self[str(i)][1]<=val[1]:
                key=i
                break
        
        if key is not None:
            for i in reversed(range(1,11)):            
                if i > key:
                    self[str(i)]=self[str(i-1)]
                else:
                    self[str(i)]=(val[0],val[1])
                    break

