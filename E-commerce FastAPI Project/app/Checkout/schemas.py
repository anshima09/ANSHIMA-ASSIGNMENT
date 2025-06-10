from pydantic import BaseModel

class CheckoutResponse(BaseModel):
    message: str
    order_id: int
    total_amount: float