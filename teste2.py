from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

# Apenas exibe resultados não envia
# Falta comentar o código

# Base para Mensagens
class Mensagem(ABC):
    def __init__(self, conteudo: str):
        self.conteudo = conteudo

    @abstractmethod
    def formatar(self) -> str:
        pass

# Classe intermediária para mensagens com arquivos
class MensagemComArquivo(Mensagem):
    def __init__(self, conteudo: str, arquivo: str, formato: str):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

# Tipos de mensagens
class TextoMensagem(Mensagem):
    def __init__(self, conteudo: str, data_envio: Optional[datetime] = None):
        super().__init__(conteudo)
        self.data_envio = data_envio or datetime.now()

    def formatar(self) -> str:
        return f"[Texto] {self.data_envio.strftime('%Y-%m-%d %H:%M:%S')} - {self.conteudo}"

class VideoMensagem(Mensagem):
    def __init__(self, conteudo, arquivo, formato, duracao):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao

    def formatar(self):
        minutos = self.duracao // 60
        segundos = self.duracao % 60
        return f"[Vídeo] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}, Duração: {minutos}m {segundos}s"


class FotoMensagem(MensagemComArquivo):
    def formatar(self) -> str:
        return f"[Foto] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}"

class ArquivoMensagem(MensagemComArquivo):
    def formatar(self) -> str:
        return f"[Arquivo] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}"

# Base para Canais
class Canal(ABC):
    def __init__(self, identificador: str):
        self.identificador = identificador

    @abstractmethod
    def enviar_mensagem(self, mensagem: Mensagem) -> None:
        pass

# Implementação dos canais
class WhatsApp(Canal):
    def enviar_mensagem(self, mensagem: Mensagem) -> None:
        print(f"[WhatsApp - {self.identificador}] {mensagem.formatar()}")

class Telegram(Canal):
    def enviar_mensagem(self, mensagem: Mensagem) -> None:
        print(f"[Telegram - {self.identificador}] {mensagem.formatar()}")

class Facebook(Canal):
    def enviar_mensagem(self, mensagem: Mensagem) -> None:
        print(f"[Facebook - {self.identificador}] {mensagem.formatar()}")

class Instagram(Canal):
    def enviar_mensagem(self, mensagem: Mensagem) -> None:
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
    video = VideoMensagem("Vídeo importante", "video.mp4", "mp4", 125)
    foto = FotoMensagem("Foto de perfil", "foto.jpg", "jpg")
    arquivo = ArquivoMensagem("Documento PDF", "arquivo.pdf", "pdf")

    # Enviando mensagens
    whatsapp.enviar_mensagem(texto)
    telegram_tel.enviar_mensagem(video)
    telegram_user.enviar_mensagem(foto)
    facebook.enviar_mensagem(arquivo)
    instagram.enviar_mensagem(texto)
