# test-rabbitmq_mongo_app

# 📂 Estrutura de diretórios

```
├── docker-compose.yml
├── api/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── worker/
│   ├── Dockerfile
│   ├── worker.py
│   └── requirements.txt
```

# Comandos docker

### ▶️ Como rodar
* docker-compose up --build

Acesse a API → http://localhost:8000/docs
Envie uma requisição POST /send/ com corpo:

```
{
  "user": "bruno",
  "msg": "olá do FastAPI!"
}
```
### MongoDB

Veja o worker consumindo e salvando no MongoDB.

Acesse o painel Mongo Express → http://localhost:8081

Banco: testdb → coleção: messages.
