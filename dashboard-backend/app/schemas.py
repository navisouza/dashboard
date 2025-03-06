from pydantic import BaseModel


class ChartDatabase(BaseModel):
    name: str
    value: int


class ChartDataCreate(ChartDatabase):
    pass


class ChartDataResponse(ChartDatabase):
    chart_id: int

    class Config:
        from_attrs = True
