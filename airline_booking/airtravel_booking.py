from pprint import pprint as pp
from airtravel import *


aircraft1 = Airbus319("G-EUPT")
f = Flight("BA758", aircraft1)

aircraft2 = Boeing777("BE12-V")
g = Flight("MA152", aircraft2)

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

pp(f'Flight number {g.number()} has a total number of seats of {g.total_seats()} of which {g.num_available_seats()} '
   f'seats are still available.')