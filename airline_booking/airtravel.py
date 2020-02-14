"""Model for Airline travel"""


class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'. Flight number has to start with two letters.")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code in'{number}'.  Use capital letters.")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number in '{number}'.  Use format: 'LLDDDD'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def route(self):
        return self._number[2:]

    def aircraft_model(self):
        return self._aircraft.model()

    def seating(self):
        return self._seating

    def allocate_seat(self, seat, passenger):
        """Allocate seat for a new passenger
        Args: seat - seat number to be allocated
               passenger - name
        Raise error if seat is already occupied"""

        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied.")
        self._seating[row][letter] = passenger
        return

    def re_allocate_seat(self, old_seat, new_seat, passenger):
        """Re-allocate seat for an existing passenger
        Args: old_seat - current seat number
              new_seat - new seat to be allocated to existing passenger
              passenger - name of the existing passenger (used as extra validation criteria
        Raise error
              if the passenger does not correspond to old_seat
              if new seat is occupied"""

        old_row, old_letter = self._parse_seat(old_seat)
        if self._seating[old_row][old_letter] != passenger:
            raise ValueError(f"Old Seat Error. {passenger} does not occupy seat {old_seat}")
        self.allocate_seat(new_seat, passenger)
        self._seating[old_row][old_letter] = None
        return

    def _parse_seat(self, seat):
        """Used to parse seat_number into:
                row - row number
                letter - seat letter
            Raise error if
                seat does not end with letter
                row number is not number or row number is different than the aircraft's seating plan"""
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter '{letter}'")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text}")
        if row not in rows:
            raise ValueError(f"Invalid row number. Row number out of range.")
        return row, letter

    def total_seats(self):
        """Returns total number of seats in the aircraft."""
        return self._aircraft.total_seats()

    def num_available_seats(self):
        """Returns total number of available seats in the aircraft."""
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self.seating() if row is not None)

    def free_seats(self):
        """Returns the list with all available seats in the aircraft."""
        rows, seat_letters = self._aircraft.seating_plan()
        free_seats = [None] + [{letter: None for letter in seat_letters if self._seating[_][letter] is None}
                               for _ in rows if _ is not None]
        return free_seats

    def make_boarding_card(self, card_printer):
        """Send boarding card to be printed in a specified format."""
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """Returns tupples (passenger_name, allocated_seat)"""
        row_numbers, seats_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seats_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def total_seats(self):
        rows, rows_seats = self.seating_plan()
        return len(rows) * len(rows_seats)


class Airbus319(Aircraft):

    def model(self):
        return "Airbus319"

    def seating_plan(self):
        return(range(1,23), "ABCDEF")


class Boeing777(Aircraft):

    def model(self):
        return "Boeing777"

    def seating_plan(self):
        return(range(1,54), "ABCDEFGH")


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger} "         \
        f"| Flight number: {flight_number} " \
        f"| Seat: {seat} "                   \
        f"| Aircraft: {aircraft} |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
