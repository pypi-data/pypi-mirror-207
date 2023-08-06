from typing import List, TypedDict


class ClientWhitelist(TypedDict):
    list_id: int
    sorted_addresses: List[str]
    is_draft: bool


class ClientWhitelistHashInput(TypedDict):
    owner_address: str
    safe_address: str
    list_contents: List[str]
    sub: str
    network_id: int


class ClientWhitelistHash(TypedDict):
    hash_input: ClientWhitelistHashInput
    hash: str
