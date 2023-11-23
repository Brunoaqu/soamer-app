import json
import random
from faker import Faker

def build_data(SIZE):
  """
  Create fake data for testing
  """
  fake = Faker()
  production_orders = []

  for _ in range(SIZE):
    code = random.randint(1000000000, 9999999999)
    production_order = {
        "project": { "key": "PRJ" },                                                  # Meta
        "issuetype": { "name": "order_de_producao" },                                 # Meta
        "description": fake.text(max_nb_chars=200),                                   # Meta
        "summary": f"Ordem De Produção #{code}",                                      # Meta
        "customfield_10053": f"{code}",                                     # Número Ordem De Produção
        "customfield_10054": f"{random.randint(1000000000, 9999999999)}",   # Código Do Produto
        "customfield_10055": f"{random.randint(1000000000, 9999999999)}",   # Código De Rastreio
        "customfield_10056": fake.color(),                                  # Cor Da Pointera
        "customfield_10057": fake.company(),                                # Tipo De Pointera
        "customfield_10058": random.randint(10, 50),                        # Quantidade
        "customfield_10059": fake.text(max_nb_chars=200),                   # Observações
    }
    production_orders.append(production_order)

  json_object = json.dumps(production_orders, indent=4)
  with open("./test/sample.json", "w") as outfile:
    outfile.write(json_object)
