import pytest
from httpx import AsyncClient
from datetime import datetime
from main import app  # Change to your actual app file name if not "main.py"

# Example data for testing
test_data = [
    {
        "sensor_id": "sensor1",
        "type": "temperature",
        "value": 30.5,
        "timestamp": datetime.utcnow().isoformat()
    },
    {
        "sensor_id": "sensor2",
        "type": "humidity",
        "value": 70.0,
        "timestamp": datetime.utcnow().isoformat()
    }
]

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from Sensor API!"}


@pytest.mark.asyncio
async def test_add_sensor_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/sensors/batch", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["inserted"] == len(test_data)


@pytest.mark.asyncio
async def test_get_measurements():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/measurements?limit=5")
    assert response.status_code == 200
    measurements = response.json()
    assert isinstance(measurements, list)
    if measurements:
        assert "id" in measurements[0]
        assert "type" in measurements[0]


@pytest.mark.asyncio
async def test_get_latest_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/sensors/latest")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_history():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Provide query params for filtering if needed
        response = await ac.get("/sensors/history", params={"sensor_type": "temperature"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_alerts():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/sensors/alerts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

