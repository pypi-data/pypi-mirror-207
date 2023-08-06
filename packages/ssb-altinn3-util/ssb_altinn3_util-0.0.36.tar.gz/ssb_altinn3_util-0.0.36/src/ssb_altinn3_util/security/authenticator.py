from typing import List

from fastapi import Request, HTTPException

from ssb_altinn3_util.security.authorization_result import AuthorizationResult
from ssb_altinn3_util.security.helpers import jwt_helper
from ssb_altinn3_util.security.helpers import auth_service_client

import ssb_altinn3_util.security.authenticator_constants as constants


class Authenticator:
    """
    Authorization component to be injected in api-endpoint as a dependency.  Requires the following to function
    properly:
    Env variable AUTH_SERVICE_URL must be set with the full absolute url to the authorization service endpoint.
    The request object (fastapi.Request) must be present as a function argument in the function using the component.
    The role-argument must be one of the roles defined in authenticator_constants (in ssb_altinn3_util.security).

    Form access must be validated in the actual endpoint code, calling the verify_read_access or verify_write_access
    function of the authenticator.  Example:

    @app.get("/stuff")
    def do_stuff(form: str, request: Request, auth: Authenticator = Depends(Authenticator(role="<role>"):
        auth.verify_read_access(form)
        ....

    Multiple roles can be specified as well, if an endpoint is available for more than one role.  This is done by
    adding the roles as a string, separating the different roles with a comma.  Note that this will grant access
    if ANY of the roles are owned by the user.  Example:

    @app.get("/stuff")
    def do_stuff(form: str, request: Request, auth: Authenticator = Depends(Authenticator(role="<role1>,<role2>"):
        auth.verify_write_access(form)
        ....

    """

    required_roles: List[str]
    allowed_forms_read: List[str]
    allowed_forms_write: List[str]

    def __init__(self, role: str):
        if not role:
            raise ValueError("No role supplied to Authenticator")
        roles = role.split(",")
        for r in roles:
            if r not in constants.VALID_ROLES:
                raise ValueError(f"Supplied role '{r}' is not a valid role!")
        self.required_roles = roles
        self.allowed_forms_read = []
        self.allowed_forms_write = []

    def __call__(self, request: Request):
        auth_header = request.headers.get("authorization", None)
        if not auth_header:
            raise HTTPException(status_code=401, detail="No token provided")
        user_email = jwt_helper.get_user_email_from_token(auth_header)
        if not user_email:
            raise HTTPException(
                status_code=401, detail="Unable to find user email in supplied token!"
            )

        result: AuthorizationResult or None = None
        for role in self.required_roles:
            result = auth_service_client.verify_access(
                user_email, role
            )
            if result.access_granted:
                break

        if result is None:
            raise HTTPException(
                status_code=400, detail="Unable to verify supplied roles."
            )
        if not result.access_granted:
            raise HTTPException(
                status_code=result.status_code, detail=result.error_message
            )
        self.allowed_forms_read = result.allowed_forms_read
        self.allowed_forms_write = result.allowed_forms_write
        return self

    def verify_form_read_access(self, form: str) -> bool:
        allowed_forms = set(self.allowed_forms_read + self.allowed_forms_write)
        if (
            constants.FORM_ACCESS_ALL in allowed_forms
            or form in allowed_forms
        ):
            return True
        raise HTTPException(
            status_code=403, detail=f"User has insufficient access to form '{form}'"
        )

    def verify_form_write_access(self, form: str) -> bool:
        if (
            constants.FORM_ACCESS_ALL in self.allowed_forms_write
            or form in self.allowed_forms_write
        ):
            return True
        raise HTTPException(
            status_code=403, detail=f"User has insufficient access to form '{form}'"
        )
