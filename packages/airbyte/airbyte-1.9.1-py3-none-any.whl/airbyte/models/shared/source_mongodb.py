"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceMongodbInstanceTypeMongoDBAtlasInstanceEnum(str, Enum):
    ATLAS = 'atlas'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbInstanceTypeMongoDBAtlas:
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    
    cluster_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster_url') }})
    r"""The URL of a cluster to connect to."""
    instance: SourceMongodbInstanceTypeMongoDBAtlasInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    
class SourceMongodbInstanceTypeReplicaSetInstanceEnum(str, Enum):
    REPLICA = 'replica'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbInstanceTypeReplicaSet:
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    
    instance: SourceMongodbInstanceTypeReplicaSetInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    server_addresses: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_addresses') }})
    r"""The members of a replica set. Please specify `host`:`port` of each member separated by comma."""
    replica_set: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replica_set'), 'exclude': lambda f: f is None }})
    r"""A replica set in MongoDB is a group of mongod processes that maintain the same data set."""
    
class SourceMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum(str, Enum):
    STANDALONE = 'standalone'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodbInstanceTypeStandaloneMongoDbInstance:
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The host name of the Mongo database."""
    instance: SourceMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""The port of the Mongo database."""
    
class SourceMongodbMongodbEnum(str, Enum):
    MONGODB = 'mongodb'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMongodb:
    r"""The values required to configure the source."""
    
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The database you want to replicate."""
    source_type: SourceMongodbMongodbEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    auth_source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_source'), 'exclude': lambda f: f is None }})
    r"""The authentication source where the user information is stored."""
    instance_type: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_type'), 'exclude': lambda f: f is None }})
    r"""The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""The password associated with this username."""
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""The username which is used to access the database."""
    