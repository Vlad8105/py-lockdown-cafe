import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f'{visitor["name"]} is not vaccinated and cannot enter '
                f'{self.name}.')
        expiration_date = visitor["vaccine"].get("expiration_date")
        if not expiration_date or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f'{visitor["name"]} vaccine has expired {self.name}.')
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f'{visitor["name"]} is not wearing a mask and cannot enter '
                f'{self.name}.')
        return f"Welcome to {self.name}"
