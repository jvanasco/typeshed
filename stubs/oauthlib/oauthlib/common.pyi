from _typeshed import Incomplete
from typing import Any

UNICODE_ASCII_CHARACTER_SET: str
CLIENT_ID_CHARACTER_SET: str
SANITIZE_PATTERN: Any
INVALID_HEX_PATTERN: Any
always_safe: str
log: Any

def quote(s, safe: bytes = b"/"): ...
def unquote(s): ...
def urlencode(params): ...
def encode_params_utf8(params): ...
def decode_params_utf8(params): ...

urlencoded: Any

def urldecode(query): ...
def extract_params(raw): ...
def generate_nonce(): ...
def generate_timestamp(): ...
def generate_token(length: int = 30, chars=...): ...
def generate_signed_token(private_pem, request): ...
def verify_signed_token(public_pem, token): ...
def generate_client_id(length: int = 30, chars=...): ...
def add_params_to_qs(query, params): ...
def add_params_to_uri(uri, params, fragment: bool = False): ...
def safe_string_equals(a, b): ...
def to_unicode(data, encoding: str = "UTF-8"): ...

class CaseInsensitiveDict(dict[Any, Any]):
    proxy: Any
    def __init__(self, data) -> None: ...
    def __contains__(self, k): ...
    def __delitem__(self, k) -> None: ...
    def __getitem__(self, k): ...
    def get(self, k, default: Incomplete | None = None): ...
    def __setitem__(self, k, v) -> None: ...
    def update(self, *args, **kwargs) -> None: ...

class Request:
    uri: Any
    http_method: Any
    headers: Any
    body: Any
    decoded_body: Any
    oauth_params: Any
    validator_log: Any
    def __init__(
        self,
        uri,
        http_method: str = "GET",
        body: Incomplete | None = None,
        headers: Incomplete | None = None,
        encoding: str = "utf-8",
    ): ...
    #
    # Start `__getattr__` override
    # attributes managed in `self._params` by `__getattr__` override
    #
    access_token: Any
    client: Any
    client_id: Any
    client_secret: Any
    code: Any
    code_challenge: Any
    code_challenge_method: Any
    code_verifier: Any
    extra_credentials: Any
    grant_type: Any
    redirect_uri: Any
    refresh_token: Any
    request_token: Any
    response_type: Any
    scope: Any
    scopes: Any
    state: Any
    token: Any
    user: Any
    token_type_hint: Any
    # OpenID Connect
    response_mode: Any
    nonce: Any
    display: Any
    prompt: Any
    claims: Any
    max_age: Any
    ui_locales: Any
    id_token_hint: Any
    login_hint: Any
    acr_values: Any
    #
    # END `__getattr__` override
    #
    def __getattr__(self, name: str): ...
    @property
    def uri_query(self): ...
    @property
    def uri_query_params(self): ...
    @property
    def duplicate_params(self): ...
