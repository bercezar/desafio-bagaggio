# 🚀 Desafio Técnico - API de Usuários - RESOLVIDO

## 📖 Contexto

Recentemente, um dos desenvolvedores da equipe recebeu a missão de criar uma API para gerenciamento de usuários.

O projeto foi entregue e já está funcionando, mas existe um detalhe: era a primeira vez que esse desenvolvedor trabalhava sozinho em uma API desse porte. 😅

Como acontece em muitos projetos reais, a aplicação evoluiu, algumas decisões foram tomadas com pressa, outras poderiam ter sido melhor planejadas e alguns pontos acabaram ficando para trás durante o desenvolvimento.

Agora você recebeu a responsabilidade de assumir essa base de código.

Sua missão não é reescrever tudo do zero.

Queremos entender como você investiga uma aplicação existente, identifica oportunidades de melhoria e realiza ajustes que deixem o projeto mais confiável, organizado e fácil de manter.

---

## 🎯 Objetivo

Analise a API existente e faça as melhorias que considerar necessárias.

Não existe uma lista fechada de problemas para corrigir.

Queremos observar como você explora a aplicação, interpreta o código e toma decisões técnicas para evoluir o projeto.

Pense como alguém que acabou de entrar em uma equipe e recebeu a tarefa de dar continuidade a um sistema já em produção.

---

## 🤖 Uso de Inteligência Artificial

O uso de ferramentas de IA é permitido.

No entanto, durante a avaliação, você poderá ser questionado sobre as alterações realizadas.

Por isso, é importante compreender e conseguir explicar as decisões tomadas ao longo do desenvolvimento.

---

## ▶️ Como Executar o Projeto

### Criar ambiente virtual

```bash
python -m venv .venv
```

### Ativar ambiente virtual

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/MacOS**

```bash
source .venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Inicializar banco de dados

```bash
python database/seed.py
```

### Executar a API

```bash
uvicorn main:app --reload
```

### Documentação

```text
http://localhost:8000/api/users/docs
```

---

## 📌 Endpoints Disponíveis

- `POST /users/`
- `GET /users/`
- `GET /users/{user_id}`
- `PATCH /users/{user_id}`
- `DELETE /users/{user_id}`

---

## 📦 O Que Esperamos na Entrega

Sua entrega deve conter:

- Código atualizado;
- Melhorias que você considerar relevantes;
- Instruções para execução do projeto;
- Explicação das alterações realizadas;
- Justificativas para decisões importantes;

---

## 📝 Importante

Não buscamos uma solução perfeita.

O objetivo deste desafio é entender como você trabalha com uma base de código existente, como investiga problemas, organiza suas ideias e evolui uma aplicação de forma incremental.

Explique suas decisões, documente seu raciocínio e sinta-se à vontade para apontar pontos que você optou por não alterar.

Boa sorte! 🍀
