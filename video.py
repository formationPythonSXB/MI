from datetime import datetime

class Video:
    
    def __init__(self,titre):
        self.titre=titre
        self.datePubli = datetime.now()
        
    def __repr__(self):
        return ("Video : " + self.titre)