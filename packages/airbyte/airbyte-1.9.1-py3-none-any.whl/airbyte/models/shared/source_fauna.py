"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceFaunaCollectionDeletionsEnabledDeletionModeEnum(str, Enum):
    DELETED_FIELD = 'deleted_field'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaunaCollectionDeletionsEnabled:
    r"""<b>This only applies to incremental syncs.</b> <br>
    Enabling deletion mode informs your destination of deleted documents.<br>
    Disabled - Leave this feature disabled, and ignore deleted documents.<br>
    Enabled - Enables this feature. When a document is deleted, the connector exports a record with a \"deleted at\" column containing the time that the document was deleted.
    """
    
    column: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column') }})
    r"""Name of the \\"deleted at\\" column."""
    deletion_mode: SourceFaunaCollectionDeletionsEnabledDeletionModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletion_mode') }})
    
class SourceFaunaCollectionDeletionsDisabledDeletionModeEnum(str, Enum):
    IGNORE = 'ignore'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaunaCollectionDeletionsDisabled:
    r"""<b>This only applies to incremental syncs.</b> <br>
    Enabling deletion mode informs your destination of deleted documents.<br>
    Disabled - Leave this feature disabled, and ignore deleted documents.<br>
    Enabled - Enables this feature. When a document is deleted, the connector exports a record with a \"deleted at\" column containing the time that the document was deleted.
    """
    
    deletion_mode: SourceFaunaCollectionDeletionsDisabledDeletionModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletion_mode') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaunaCollection:
    r"""Settings for the Fauna Collection."""
    
    deletions: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletions') }})
    r"""<b>This only applies to incremental syncs.</b> <br>
    Enabling deletion mode informs your destination of deleted documents.<br>
    Disabled - Leave this feature disabled, and ignore deleted documents.<br>
    Enabled - Enables this feature. When a document is deleted, the connector exports a record with a \"deleted at\" column containing the time that the document was deleted.
    """
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size') }})
    r"""The page size used when reading documents from the database. The larger the page size, the faster the connector processes documents. However, if a page is too large, the connector may fail. <br>
    Choose your page size based on how large the documents are. <br>
    See <a href=\"https://docs.fauna.com/fauna/current/learn/understanding/types#page\">the docs</a>.
    """
    
class SourceFaunaFaunaEnum(str, Enum):
    FAUNA = 'fauna'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFauna:
    r"""The values required to configure the source."""
    
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    r"""Domain of Fauna to query. Defaults db.fauna.com. See <a href=https://docs.fauna.com/fauna/current/learn/understanding/region_groups#how-to-use-region-groups>the docs</a>."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""Endpoint port."""
    scheme: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme') }})
    r"""URL scheme."""
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""Fauna secret, used when authenticating with the database."""
    source_type: SourceFaunaFaunaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    collection: Optional[SourceFaunaCollection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection'), 'exclude': lambda f: f is None }})
    r"""Settings for the Fauna Collection."""
    