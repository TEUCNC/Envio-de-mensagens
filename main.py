from abc import ABC, abstractmethod
from datetime import datetime

## Funcional

# ========================
# CLASSES DE MENSAGEM
# ========================

# Classe base abstrata para qualquer tipo de mensagem
class Mensagem(ABC):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def formatar(self):
        pass

# Classe para mensagens de texto
class TextoMensagem(Mensagem):
    def __init__(self, conteudo, data_envio=None):
        super().__init__(conteudo)
        # Se não for passada data, usa o momento atual
        self.data_envio = data_envio or datetime.now()

    def formatar(self):
        return f"[Texto] {self.data_envio.strftime('%Y-%m-%d %H:%M:%S')} - {self.conteudo}"

# Classe para mensagens de vídeo
class VideoMensagem(Mensagem):
    def __init__(self, conteudo, arquivo, formato, duracao):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao  # em segundos

    def formatar(self):
        minutos = self.duracao // 60
        segundos = self.duracao % 60
        return f"[Vídeo] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}, Duração: {minutos}m {segundos}s"

# Classe para mensagens com fotos
class FotoMensagem(Mensagem):
    def __init__(self, conteudo, arquivo, formato):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

    def formatar(self):
        return f"[Foto] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}"

# Classe para mensagens com arquivos em geral
class ArquivoMensagem(Mensagem):
    def __init__(self, conteudo, arquivo, formato):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

    def formatar(self):
        return f"[Arquivo] {self.conteudo} - Arquivo: {self.arquivo}, Formato: {self.formato}"

# ========================
# CLASSES DE CANAIS
# ========================

# Classe base abstrata para qualquer canal de comunicação
class Canal(ABC):
    def __init__(self, identificador):
        self.identificador = identificador  # número de telefone ou usuário

    @abstractmethod
    def enviar_mensagem(self, mensagem: Mensagem):
        pass

# Canal WhatsApp
class WhatsApp(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[WhatsApp - {self.identificador}] {mensagem.formatar()}")

# Canal Telegram
class Telegram(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[Telegram - {self.identificador}] {mensagem.formatar()}")

# Canal Facebook
class Facebook(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[Facebook - {self.identificador}] {mensagem.formatar()}")

# Canal Instagram
class Instagram(Canal):
    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"[Instagram - {self.identificador}] {mensagem.formatar()}")

# ========================
# FUNÇÃO PRINCIPAL (CLI)
# ========================

def main():
    print("Bem-vindo ao sistema de envio de mensagens!\n")

    # Dicionário de opções de canais disponíveis
    canais = {
        "1": ("WhatsApp", WhatsApp),
        "2": ("Telegram", Telegram),
        "3": ("Facebook", Facebook),
        "4": ("Instagram", Instagram)
    }

    # Tipos de mensagem disponíveis
    mensagens = {
        "1": "Texto",
        "2": "Vídeo",
        "3": "Foto",
        "4": "Arquivo"
    }

    while True:
        # Escolher canal
        print("\nEscolha um canal:")
        for key, (nome, _) in canais.items():
            print(f"{key} - {nome}")
        canal_opcao = input("Opção: ").strip()

        if canal_opcao not in canais:
            print("Canal inválido. Tente novamente.")
            continue

        canal_nome, canal_classe = canais[canal_opcao]
        identificador = input(f"Digite o {'número de telefone' if canal_nome in ['WhatsApp', 'Telegram'] else 'nome de usuário'}: ")
        canal = canal_classe(identificador)

        # Escolher tipo de mensagem
        print("\nEscolha o tipo de mensagem:")
        for key, tipo in mensagens.items():
            print(f"{key} - {tipo}")
        msg_opcao = input("Opção: ").strip()

        if msg_opcao not in mensagens:
            print("Tipo de mensagem inválido. Tente novamente.")
            continue

        # Conteúdo comum a todas as mensagens
        conteudo = input("Digite o conteúdo da mensagem: ")

        # Coleta os dados específicos para cada tipo de mensagem
        if msg_opcao == "1":
            msg = TextoMensagem(conteudo)
        elif msg_opcao == "2":
            arquivo = input("Nome do arquivo de vídeo: ")
            formato = input("Formato do vídeo (ex: mp4): ")
            duracao = int(input("Duração do vídeo (em segundos): "))
            msg = VideoMensagem(conteudo, arquivo, formato, duracao)
        elif msg_opcao == "3":
            arquivo = input("Nome do arquivo da foto: ")
            formato = input("Formato da foto (ex: jpg): ")
            msg = FotoMensagem(conteudo, arquivo, formato)
        elif msg_opcao == "4":
            arquivo = input("Nome do arquivo: ")
            formato = input("Formato do arquivo (ex: pdf): ")
            msg = ArquivoMensagem(conteudo, arquivo, formato)

        # Envia (simulado com print)
        print("\nEnviando mensagem...")
        canal.enviar_mensagem(msg)

        # Pergunta se deseja continuar
        continuar = input("\nDeseja enviar outra mensagem? (s/n): ").lower()
        if continuar != 's':
            break

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
