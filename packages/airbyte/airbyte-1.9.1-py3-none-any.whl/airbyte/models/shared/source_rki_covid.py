"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceRkiCovidRkiCovidEnum(str, Enum):
    RKI_COVID = 'rki-covid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRkiCovid:
    r"""The values required to configure the source."""
    
    source_type: SourceRkiCovidRkiCovidEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""UTC date in the format 2017-01-25. Any data before this date will not be replicated."""
    