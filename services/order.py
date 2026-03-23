from db.models import Order, Ticket, User
from django.db import transaction


def create_order(tickets: list, username: str) -> Order:
    with transaction.atomic():
        if not tickets:
            raise ValueError("Tickets cannot be empty")

        user = User.objects.get(
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
