"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSurveymonkeySurveyMonkeyAuthorizationMethodAuthMethodEnum(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveymonkeySurveyMonkeyAuthorizationMethod:
    r"""The authorization method to use to retrieve data from SurveyMonkey"""
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests. See the <a href=\\"https://docs.airbyte.io/integrations/sources/surveymonkey\\">docs</a> for information on how to generate this key."""
    auth_method: SourceSurveymonkeySurveyMonkeyAuthorizationMethodAuthMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of the SurveyMonkey developer application."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of the SurveyMonkey developer application."""
    
class SourceSurveymonkeyOriginDatacenterOfTheSurveyMonkeyAccountEnum(str, Enum):
    r"""Depending on the originating datacenter of the SurveyMonkey account, the API access URL may be different."""
    USA = 'USA'
    EUROPE = 'Europe'
    CANADA = 'Canada'

class SourceSurveymonkeySurveymonkeyEnum(str, Enum):
    SURVEYMONKEY = 'surveymonkey'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveymonkey:
    r"""The values required to configure the source."""
    
    source_type: SourceSurveymonkeySurveymonkeyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    credentials: Optional[SourceSurveymonkeySurveyMonkeyAuthorizationMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""The authorization method to use to retrieve data from SurveyMonkey"""
    origin: Optional[SourceSurveymonkeyOriginDatacenterOfTheSurveyMonkeyAccountEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origin'), 'exclude': lambda f: f is None }})
    r"""Depending on the originating datacenter of the SurveyMonkey account, the API access URL may be different."""
    survey_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_ids'), 'exclude': lambda f: f is None }})
    r"""IDs of the surveys from which you'd like to replicate data. If left empty, data from all boards to which you have access will be replicated."""
    