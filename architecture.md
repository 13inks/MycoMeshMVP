# System Architecture

```mermaid
flowchart LR
  subgraph Edge Gateway (on-prem)
    A[BLE Scanner & Local MQTT] --> B["Pr3p Edge Agent"]
    B -->|pub| C[Local Mosquitto Broker]
  end

  C -->|MQTT over TLS| D[Cloud Ingestion (AWS IoT Core)]
  D --> E[MycoMesh Microservices]
  subgraph MycoMesh Services
      E1[Narrative Seed Agent] 
      E2[Forecast Engine (Bacterial Service)] 
      E3[Swarm Quorum Monitor] 
      E4[Data Chelation Layer]
      E5[ZK Privacy Module]
      E6[Tokenomics & SugarCoin Ledger]
    end

  E --> F[Pr3p Dashboard & APIs]
  F --> G[User (GM / Chef) Mobile/Web]

  E6 --> H[Blockchain Network (SugarCoin)]
  F -->|Alert / Command| C
```
