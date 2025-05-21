from abc import ABC, abstractmethod
from datetime import datetime

# Apenas exibe resultados não envia

# Base para Mensagens
class Mensagem(ABC):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    @abstractmethod
    def formatar(self):
        pass

# Tipos de mensagens
class TextoMensagem(Mensagem):
    def __init__(self, conteudo, data_envio=None):
        super().__init__(conteudo)
        self.data_envio = data_envio or datetime.now()

    def formatar(self):
        return f"[Texto] {self.data_envio.strftime('%Y-%m-%d %H:%M:%S')} - {self.conteudo}"

class VideoMensagem(Mensagem):
    def __init__(self, conteudo, arquivo, formato, duracao):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao

    def formatar(self):
        return f"[Vídeo] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}, Duração: {self.duracao}s"

class FotoMensagem(Mensagem):
    def __init__(self, conteudo, arquivo, formato):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

    def formatar(self):
        return f"[Foto] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}"

class ArquivoMensagem(Mensagem):
    def __init__(self, conteudo, arquivo, formato):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

    def formatar(self):
        return f"[Arquivo] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}"

# Base para Canais
class Canal(ABC):
    def __init__(self, identificador):
        self.identificador = identificador

    @abstractmethod
    def enviar_mensagem(self, mensagem: Mensagem):
        pass

# Implementação dos canais
class WhatsApp(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[WhatsApp - {self.identificador}] {mensagem.formatar()}")

class Telegram(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[Telegram - {self.identificador}] {mensagem.formatar()}")

class Facebook(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[Facebook - {self.identificador}] {mensagem.formatar()}")

class Instagram(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[Instagram - {self.identificador}] {mensagem.formatar()}")

# Demonstração
if __name__ == "__main__":
    # Criando canais
    whatsapp = WhatsApp("+55999999999")
    telegram_tel = Telegram("+55888888888")
    telegram_user = Telegram("@pedro_bot")
    facebook = Facebook("pedro.fb")
    instagram = Instagram("pedro.ig")

    # Criando mensagens
    texto = TextoMensagem("Olá, isso é uma mensagem de texto.")
    video = VideoMensagem("Vídeo importante", "video.mp4", "mp4", 120)
    foto = FotoMensagem("Foto de perfil", "foto.jpg", "jpg")
    arquivo = ArquivoMensagem("Documento PDF", "arquivo.pdf", "pdf")

    # Enviando mensagens
    whatsapp.enviar_mensagem(texto)
    telegram_tel.enviar_mensagem(video)
    telegram_user.enviar_mensagem(foto)
    facebook.enviar_mensagem(arquivo)
    instagram.enviar_mensagem(texto)
