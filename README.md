# Sistema de Gerência de Estoque/Almoxarifado

Um sistema web para controlar a movimentação de itens, equipamentos e empréstimos em almoxarifados.

## 🚀 Como Este Projeto Foi Criado

### 1. Instalação do Django
```bash
pip install django
django-admin startproject setup .
```

### 2. Criação dos Apps (Módulos)
```bash
python manage.py startapp core         # Autenticação e login
python manage.py startapp equipamentos # Gerenciamento de EPIs
python manage.py startapp emprestimos  # Controle de empréstimos
python manage.py startapp colaboradores # Cadastro de usuários
python manage.py startapp historico    # Log de movimentações
python manage.py startapp relatorios   # Geração de relatórios
python manage.py startapp dashboard    # Página inicial
```

### 3. Configuração Inicial
- Adicionou os apps ao `INSTALLED_APPS` em `setup/settings.py`
- Criou modelos de dados em cada app (`models.py`)
- Configurou rotas em cada app (`urls.py`)
- Criou views para renderizar pages (`views.py`)

### 4. Interface (Frontend)
- Templates HTML em `/templates/` para cada página
- Estilos CSS em `/static/css/`
- Assets estáticos em `/static/`

---

## 📋 Requisitos

- Python 3.8+
- Django 3.2+

---

## ⚙️ Como Executar Localmente

1. **Clone o repositório:**
```bash
git clone <url-do-repo>
cd sistema-epi-gabrielgv13
```

2. **Instale as dependências:**
```bash
pip install django
```

3. **Execute as migrações:**
```bash
python manage.py migrate
```

4. **Inicie o servidor:**
```bash
python manage.py runserver
```

5. **Acesse em seu navegador:**
```
http://localhost:8000
```

---

## 📁 Estrutura de Pastas

```
projeto/
├── setup/              # Configurações principais do Django
├── core/               # App de autenticação
├── equipamentos/       # Cadastro de EPIs
├── emprestimos/        # Controle de empréstimos
├── colaboradores/      # Gerencia usuários
├── historico/          # Log de movimentações
├── relatorios/         # Relatórios
├── dashboard/          # Dashboard
├── templates/          # Páginas HTML
├── static/             # CSS, JS, imagens
├── manage.py           # Comando principal Django
└── db.sqlite3          # Banco de dados
```

---

## 🔧 Processo de Desenvolvimento

### Adicionar Novo Modelo
1. Edite `models.py` no respectivo app
2. Execute: `python manage.py makemigrations`
3. Execute: `python manage.py migrate`

### Adicionar Nova Página
1. Crie uma função view em `views.py`
2. Defina a rota em `urls.py`
3. Crie o template em `/templates/`

### Registrar no Admin
Adicione seus modelos ao arquivo `admin.py` para gerenciar via painel administrativo.

---

## ✨ Funcionalidades Principales

- ✅ Autenticação de usuários
- ✅ Cadastro de equipamentos
- ✅ Controle de empréstimos
- ✅ Histórico de movimentações
- ✅ Relatórios de estoque
- ✅ Painel administrativo

---

## 📝 Próximos Passos

- Adicionar testes unitários
- Melhorar interface visual
