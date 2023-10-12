# Task Manager - Python + Django + Docker
Aplicação backend desenvolvida com tecnologias modernas e práticas de desenvolvimento, como Python, Django e Docker, para oferecer um sistema de gerenciamento de tarefas eficiente e escalável.

Tecnologias Utilizadas

Django==4.2.6
asgiref==3.7.2
django-cors-headers==4.2.0
django-filter==23.3
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.0
gunicorn==21.2.0
Markdown==3.5
mysqlclient==2.2.0
packaging==23.2
PyJWT==2.8.0
python-decouple==3.8
pytz==2023.3.post1
setuptools==68.1.2
sqlparse==0.4.4



Deployment
[Api Task](https://backend-task-manager-django-production.up.railway.app/api)


Repositório Frontend
[Task Manager Frontend](https://github.com/RafaelCardoso11/frontend-task-manager-reactJS)

É possível no projeto:
1) Adicionar novas tarefas (Create)
2) Visualizar novas tarefas (List and ReadOne)
3) Editar tarefas (Update)
4) Marcar como concluída as tarefas (Completion)
5) Login / Registro


## Inicialização do Projeto (Produção)

### Pré-requisitos

Certifique-se de que você tenha o docker instalado em sua máquina.

```bash
docker -v
```

### Inicialização
1. **Navegue para a pasta do projeto:** Use o comando `cd` para entrar na pasta do projeto onde está localizado o arquivo `docker-compose.yml`.

```bash
cd caminho-para-o-seu-projeto
```
3. **Configure as variáveis de ambiente**
 `exemplo em .env.example`
2. **Suba os containers**
```bash
docker-compose up 
```


``Python ``
``Django ``
``Django rest framework ``
``Django simple jwt ``

Qualquer dúvida estou a disposição.