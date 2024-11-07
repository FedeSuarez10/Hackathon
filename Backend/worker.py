# worker.py
from redis import Redis
from rq import Worker, Queue

# Connexion à Redis
redis_conn = Redis()

# Définir la file d'attente (queue) et spécifier la connexion
listen = [Queue('default', connection=redis_conn)]  # Fournir la connexion explicitement ici

if __name__ == '__main__':
    # Démarrer le worker pour écouter les tâches dans la queue 'default'
    worker = Worker(listen, connection=redis_conn)
    worker.work()
