from typing import Any, Dict, Optional

from pydantic import BaseModel, Extra, Field


class OrganizationUpdate(BaseModel):
    class Config:
        extra = Extra.ignore

    key: Optional[str] = Field(
        None,
        description="A URL-friendly name of the organization (i.e: slug). You will be able to query later using this key instead of the id (UUID) of the organization.",
        title="Key",
    )
    name: Optional[str] = Field(
        None,
        description="The name of the organization, usually it's your company's name.",
        title="Name",
    )
    settings: Optional[Dict[str, Any]] = Field(
        None, description="the settings for this project", title="Settings"
    )
