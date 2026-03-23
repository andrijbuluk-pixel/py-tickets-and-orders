from db.models import Order, Ticket
from django.db import transaction
from django.contrib.auth import get_user_model


@transaction.atomic
def create_order(tickets: list, username: str, created_at: int) -> Order:
    if not tickets:
        raise ValueError("Tickets cannot be empty")

    user_model = get_user_model()

    user = user_model.objects.get(
        username=username
    )

    order = Order.objects.create(
        user=user
    )

    for ticket in tickets:
        Ticket.objects.create(
            row=ticket["row"],
            seat=ticket["seat"],
            movie_session_id=ticket["movie_session"],
            order=order
        )

    return order
