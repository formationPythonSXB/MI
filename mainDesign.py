from channel import Channel
from user import User
from video import Video

arte=Channel("ARTE")
cestpassorcier=Channel("c'est pas sorcier")
videodechat=Channel("video de chat")

alice=User("alice")
bob=User("bob")
charlie=User("charlie")

arte.subscribe(alice)
cestpassorcier.subscribe(alice)
cestpassorcier.subscribe(bob)
videodechat.subscribe(bob)
videodechat.subscribe(charlie)

cestpassorcier.publish(Video("Le système solaire"))
arte.publish(Video("La grenouille, un animal extraordinaire"))
cestpassorcier.publish(Video("Le génie des fourmis"))
videodechat.publish(Video("Video de chat qui fait miaou"))
cestpassorcier.publish(Video("Les chateaux forts"))