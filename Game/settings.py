class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""

        #Configurações da tela
        self.screen_width = 1200 #Tamanho da tela
        self.screen_height = 800    #Tamanho da tela
        self.bg_color = (230, 230, 230) #background color

        #Configurações da nave
        self.ship_speed_factor = 1.5 #Velocidade da nave (pixels por clique)

        #Configurações dos projéteis
        self.bullet_speed_factor = 1 #Velocidade projétil
        self.bullet_width = 3   #Largura tiro
        self.bullet_height = 15 #Altura tiro
        self.bullet_color = 60, 60, 60  #Cor do tiro
        self.bullets_allowed = 3    #Limite de tiros