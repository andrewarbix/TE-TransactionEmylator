import hashlib
import json
import random
import time

# Функция для генерации случайных данных транзакции
def generate_transaction_data():
    transaction = {
        "sender": f"address_{random.randint(1, 1000)}",
        "receiver": f"address_{random.randint(1, 1000)}",
        "amount": random.uniform(0.01, 1000.00),
        "timestamp": time.time()
    }
    return transaction

# Функция для хэширования данных транзакции
def hash_transaction(transaction_data):
    transaction_str = json.dumps(transaction_data, sort_keys=True)
    transaction_hash = hashlib.sha256(transaction_str.encode('utf-8')).hexdigest()
    return transaction_hash

# Функция для эмуляции транзакции и формирования блока
def simulate_transaction():
    # Генерация данных транзакции
    transaction_data = generate_transaction_data()
    print(f"Transaction Data: {transaction_data}")
    
    # Хэширование данных
    transaction_hash = hash_transaction(transaction_data)
    print(f"Transaction Hash: {transaction_hash}")
    
    # Эмуляция блока
    block = {
        "previous_block_hash": "previous_block_hash_example",
        "transactions": [transaction_data],
        "block_hash": transaction_hash
    }
    
    print(f"Block: {block}")

# Запуск эмуляции транзакции
simulate_transaction()
