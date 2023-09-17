# - attributes: power
# - behavior:
#     play_game(duration): 1% per 1 minutes (1% per minute)
#     coding(duration): 1% per 10 minute (0,1% per minute )
#     browsing(duration): 2% per 10 minutes (0,2% per minute)
#     play_audio(duration): 5% per 10 minutes (0,5% per minute)
#     charge(duration): 1% per minute

class Laptop :
    #attributes
    def __init__(self,initialbatrey=0): #nilaidefaultbatrey = 0
        self.power= initialbatrey
        print(f'batreynya {self.power} %, abis perlu di charge')
    
    #methods
    def charging(self, duration=1): # + 1% per minute
        self.power += duration 
        if self.power > 100 :
            self.power = 100
        print(f'habis dicharging {duration} menit, batreynya jadi {self.power} %')
    
    def playing_game(self, duration): # - 1% per 10 minute
        consumption_playing_game=1* duration / 10
        self.power -= consumption_playing_game
        if self.power <= 0 :
            self.power=0
            print(f'udah habis batrey , charge dulu, istirahat')
        print(f'habis dibuat main game {duration} menit, sisa segini kan {self.power} % batreynya')
    
    def browsing(self, duration): # 2% per 10 minutes
        consumption_browsing=2* duration / 10
        self.power -= consumption_browsing
        if self.power <= 0 :
            self.power = 0
            print(f'udah habis batrey , charge dulu, istirahat')
        print(f'habis dibuat browsing {duration} menit, sisa segini kan {self.power} % batreynya')
    
    def coding(self, duration): # 1% per 10 minutes
        consumption_coding=1* duration / 10
        self.power -= consumption_coding
        if self.power <= 0 :
            self.power = 0
            print(f'udah habis batrey , charge dulu, istirahat')
        print(f'habis dibuat coding {duration} menit, sisa segini kan {self.power} % batreynya')
    
    def playing_audio(self, duration): # 5% per 10 minutes
        consumption_playing_audio=5* duration / 10
        self.power -= consumption_playing_audio
        if self.power <= 0 :
            self.power = 0
            print(f'udah habis batrey , charge dulu, istirahat')
        print(f'habis dibuat muter lagu {duration} menit, sisa segini kan {self.power} % batreynya')

laptop_sherly=Laptop()
#charge 2 hours
laptop_sherly.charging(120)
# playing game 1 hour
laptop_sherly.playing_game(60)
# browsing 1 hour
laptop_sherly.browsing(60)
#charge 20 minutes
laptop_sherly.charging(20)
#coding 2 hours
laptop_sherly.coding(120)
#play audio 2 hours
laptop_sherly.playing_audio(120)