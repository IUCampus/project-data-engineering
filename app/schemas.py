from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SensorData(BaseModel):
    sensor_id: str
    type: str
    value: float
    unit: str
    timestamp: datetime
    location: Optional[dict] = Field(default_factory=dict)
    extra: Optional[dict] = Field(default_factory=dict)
