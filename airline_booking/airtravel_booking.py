from pprint import pprint as pp
from airtravel import *


aircraft = Aircraft("G-EUPT", "Airbus A319", num_rows=12, num_seats_per_row=4)
f = Flight("BA758", aircraft)
f.allocate_seat("12A", "Joe")
f.allocate_seat("12B", "Cassie")
f.allocate_seat("4C", "Archie")
f.allocate_seat("12D", "Elizabeth")
f.re_allocate_seat("4C", "12C", "Archie")
f.allocate_seat("10B", "Emma")
f.allocate_seat("3D", "Ellie")
# pp(f.seating())
print(f"There are a total of {f.total_seats()} seats on flight number {f.number()}. "
      f"{f.num_available_seats()} seats are still available.")
f.make_boarding_card(console_card_printer)