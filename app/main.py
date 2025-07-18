from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objs: List[Customer] = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    cleaner_obj = Cleaner(name=cleaner)

    for cust in customer_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
