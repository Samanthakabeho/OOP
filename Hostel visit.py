from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

@dataclass
class Visitor:
    name: str
    visitor_id: str

    def __str__(self):
        return f"{self.name} ({self.visitor_id})"

@dataclass
class Resident:
    name: str
    room: str

    def __str__(self):
        return f"{self.name} - Room {self.room}"

class Hostel:
    def __init__(self, name: str):
        self.name = name
        # store visits as tuples: (timestamp, Visitor, Resident)
        self.visits: List[Tuple[datetime, Visitor, Resident]] = []

    def record_visit(self, visitor: Visitor, resident: Resident, when: datetime = None):
        """Record a visit of a visitor to a resident. Optionally supply a datetime."""
        if when is None:
            when = datetime.now()
        # Basic type checks (helpful during development)
        if not isinstance(visitor, Visitor):
            raise TypeError("visitor must be a Visitor instance")
        if not isinstance(resident, Resident):
            raise TypeError("resident must be a Resident instance")

        self.visits.append((when, visitor, resident))
        print(f"Recorded visit: {visitor} -> {resident} at {when.strftime('%Y-%m-%d %H:%M:%S')}")

    def show_visits(self):
        """Pretty-print a list of visits."""
        if not self.visits:
            print(f"No visits recorded for {self.name}.")
            return

        print(f"Visits recorded for {self.name}:")
        print("-" * 60)
        print(f"{'No.':<4} {'Timestamp':<20} {'Visitor':<20} {'Resident':<15}")
        print("-" * 60)
        for i, (ts, visitor, resident) in enumerate(self.visits, start=1):
            ts_str = ts.strftime('%Y-%m-%d %H:%M:%S')
            print(f"{i:<4} {ts_str:<20} {str(visitor):<20} {str(resident):<15}")
        print("-" * 60)

# ---- Demo usage (from the slide) ----
if __name__ == "__main__":
    visitor1 = Visitor('Alice', 'V123')
    resident1 = Resident('Bob', '12B')

    hostel = Hostel('UCU Hostel')
    hostel.record_visit(visitor1, resident1)

    # add a second visit to show multiple entries
    visitor2 = Visitor('Sam', 'V456')
    resident2 = Resident('Merinah', '8A')
    hostel.record_visit(visitor2, resident2)

    hostel.show_visits()
