# federated-voter-sync
federated voter synchronisation system
# Federated Voter Synchronization 

This project demonstrates a **privacy-preserving, federated voter data synchronization system**.

## Key Ideas
- States keep their own voter databases
- Only hashed identity signals are shared
- No central voter database
- Full auditability

## Services
- `state_service` – Simulated state election authority
- `sync_service` – Coordination & matching layer

## Run
```bash
docker-compose up --build
