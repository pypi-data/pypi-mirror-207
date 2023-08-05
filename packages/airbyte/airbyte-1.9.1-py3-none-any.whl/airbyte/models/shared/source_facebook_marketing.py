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

class SourceFacebookMarketingInsightConfigLevelEnum(str, Enum):
    r"""Chosen level for API"""
    AD = 'ad'
    ADSET = 'adset'
    CAMPAIGN = 'campaign'
    ACCOUNT = 'account'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFacebookMarketingInsightConfig:
    r"""Config for custom insights"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name value of insight"""
    action_breakdowns: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_breakdowns'), 'exclude': lambda f: f is None }})
    r"""A list of chosen action_breakdowns for action_breakdowns"""
    breakdowns: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('breakdowns'), 'exclude': lambda f: f is None }})
    r"""A list of chosen breakdowns for breakdowns"""
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date until which you'd like to replicate data for this stream, in the format YYYY-MM-DDT00:00:00Z. All data generated between the start date and this end date will be replicated. Not setting this option will result in always syncing the latest data."""
    fields_: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is None }})
    r"""A list of chosen fields for fields parameter"""
    insights_lookback_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insights_lookback_window'), 'exclude': lambda f: f is None }})
    r"""The attribution window"""
    level: Optional[SourceFacebookMarketingInsightConfigLevelEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('level'), 'exclude': lambda f: f is None }})
    r"""Chosen level for API"""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date from which you'd like to replicate data for this stream, in the format YYYY-MM-DDT00:00:00Z."""
    time_increment: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_increment'), 'exclude': lambda f: f is None }})
    r"""Time window in days by which to aggregate statistics. The sync will be chunked into N day intervals, where N is the number of days you specified. For example, if you set this value to 7, then all statistics will be reported as 7-day aggregates by starting from the start_date. If the start and end dates are October 1st and October 30th, then the connector will output 5 records: 01 - 06, 07 - 13, 14 - 20, 21 - 27, and 28 - 30 (3 days only)."""
    
class SourceFacebookMarketingFacebookMarketingEnum(str, Enum):
    FACEBOOK_MARKETING = 'facebook-marketing'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFacebookMarketing:
    r"""The values required to configure the source."""
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The value of the generated access token. From your App’s Dashboard, click on \\"Marketing API\\" then \\"Tools\\". Select permissions <b>ads_management, ads_read, read_insights, business_management</b>. Then click on \\"Get token\\". See the <a href=\\"https://docs.airbyte.com/integrations/sources/facebook-marketing\\">docs</a> for more information."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The Facebook Ad account ID to use when pulling data from the Facebook Marketing API. Open your Meta Ads Manager. The Ad account ID number is in the account dropdown menu or in your browser's address bar. See the <a href=\\"https://www.facebook.com/business/help/1492627900875762\\">docs</a> for more information."""
    source_type: SourceFacebookMarketingFacebookMarketingEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date from which you'd like to replicate data for all incremental streams, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    action_breakdowns_allow_empty: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_breakdowns_allow_empty'), 'exclude': lambda f: f is None }})
    r"""Allows action_breakdowns to be an empty list"""
    custom_insights: Optional[list[SourceFacebookMarketingInsightConfig]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_insights'), 'exclude': lambda f: f is None }})
    r"""A list which contains ad statistics entries, each entry must have a name and can contains fields, breakdowns or action_breakdowns. Click on \\"add\\" to fill this field."""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""The date until which you'd like to replicate data for all incremental streams, in the format YYYY-MM-DDT00:00:00Z. All data generated between the start date and this end date will be replicated. Not setting this option will result in always syncing the latest data."""
    fetch_thumbnail_images: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fetch_thumbnail_images'), 'exclude': lambda f: f is None }})
    r"""Set to active if you want to fetch the thumbnail_url and store the result in thumbnail_data_url for each Ad Creative."""
    include_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_deleted'), 'exclude': lambda f: f is None }})
    r"""Set to active if you want to include data from deleted Campaigns, Ads, and AdSets."""
    insights_lookback_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insights_lookback_window'), 'exclude': lambda f: f is None }})
    r"""The attribution window. Facebook freezes insight data 28 days after it was generated, which means that all data from the past 28 days may have changed since we last emitted it, so you can retrieve refreshed insights from the past by setting this parameter. If you set a custom lookback window value in Facebook account, please provide the same value here."""
    max_batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_batch_size'), 'exclude': lambda f: f is None }})
    r"""Maximum batch size used when sending batch requests to Facebook API. Most users do not need to set this field unless they specifically need to tune the connector to address specific issues or use cases."""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size'), 'exclude': lambda f: f is None }})
    r"""Page size used when sending requests to Facebook API to specify number of records per page when response has pagination. Most users do not need to set this field unless they specifically need to tune the connector to address specific issues or use cases."""
    