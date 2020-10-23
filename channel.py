class Channel:
    
    def __init__(self,nom):
        self.nom=nom
        self.users = []
        self.videos = []
        
    def __repr__(self):
        return ("Channel : " + self.nom)
        
    def subscribe(self,user):
        if user not in self.users:
            self.users.append(user)
            for video in self.videos: user.videos.append(video)
        
    def unsubscribe(self,user):
        if user in self.users:
            self.users.remove(user)
            for video in self.videos: user.videos.remove(video)
        
    def notifySuscribers(self,video):
        for user in self.users :
            user.videos.append(video)
            user.actualiser()
        
    def publish(self,video):
        if video not in self.videos:
            self.videos.append(video)
            self.notifySuscribers(video)