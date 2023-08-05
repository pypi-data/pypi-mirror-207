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

class SourceSftpBulkFileTypeEnum(str, Enum):
    r"""The file type you want to sync. Currently only 'csv' and 'json' files are supported."""
    CSV = 'csv'
    JSON = 'json'

class SourceSftpBulkSftpBulkEnum(str, Enum):
    SFTP_BULK = 'sftp-bulk'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulk:
    r"""The values required to configure the source."""
    
    folder_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_path') }})
    r"""The directory to search files for sync"""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The server host address"""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""The server port"""
    source_type: SourceSftpBulkSftpBulkEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date from which you'd like to replicate data for all incremental streams, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    stream_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_name') }})
    r"""The name of the stream or table you want to create"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""The server user"""
    file_most_recent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_most_recent'), 'exclude': lambda f: f is None }})
    r"""Sync only the most recent file for the configured folder path and file pattern"""
    file_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_pattern'), 'exclude': lambda f: f is None }})
    r"""The regular expression to specify files for sync in a chosen Folder Path"""
    file_type: Optional[SourceSftpBulkFileTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_type'), 'exclude': lambda f: f is None }})
    r"""The file type you want to sync. Currently only 'csv' and 'json' files are supported."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""OS-level password for logging into the jump server host"""
    private_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key'), 'exclude': lambda f: f is None }})
    r"""The private key"""
    