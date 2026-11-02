"""Port of switzerland_plate/lib/src/switzerland_validators.dart. Hand-ported; codegen never overwrites this file."""
from __future__ import annotations

from dataclasses import dataclass

from plates.core.validators.plate_validator import GatedPlateValidator, PlateEntry, PlateValidation, is_digits

SWITZERLAND_CANTONS = ('AG', 'AI', 'AR', 'BE', 'BL', 'BS', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU', 'NE',
                       'NW', 'OW', 'SG', 'SH', 'SO', 'SZ', 'TG', 'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH')

NOT_FOUND = 'COUNTRY NOT FOUND'
REFUSED = ('7', '07', '007')


def _is_plain(s: str) -> bool:
    return is_digits(s) and not s.startswith('0')


@dataclass(frozen=True)
class SwitzerlandValidator(GatedPlateValidator):
    military: bool = False
    gate_group = 'number'

    REASON_CANTON = 'The canton is a Swiss canton code.'
    REASON_NUMBER = 'The number is digits without a leading 0.'

    def judge(self, entry: PlateEntry) -> PlateValidation:
        canton = entry.group('canton')
        if canton not in SWITZERLAND_CANTONS and not (self.military and canton == 'M'):
            return PlateValidation.invalid(self.REASON_CANTON)
        if not _is_plain(entry.group('number')):
            return PlateValidation.invalid(self.REASON_NUMBER)
        return PlateValidation.valid()


@dataclass(frozen=True)
class SwitzerlandDiplomaticValidator(GatedPlateValidator):
    gate_group = 'code'

    REASON_SERIAL = 'The serial is one to three digits.'
    REASON_CODE = 'The code is one to three digits.'

    def validate(self, entry: PlateEntry) -> PlateValidation:
        if entry.group('code') in REFUSED:
            return PlateValidation.invalid(NOT_FOUND)
        return super().validate(entry)

    def judge(self, entry: PlateEntry) -> PlateValidation:
        if entry.group('canton') not in SWITZERLAND_CANTONS:
            return PlateValidation.invalid(SwitzerlandValidator.REASON_CANTON)
        if not _is_plain(entry.group('serial')):
            return PlateValidation.invalid(self.REASON_SERIAL)
        if not _is_plain(entry.group('code')):
            return PlateValidation.invalid(self.REASON_CODE)
        return PlateValidation.valid()
