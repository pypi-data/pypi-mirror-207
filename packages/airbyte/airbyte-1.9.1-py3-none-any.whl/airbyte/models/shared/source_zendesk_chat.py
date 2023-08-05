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

class SourceZendeskChatCredentialsAccessTokenCredentialsEnum(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskChatCredentialsAccessToken:
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The Access Token to make authenticated requests."""
    credentials: SourceZendeskChatCredentialsAccessTokenCredentialsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    
class SourceZendeskChatCredentialsOAuth20CredentialsEnum(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskChatCredentialsOAuth20:
    
    credentials: SourceZendeskChatCredentialsOAuth20CredentialsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""Access Token for making authenticated requests."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your OAuth application"""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of your OAuth application."""
    refresh_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token'), 'exclude': lambda f: f is None }})
    r"""Refresh Token to obtain new Access Token, when it's expired."""
    
class SourceZendeskChatZendeskChatEnum(str, Enum):
    ZENDESK_CHAT = 'zendesk-chat'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskChat:
    r"""The values required to configure the source."""
    
    source_type: SourceZendeskChatZendeskChatEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date from which you'd like to replicate data for Zendesk Chat API, in the format YYYY-MM-DDT00:00:00Z."""
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    subdomain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain'), 'exclude': lambda f: f is None }})
    r"""Required if you access Zendesk Chat from a Zendesk Support subdomain."""
    