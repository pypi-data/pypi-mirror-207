"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationS3GlueS3GlueEnum(str, Enum):
    S3_GLUE = 's3-glue'

class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum(str, Enum):
    GZIP = 'GZIP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionGZIP:
    r"""Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \\".jsonl.gz\\")."""
    
    compression_type: Optional[DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionGZIPCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum(str, Enum):
    NO_COMPRESSION = 'No Compression'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionNoCompression:
    r"""Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \\".jsonl.gz\\")."""
    
    compression_type: Optional[DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONFlatteningEnum(str, Enum):
    r"""Whether the input json data should be normalized (flattened) in the output JSON Lines. Please refer to docs for details."""
    NO_FLATTENING = 'No flattening'
    ROOT_LEVEL_FLATTENING = 'Root level flattening'

class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum(str, Enum):
    JSONL = 'JSONL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3GlueFormatJSONLinesNewlineDelimitedJSON:
    r"""Format of the data output. See <a href=\\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\\">here</a> for more details"""
    
    format_type: DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    compression: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \\".jsonl.gz\\")."""
    flattening: Optional[DestinationS3GlueFormatJSONLinesNewlineDelimitedJSONFlatteningEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening'), 'exclude': lambda f: f is None }})
    r"""Whether the input json data should be normalized (flattened) in the output JSON Lines. Please refer to docs for details."""
    
class DestinationS3GlueSerializationLibraryEnum(str, Enum):
    r"""The library that your query engine will use for reading and writing data in your lake."""
    ORG_OPENX_DATA_JSONSERDE_JSON_SER_DE = 'org.openx.data.jsonserde.JsonSerDe'
    ORG_APACHE_HIVE_HCATALOG_DATA_JSON_SER_DE = 'org.apache.hive.hcatalog.data.JsonSerDe'

class DestinationS3GlueS3BucketRegionEnum(str, Enum):
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    UNKNOWN = ''
    US_EAST_1 = 'us-east-1'
    US_EAST_2 = 'us-east-2'
    US_WEST_1 = 'us-west-1'
    US_WEST_2 = 'us-west-2'
    AF_SOUTH_1 = 'af-south-1'
    AP_EAST_1 = 'ap-east-1'
    AP_SOUTH_1 = 'ap-south-1'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    AP_NORTHEAST_2 = 'ap-northeast-2'
    AP_NORTHEAST_3 = 'ap-northeast-3'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    CA_CENTRAL_1 = 'ca-central-1'
    CN_NORTH_1 = 'cn-north-1'
    CN_NORTHWEST_1 = 'cn-northwest-1'
    EU_CENTRAL_1 = 'eu-central-1'
    EU_NORTH_1 = 'eu-north-1'
    EU_SOUTH_1 = 'eu-south-1'
    EU_WEST_1 = 'eu-west-1'
    EU_WEST_2 = 'eu-west-2'
    EU_WEST_3 = 'eu-west-3'
    SA_EAST_1 = 'sa-east-1'
    ME_SOUTH_1 = 'me-south-1'
    US_GOV_EAST_1 = 'us-gov-east-1'
    US_GOV_WEST_1 = 'us-gov-west-1'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3Glue:
    r"""The values required to configure the destination."""
    
    destination_type: DestinationS3GlueS3GlueEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    format: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""Format of the data output. See <a href=\\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\\">here</a> for more details"""
    glue_database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('glue_database') }})
    r"""Name of the glue database for creating the tables, leave blank if no integration"""
    glue_serialization_library: DestinationS3GlueSerializationLibraryEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('glue_serialization_library') }})
    r"""The library that your query engine will use for reading and writing data in your lake."""
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    r"""The name of the S3 bucket. Read more <a href=\\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html\\">here</a>."""
    s3_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path') }})
    r"""Directory under the S3 bucket where data will be written. Read more <a href=\\"https://docs.airbyte.com/integrations/destinations/s3#:~:text=to%20format%20the-,bucket%20path,-%3A\\">here</a>"""
    s3_bucket_region: DestinationS3GlueS3BucketRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region') }})
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id'), 'exclude': lambda f: f is None }})
    r"""The access key ID to access the S3 bucket. Airbyte requires Read and Write permissions to the given bucket. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">here</a>."""
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    r"""The pattern allows you to set the file-name format for the S3 staging file(s)"""
    s3_endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_endpoint'), 'exclude': lambda f: f is None }})
    r"""Your S3 endpoint url. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/s3.html#:~:text=Service%20endpoints-,Amazon%20S3%20endpoints,-When%20you%20use\\">here</a>"""
    s3_path_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_path_format'), 'exclude': lambda f: f is None }})
    r"""Format string on how data will be organized inside the S3 bucket directory. Read more <a href=\\"https://docs.airbyte.com/integrations/destinations/s3#:~:text=The%20full%20path%20of%20the%20output%20data%20with%20the%20default%20S3%20path%20format\\">here</a>"""
    secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key'), 'exclude': lambda f: f is None }})
    r"""The corresponding secret to the access key ID. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">here</a>"""
    