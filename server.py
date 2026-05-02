import socket

# AF_INET: IPv4, SOCK_STREAM: TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Quando você fecha um servidor ou uma conexão TCP termina,
#  o sistema operacional não libera a porta imediatamente.
#  Ele a coloca em um estado chamado TIME_WAIT.
#  O timewait serve para garantir que todos os pacotes relacionados
#  à conexão anterior sejam descartados antes que a porta seja reutilizada.
#  Isso previne que dados antigos sejam acidentalmente enviados para 
#  um novo processo que está usando a mesma porta.
#  A função setsockopt (Set Socket Options) serve para alterar o comportamento padrão do socket.

# socket.SOL_SOCKET -> Aqui estamos dizendo que queremos alterar uma opção
# na camada do próprio Socket (Socket Level), e não em protocolos específicos como o TCP ou IP.

# socket.SO_REUSEADDR -> Ela diz ao kernel do sistema operacional: "Ei, se 
# essa porta estiver no estado TIME_WAIT, pode permitir que eu a use novamente agora mesmo".

# 1 -> O valor 1 (True) é usado para ativar a opção SO_REUSEADDR. 0 significa desativar (False).
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind -> Associa o socket a um endereço específico e porta.
# Passamos a tupla (IP, PORTA)
# localhost -> É o mesmo que usar o endereço IP '127.0.0.1', 
# que é o endereço de loopback para a máquina local.
server.bind(('localhost', 8080))

# Listen -> Coloca o servidor em modo de escuta, aguardando conexões de clientes.
# O número 5 é o backlog, que define o número máximo de conexões pendentes 
# que o servidor pode ter antes de recusar novas conexões.
# Se o servidor estiver ocupado processando uma conexão e outras conexões chegarem, 
# elas serão colocadas nessa fila. Se a fila atingir o limite definido (neste caso, 5), 
# novas conexões serão recusadas até que haja espaço na fila.
server.listen(5)

print("Servidor aguardando conexões em http://127.0.0.1:8080...")

# accept -> Aceita uma conexão de um cliente. 
# Ele bloqueia a execução do programa até que um cliente se conecte.
# Retorna uma tupla (conn, addr):
# conn: É um novo socket que representa a conexão com o cliente.
# addr: É o endereço do cliente, geralmente uma tupla (IP, PORTA).
# O socket de escuta continua livre para ouvir novos "olá" de outros navegadores.
# O socket retornado pelo accept() (o conn) fica dedicado exclusivamente a trocar 
# mensagens com aquele cliente específico.

while True:
  
  client_socket, client_address = server.accept()
  
  print(f"Cliente conectado: {client_address}")
  
  # Por enquanto vamos fechar a conexão imediatamente, 
  # mas aqui é onde se leem dados do cliente.
  client_socket.close()
  