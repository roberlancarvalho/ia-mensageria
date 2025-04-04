from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'topico-ia',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='grupo-ia',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("IA2 aguardando mensagens...")

for message in consumer:
    msg = message.value
    print(f"IA2 recebeu: {msg}")

    texto = msg["texto"].lower()
    if "excelente" in texto or "ótimo" in texto:
        print("Classificação: Positiva")
    elif "demorou" in texto or "problema" in texto:
        print("Classificação: Negativa")
    else:
        print("Classificação: Neutra")
