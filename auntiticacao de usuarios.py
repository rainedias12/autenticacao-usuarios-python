import datetime # Importa o módulo datetime para obter a data atual

class DataBase:
  """
  Uma classe para gerenciar usuários em um arquivo de texto simples.
  Cada linha do arquivo representa um usuário no formato: email;senha;nome;data_criacao
  """
  def __init__(self, filename):
      """
      Inicializa a instância do DataBase.
      :param filename: O nome do arquivo onde os dados do usuário serão armazenados.
      """
      self.filename = filename
      self.users = {} # Dicionário para armazenar usuários (email: (senha, nome, data_criacao))
      self.load() # Carrega os usuários do arquivo ao inicializar

  def load(self):
      """
      Carrega os dados dos usuários do arquivo especificado.
      Se o arquivo não existir, ele será criado.
      """
      try:
          with open(self.filename, "r") as f: # Abre o arquivo em modo de leitura
              for line in f:
                  # Remove espaços em branco e divide a linha por ';'
                  email, password, name, created = line.strip().split(";")
                  # Armazena os dados do usuário no dicionário
                  self.users[email] = (password, name, created)
      except FileNotFoundError:
          # Se o arquivo não existir, cria um arquivo vazio
          with open(self.filename, "w") as f:
              pass # Apenas cria o arquivo e o fecha

  def get_user(self, email):
      """
      Retorna as informações de um usuário pelo email.
      :param email: O email do usuário a ser buscado.
      :return: Uma tupla (senha, nome, data_criacao) se o usuário existir,
               ou -1 se o usuário não for encontrado.
      """
      if email in self.users:
          return self.users[email]
      else:
          return -1

  def add_user(self, email, password, name):
      """
      Adiciona um novo usuário ao banco de dados.
      :param email: O email do novo usuário.
      :param password: A senha do novo usuário.
      :param name: O nome do novo usuário.
      :return: 1 se o usuário foi adicionado com sucesso, -1 se o email já existe.
      """
      if email.strip() not in self.users:
          # Adiciona o novo usuário com a data de criação atual
          self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
          self.save() # Salva as alterações no arquivo
          return 1
      else:
          print("Email exists already")
          return -1

  def validate(self, email, password):
      """
      Valida as credenciais de um usuário.
      :param email: O email do usuário.
      :param password: A senha fornecida.
      :return: True se o email e a senha correspondem, False caso contrário.
      """
      if self.get_user(email) != -1:
          # Compara a senha fornecida com a senha armazenada (primeiro elemento da tupla)
          return self.users[email][0] == password
      else:
          return False

  def save(self):
      """
      Salva todos os dados dos usuários atualmente no dicionário 'users' de volta ao arquivo.
      Sobrescreve o conteúdo existente do arquivo.
      """
      with open(self.filename, "w") as f: # Abre o arquivo em modo de escrita (sobrescreve)
          for email, user_data in self.users.items():
              # user_data é uma tupla: (password, name, created)
              # Constrói a linha no formato "email;senha;nome;data_criacao"
              f.write(f"{email};{user_data[0]};{user_data[1]};{user_data[2]}\n")

  @staticmethod
  def get_date():
      """
      Retorna a data atual no formato "YYYY-MM-DD".
      :return: Uma string representando a data atual.
      """
      return str(datetime.datetime.now()).split(" ")[0]

# Exemplo de uso da classe DataBase (opcional, para testar)
if __name__ == "__main__":
    db = DataBase("users.txt") # Cria uma instância do banco de dados

    # Adicionando alguns usuários
    print(f"Adicionando usuario1@example.com: {db.add_user('usuario1@example.com', 'senha123', 'Usuario Um')}")
    print(f"Adicionando usuario2@example.com: {db.add_user('usuario2@example.com', 'abc456', 'Usuario Dois')}")
    print(f"Tentando adicionar usuario1@example.com novamente: {db.add_user('usuario1@example.com', 'nova_senha', 'Usuario Um')}")

    # Validando usuários
    print(f"Validando usuario1@example.com com senha correta: {db.validate('usuario1@example.com', 'senha123')}")
    print(f"Validando usuario1@example.com com senha incorreta: {db.validate('usuario1@example.com', 'errada')}")
    print(f"Validando usuario_inexistente@example.com: {db.validate('usuario_inexistente@example.com', 'qualquer')}")

    # Obtendo informações de um usuário
    user_info = db.get_user('usuario2@example.com')
    if user_info != -1:
        print(f"Informações de usuario2@example.com: Senha={user_info[0]}, Nome={user_info[1]}, Criado={user_info[2]}")
    else:
        print("Usuario2 não encontrado.")

    # Você pode verificar o arquivo 'users.txt' após executar este script.