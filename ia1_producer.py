from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

mensagens = [
    {"id": 1, "texto": "O atendimento foi excelente!"},
    {"id": 2, "texto": "A consulta demorou demais e não resolveu meu problema."}
]

for msg in mensagens:
    print(f"IA1 enviando: {msg}")
    producer.send("topico-ia", msg)
    time.sleep(1)

producer.flush()
