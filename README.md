# Comunicação entre IAs com Apache Kafka 🧠🛰️

Este repositório demonstra como duas aplicações Python simulando inteligências artificiais podem se comunicar entre si de forma assíncrona usando Apache Kafka. Todo o ambiente é configurado com Docker Compose e o código está organizado para ser simples e didático.

---

## 🧩 Tecnologias utilizadas

- [Python 3.12](https://www.python.org/)
- [Apache Kafka 3.4.0](https://kafka.apache.org/)
- [Kafka-Python](https://pypi.org/project/kafka-python/)
- [Docker + Docker Compose](https://docs.docker.com/)
- VS Code + Git Bash ou PowerShell

---

## 📁 Estrutura do projeto

```
.
├── docker-compose.yml          # Define os serviços Kafka e Zookeeper
├── ia1_producer.py             # Script produtor (IA que envia mensagens)
├── ia2_consumer.py             # Script consumidor (IA que interpreta as mensagens)
├── requirements.txt            # Dependências Python
└── README.md                   # Este arquivo
```

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/kafka-ai-comms.git
cd kafka-ai-comms
```

### 2. Suba o ambiente Kafka + Zookeeper
```bash
docker compose up -d
```

### 3. Crie o tópico Kafka
```bash
docker exec kafka kafka-topics.sh --create --topic topico-ia --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 4. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/Scripts/activate  # PowerShell: .\venv\Scripts\Activate
pip install -r requirements.txt
```

### 5. Rode os scripts

Em dois terminais diferentes:

**Terminal 1: Consumidor (IA2)**

```bash
python ia2_consumer.py
```

**Terminal 2: Produtor (IA1)**

```bash
python ia1_producer.py
```

Você verá as mensagens sendo enviadas e classificadas em tempo real! 🎯

---

## 🧠 Possíveis evoluções

- Integração com modelos reais de IA via Hugging Face (Transformers)
- Persistência em banco de dados (PostgreSQL ou MongoDB)
- Exposição via API com FastAPI
- Dashboard de visualização de mensagens em tempo real

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

Desenvolvido por [Roberlan Carvalho](https://www.roberlancarvalho.com)