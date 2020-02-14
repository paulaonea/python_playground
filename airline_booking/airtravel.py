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
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied.")
        self._seating[row][letter] = passenger
        return

    def re_allocate_seat(self, old_seat, new_seat, passenger):
        old_row, old_letter = self._parse_seat(old_seat)
        if self._seating[old_row][old_letter] != passenger:
            raise ValueError(f"Old Seat Error. {passenger} does not occupy seat {old_seat}")
        self.allocate_seat(new_seat, passenger)
        self._seating[old_row][old_letter] = None
        return

    def _parse_seat(self, seat):
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
        return sum(sum(1 for s in row.values()) for row in self.seating() if row is not None)

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self.seating() if row is not None)

    def free_seats(self):
        rows, seat_letters = self._aircraft.seating_plan()
        free_seats = [None] + [{letter: None for letter in seat_letters if self._seating[_][letter] is None}
                               for _ in rows if _ is not None]
        return free_seats

    def make_boarding_card(self, card_printer):
        passengers_booked = self._passenger_seats()
        for passenger, seat in passengers_booked:
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        passengers_booked = []
        row_numbers, seats_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seats_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    passengers_booked.append((passenger, f"{row}{letter}"))
        return passengers_booked


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHIJK"[:self._num_seats_per_row])


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
