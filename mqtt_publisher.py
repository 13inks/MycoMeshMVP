import asyncio
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "pr3p/rooms/env"

class Publisher:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect(BROKER)

    async def publish(self, data):
        self.client.publish(TOPIC, data.hex())

if __name__ == "__main__":
    # Example run
    pub = Publisher()
    asyncio.run(scan_and_publish(pub))
