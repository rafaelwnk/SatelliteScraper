class Satellite:
    def __init__(self, name: str, orbital_status: str, designation: str, orbit: str):
        self.name: str = name
        self.orbital_status: str = orbital_status
        self.designation: str = designation
        self.orbit: str = orbit