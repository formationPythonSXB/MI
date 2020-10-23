class User:
    
    def __init__(self,nom):
        self.nom=nom
        self.videos = []
        
    def __repr__(self):
        return ("User : " + self.nom)
    
    def actualiser(self):
        
        with open("videos_" + self.nom,"w") as fw :
            for video in self.videos : fw.write(str(video)+"\n")