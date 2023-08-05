"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceFireboltFireboltEnum(str, Enum):
    FIREBOLT = 'firebolt'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFirebolt:
    r"""The values required to configure the source."""
    
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The database to connect to."""
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Firebolt password."""
    source_type: SourceFireboltFireboltEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Firebolt email address you use to login."""
    account: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account'), 'exclude': lambda f: f is None }})
    r"""Firebolt account to login."""
    engine: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('engine'), 'exclude': lambda f: f is None }})
    r"""Engine name or url to connect to."""
    host: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host'), 'exclude': lambda f: f is None }})
    r"""The host name of your Firebolt database."""
    