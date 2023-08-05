import pytest
import sys

from luckyun_nacos import Client


@pytest.fixture(autouse=True)
def capture_wrap():
    sys.stderr.close = lambda *args: None
    sys.stdout.close = lambda *args: None
    yield

class TestClient:

    SERVER_ADDRESSES = "http://127.0.0.1:31000"
    NAMESPACE = "dev_env"
    SERVICE_NAME = "python_service"
    SERVICE_IP = "127.0.0.1"
    SERVICE_PORT = 5000

    DATA_ID = "common-dev.yml"
    GROUP = "DEFAULT_GROUP"

    def test_client_initialization(self):

        client = Client(TestClient.SERVER_ADDRESSES, namespace=TestClient.NAMESPACE,
                        service_name=TestClient.SERVICE_NAME, service_ip=TestClient.SERVICE_IP, service_port=TestClient.SERVICE_PORT,heartbeat_rate=5)

        client.add_instance()

    def test_client_getconfig(self):

        client = Client(TestClient.SERVER_ADDRESSES, namespace=TestClient.NAMESPACE,
                        service_name=TestClient.SERVICE_NAME, service_ip=TestClient.SERVICE_IP, service_port=TestClient.SERVICE_PORT)

        assert isinstance(client.get_config(
            TestClient.DATA_ID, TestClient.GROUP), dict)
