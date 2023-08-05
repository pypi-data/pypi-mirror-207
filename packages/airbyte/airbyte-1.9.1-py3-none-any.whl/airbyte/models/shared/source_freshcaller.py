"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceFreshcallerFreshcallerEnum(str, Enum):
    FRESHCALLER = 'freshcaller'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFreshcaller:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Freshcaller API Key. See the <a href=\\"https://docs.airbyte.io/integrations/sources/freshcaller\\">docs</a> for more information on how to obtain this key."""
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    r"""Used to construct Base URL for the Freshcaller APIs"""
    source_type: SourceFreshcallerFreshcallerEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""UTC date and time. Any data created after this date will be replicated."""
    requests_per_minute: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requests_per_minute'), 'exclude': lambda f: f is None }})
    r"""The number of requests per minute that this source allowed to use. There is a rate limit of 50 requests per minute per app per account."""
    sync_lag_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync_lag_minutes'), 'exclude': lambda f: f is None }})
    r"""Lag in minutes for each sync, i.e., at time T, data for the time range [prev_sync_time, T-30] will be fetched"""
    