from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ChartData
from app.schemas import ChartDataCreate, ChartDataResponse

router = APIRouter()


@router.post("/chart", response_model=ChartDataResponse)
def create_chart(
    chart_data: ChartDataCreate,
    db: Annotated[Session, Depends(get_db)],
):
    """
    Create a new chart data record.

    Parameters
    ----------
    chart_data (ChartDataCreate): The chart data to create.
    db (Session): Database session dependency.

    Returns
    -------
    ChartDataResponse: The newly created chart data.

    """
    chart = ChartData(**chart_data.dict())
    db.add(chart)
    db.commit()
    db.refresh(chart)
    return chart


@router.get("/charts")
def get_charts(db: Annotated[Session, Depends(get_db)]):
    """
    Retrieve all chart data from the database.

    Parameters
    ----------
    db (Session): Database session dependency.

    Returns
    -------
    List of all chart data.

    """
    return db.query(ChartData).all()


@router.get("/chart/{chart_id}")
def get_chart(chart_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Retrieve chart data by chart ID.

    Parameters
    ----------
    chart_id (int): The ID of the chart to retrieve.
    db (Session): Database session dependency.

    Returns
    -------
    ChartData: The chart data with the specified ID.

    """
    chart = db.query(ChartData).filter(ChartData.chart_id == chart_id).first()
    if not chart:
        raise HTTPException(status_code=404, detail="Chart data not found")
    return chart


@router.put("/chart/{chart_id}", response_model=ChartDataResponse)
def update_chart(
    chart_id: int,
    chart_data: ChartDataCreate,
    db: Annotated[Session, Depends(get_db)],
):
    """
    Update chart data by chart ID.

    Parameters
    ----------
    chart_id (int): The ID of the chart to update.
    chart_data (ChartDataCreate): The updated chart data.
    db (Session): Database session dependency.

    Returns
    -------
    ChartDataResponse: The updated chart data.

    """
    chart = db.query(ChartData).filter(ChartData.chart_id == chart_id).first()
    if not chart:
        raise HTTPException(status_code=404, detail="Chart data not found")
    for key, value in chart_data.dict().items():
        setattr(chart, key, value)
    db.commit()
    db.refresh(chart)
    return chart


@router.delete("/charts/{chart_id}", status_code=204)
def delete_chart(chart_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Delete chart data by chart ID.

    Parameters
    ----------
    chart_id (int): The ID of the chart to delete.
    db (Session): Database session dependency.

    """
    chart = db.query(ChartData).filter(ChartData.chart_id == chart_id).first()
    if not chart:
        raise HTTPException(status_code=404, detail="Chart data not found")
    db.delete(chart)
    db.commit()
