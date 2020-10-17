"""Discovery module for Tuya devices.

Entirely based on tuya-convert.py from tuya-convert:

https://github.com/ct-Open-Source/tuya-convert/blob/master/scripts/tuya-discovery.py
"""
import sys
import json
import asyncio
import logging
from datetime import datetime
from hashlib import md5

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

_LOGGER = logging.getLogger(__name__)

UDP_KEY = md5(b"yGAdlopoPVldABfn").digest()


def decrypt_udp(message):
    """Decrypt encrypted UDP broadcasts."""

    def _unpad(data):
        return data[: -ord(data[len(data) - 1 :])]

    cipher = Cipher(algorithms.AES(UDP_KEY), modes.ECB(), default_backend())
    decryptor = cipher.decryptor()
    return _unpad(decryptor.update(message) + decryptor.finalize()).decode()


class TuyaDiscovery(asyncio.DatagramProtocol):
    """Datagram handler listening for Tuya broadcast messages."""

    def __init__(self, device_id):
        """Initialize a new TuyaDiscovery instance."""
        self.device_id = device_id

    def datagram_received(self, data, addr):
        """Handle received broadcast message."""
        data = data[20:-8]
        try:
            data = decrypt_udp(data)
        except Exception:
            data = data.decode()

        decoded = json.loads(data)
        if decoded.get("gwId") == self.device_id:
            print(datetime.now(), decoded)


async def discover(timeout, device_id, loop):
    """Discover and return Tuya devices on the network."""

    def proto_factory():
        return TuyaDiscovery(device_id)

    listener = loop.create_datagram_endpoint(
        proto_factory, local_addr=("0.0.0.0", 6666)
    )
    encrypted_listener = loop.create_datagram_endpoint(
        proto_factory, local_addr=("0.0.0.0", 6667)
    )

    listeners = await asyncio.gather(listener, encrypted_listener)
    _LOGGER.debug("Listening to broadcasts on UDP port 6666 and 6667")

    try:
        await asyncio.sleep(timeout)
    finally:
        for transport, _ in listeners:
            transport.close()


def main():
    """Run discovery and print result."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(discover(10000000000, sys.argv[1], loop))


if __name__ == "__main__":
    main()
