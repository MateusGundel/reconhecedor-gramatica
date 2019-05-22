# Reconhecedor-gramatica
Trabalho desenvolvido para a discipla de Linguagens Formais da UNISC

## Como executar
 Na pasta do projeto executar os seguintes comandos

#### cria container
```docker build -t django:0.0.0 . --no-cache=true```

#### executa o container
```docker run -it --rm -p 8000:8000 -v ${PWD}:/webapps django:0.0.0 /bin/bash```

#### rodar o server
```python manage.py runserver 0.0.0.0:8000```

E basta acessar [o endereço](localhost:8000) na sua máquina

