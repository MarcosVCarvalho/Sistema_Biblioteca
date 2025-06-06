from datetime import datetime

# Função para obter a data do usuário
def obter_data_usuario():
    while True:
        data_str = input("Digite a data no formato DD-MM-AAAA: ")
        try:
            # Tenta converter a string em um objeto de data
            data = datetime.strptime(data_str, "%d-%m-%Y")
            return data  # Retorna o objeto de data se a conversão for bem-sucedida
        except ValueError:
            print("Formato inválido. Por favor, digite a data no formato DD-MM-AAAA.")

# Exemplo de uso
data_usuario = obter_data_usuario()
print("Data informada:", data_usuario.strftime("%d-%m-%Y"))
