from sqlalchemy import Column, Integer, String

from .database import Base


class ChartData(Base):
    """
    ChartData represents the data for a chart.

    Attributes
    ----------
        chart_id (int): The unique identifier for the chart data.
        name (str): The name of the chart data.
        value (int): The value associated with the chart data.

    """

    __tablename__ = "chart_data"

    chart_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Integer)
