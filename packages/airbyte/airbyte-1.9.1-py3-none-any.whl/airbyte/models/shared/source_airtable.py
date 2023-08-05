"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceAirtableCredentialsPersonalAccessTokenAuthMethodEnum(str, Enum):
    API_KEY = 'api_key'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAirtableCredentialsPersonalAccessToken:
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The Personal Access Token for the Airtable account. See the <a href=\\"https://airtable.com/developers/web/guides/personal-access-tokens\\">Support Guide</a> for more information on how to obtain this token."""
    auth_method: Optional[SourceAirtableCredentialsPersonalAccessTokenAuthMethodEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    
class SourceAirtableCredentialsOAuth20AuthMethodEnum(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAirtableCredentialsOAuth20:
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID of the Airtable developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret the Airtable developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access token."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""Access Token for making authenticated requests."""
    auth_method: Optional[SourceAirtableCredentialsOAuth20AuthMethodEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    token_expiry_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date-time when the access token should be refreshed."""
    
class SourceAirtableAirtableEnum(str, Enum):
    AIRTABLE = 'airtable'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAirtable:
    r"""The values required to configure the source."""
    
    source_type: SourceAirtableAirtableEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    