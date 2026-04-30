# 🚀 TODO: Servidor HTTP/1.1 com Socket Persistente

## 🟢 Fase 1: O "Hello World" do TCP

- [ ] **Criar o Socket:** Instanciar `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.
- [ ] **Configurar Reuso de Endereço:** Usar `setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)` para evitar o erro de "Address already in use" ao reiniciar o servidor.
- [ ] **Bind e Listen:** Vincular ao `localhost` na porta `8080` e definir o backlog de conexões.
- [ ] **Loop de Aceitação:** Implementar o `accept()` para receber a conexão do cliente e imprimir o endereço de IP/porta de quem conectou.

## 🟡 Fase 2: Parsing e Protocolo (A Arte do Texto)

- [ ] **Buffer de Recebimento:** Ler os dados usando `recv(4096)` e decodificar para string (UTF-8).
- [ ] **Parser da Request Line:** Extrair o Método (GET/POST), o Path e a Versão do protocolo.
- [ ] **Parser de Headers:** Criar um dicionário para armazenar os headers, parando a leitura no delimitador duplo `\r\n\r\n`.
- [ ] **Gerador de Resposta:** Criar uma função que monte a string de resposta seguindo o padrão:

  ```http
  HTTP/1.1 200 OK
  Content-Type: text/html; charset=utf-8
  Content-Length: <tamanho_do_corpo>

  <html>...</html>
  ```

## 🔴 Fase 3: Persistência (Keep-Alive)

- [ ] **Loop de Conexão Ativa:** Envolver a leitura do socket em um loop `while True` que só quebra se o cliente fechar a conexão ou houver um timeout.
- [ ] **Lógica de Fechamento:**
  - Se o header `Connection: close` estiver presente, fechar após enviar.
  - Se `Connection: keep-alive` (padrão no HTTP/1.1), manter o socket aberto.
- [ ] **Timeout:** Configurar `socket.settimeout(5.0)` para evitar que conexões ociosas travem o servidor para sempre.

## 🔵 Fase 4: Servindo Arquivos Reais

- [ ] **Mapeamento de Arquivos:** Se o path for `/`, buscar `index.html`. Se for `/style.css`, buscar o arquivo CSS.
- [ ] **Tratamento de Erros (404):** Se o arquivo não existir no disco, retornar o status code `404 Not Found` com uma página customizada.
- [ ] **Suporte a Tipos MIME:** Adicionar headers `Content-Type` dinâmicos baseados na extensão do arquivo (.png, .jpg, .js).

## 🟣 Fase 5: Concorrência (Bônus)

- [ ] **Multi-threading:** Usar a biblioteca `threading` para que cada `accept()` gere uma nova thread. Isso permite que o servidor atenda múltiplos navegadores simultaneamente sem que um bloqueie o outro.

---

## 💡 Dica de Implementação

Ao enviar a resposta, lembre-se de converter a string para bytes:

```python
response = "HTTP/1.1 200 OK\r\n\r\nHello World".encode('utf-8')
client_socket.sendall(response)
```

## 📚 Referências

- https://docs.python.org/3/library/socket.html
