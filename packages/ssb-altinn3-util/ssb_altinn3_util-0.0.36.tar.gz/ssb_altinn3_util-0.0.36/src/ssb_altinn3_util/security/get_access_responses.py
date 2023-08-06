from pydantic import BaseModel
from typing import List


class GetFormWithGroupsResponse(BaseModel):
    ra_number: str
    survey_number: int
    readers: List[str]
    writers: List[str]


class GetGroupWithRolesAndFormsResponse(BaseModel):
    group_name: str
    direct_roles: List[str]
    inherited_roles: List[str]
    forms_read: List[str]
    forms_write: List[str]


class GetRoleWithGroupsResponse(BaseModel):
    role_name: str
    direct_members: List[str]
    inherited_members: List[str]
