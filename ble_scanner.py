import asyncio
from bleak import BleakScanner, BleakClient

TARGET_TAG = "StationTag"
CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

async def scan_and_publish(publisher):
    devices = await BleakScanner.discover()
    for d in devices:
        if TARGET_TAG in d.name:
            async with BleakClient(d.address) as client:
                data = await client.read_gatt_char(CHAR_UUID)
                await publisher.publish(data)
            break

if __name__ == "__main__":
    # TODO: integrate with mqtt_publisher
    pass
