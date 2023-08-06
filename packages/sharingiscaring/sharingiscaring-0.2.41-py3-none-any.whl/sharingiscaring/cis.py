from pydantic import BaseModel, Extra, Field
import datetime as dt
from typing import Union
from enum import Enum
import io
import base58
from sharingiscaring.GRPCClient import GRPCClient
from sharingiscaring.GRPCClient.CCD_Types import *

from sharingiscaring.enums import NET
from rich import print
import math

LEN_ACCOUNT_ADDRESS = 50


# Metadata classes
class TokenAttribute(BaseModel):
    type: str
    name: str
    value: str


class TokenDisplay(BaseModel):
    url: str
    hash: str = None


class TokenMetaData(BaseModel):
    name: str
    unique: bool
    description: str
    attributes: list[TokenAttribute] = None
    display: TokenDisplay
    thumbnail: TokenDisplay = None


# class MongoTypeTokenHolder(BaseModel):
#     account_address: CCD_AccountAddress
#     token_amount: str


class MongoTypeTokenForAddress(BaseModel):
    token_address: str
    contract: str
    token_id: str
    token_amount: str


class MongoTypeTokenHolderAddress(BaseModel):
    id: str = Field(..., alias="_id")
    tokens: dict[str, MongoTypeTokenForAddress]


class MongoTypeTokenAddress(BaseModel):
    id: str = Field(..., alias="_id")
    contract: str
    token_id: str
    token_amount: str = None
    metadata_url: str = None
    last_height_processed: int
    token_holders: dict[CCD_AccountAddress, str] = None


class MongoTypeLoggedEvent(BaseModel):
    id: str = Field(..., alias="_id")
    logged_event: str
    result: dict
    tag: int
    event_type: str
    block_height: int
    tx_hash: str
    token_address: str
    contract: str


# CIS
class StandardIdentifiers(Enum):
    CIS_0 = "CIS-0"
    CIS_1 = "CIS-1"
    CIS_2 = "CIS-2"


class LoggedEvents(Enum):
    transfer_event = 255
    mint_event = 254
    burn_event = 253
    metadata_event = 251


# CIS-2 Logged Event Types


class transferEvent(BaseModel):
    tag: int
    token_id: str = None
    token_amount: int = None
    from_address: str = None
    to_address: str = None


class mintEvent(BaseModel):
    tag: int
    token_id: str = None
    token_amount: int = None
    to_address: str = None


class burnEvent(BaseModel):
    tag: int
    token_id: str = None
    token_amount: int = None
    from_address: str = None


class updateOperatorEvent(BaseModel):
    tag: int
    operator_update: str = None
    owner: str = None
    operator: str = None


class MetadataUrl(BaseModel):
    url: str
    checksum: str = None


class tokenMetadataEvent(BaseModel):
    tag: int
    token_id: str
    metadata: MetadataUrl


class CIS:
    def __init__(
        self,
        grpcclient: GRPCClient = None,
        instance_index=None,
        instance_subindex=None,
        entrypoint=None,
        net: NET.MAINNET = None,
    ):
        self.grpcclient = grpcclient
        self.instance_index = instance_index
        self.instance_subindex = instance_subindex
        self.entrypoint = entrypoint
        self.net = net

    def standard_identifier(self, identifier: StandardIdentifiers) -> bytes:
        si = io.BytesIO()
        # write the length of ASCII characters for the identifier
        number = len(identifier.value)
        byte_array = number.to_bytes(1, "little")
        si.write(byte_array)
        # write the identifier
        si.write(bytes(identifier.value, encoding="ASCII"))
        # convert to bytes
        return si.getvalue()

    def supports_parameter(self, standard_identifier: StandardIdentifiers) -> bytes:
        sp = io.BytesIO()
        # write the number of standardIdentifiers present
        number = 1
        byte_array = number.to_bytes(2, "little")
        sp.write(byte_array)
        # write the standardIdentifier
        sp.write(self.standard_identifier(standard_identifier))
        # convert to bytes
        return sp.getvalue()

    def support_result(self, bs: io.BytesIO):
        t = int.from_bytes(bs.read(2), byteorder="little")
        if t == 0:
            return t, "Standard is not supported"
        elif t == 1:
            return t, "Standard is supported by this contract"
        elif t == 2:
            contracts = []
            n = int.from_bytes(bs.read(1), byteorder="little")
            for _ in range(n):
                contracts.append(self.contract_address(bs))
                return (
                    t,
                    "Standard is supported by using one of these contract addresses: "
                    + [x for x in contracts],
                )

    def supports_response(self, res: bytes):
        bs = io.BytesIO(bytes.fromhex(res.decode()))
        if bs.getbuffer().nbytes > 0:
            n = int.from_bytes(bs.read(2), byteorder="big")
            responses = []
            for _ in range(n):
                responses.append(self.support_result(bs))
            return responses[0]
        else:
            return False, "Lookup Failure"

    def supports_standard(self, standard_identifier: StandardIdentifiers) -> bool:
        parameter_bytes = self.supports_parameter(standard_identifier)

        ii = self.grpcclient.invoke_instance(
            "last_final",
            self.instance_index,
            self.instance_subindex,
            self.entrypoint,
            parameter_bytes,
            self.net,
        )

        res = ii.success.return_value
        support_result, support_result_text = self.supports_response(res)

        return support_result == 1

    def balanceOf(self, block_hash: str, tokenID: str, account_id: str):
        parameter_bytes = self.balanceOfParameter(tokenID, account_id)

        ii = self.grpcclient.invoke_instance(
            block_hash,
            self.instance_index,
            self.instance_subindex,
            self.entrypoint,
            parameter_bytes,
            self.net,
        )

        res = ii.success.return_value
        support_result = self.balanceOfResponse(res)

        return support_result, ii

    # def supports_parameter(self, standard_identifier: StandardIdentifiers) -> bytes:
    #     sp = io.BytesIO()
    #     # write the number of standardIdentifiers present
    #     number = 2
    #     byte_array = number.to_bytes(1, "little")
    #     sp.write(byte_array)

    #     # write the standardIdentifier
    #     si = io.BytesIO()
    #     # write the length of ASCII characters for the identifier
    #     identifier = StandardIdentifiers.CIS_1
    #     number = len(identifier.value)
    #     byte_array = number.to_bytes(1, "little")
    #     si.write(byte_array)
    #     # write the identifier
    #     si.write(bytes(identifier.value, encoding="ASCII"))
    #     sp.write(si)
    #     si = io.BytesIO()
    #     identifier = StandardIdentifiers.CIS_1
    #     # write the length of ASCII characters for the identifier
    #     number = len(identifier.value)
    #     byte_array = number.to_bytes(1, "little")
    #     si.write(byte_array)
    #     # write the identifier
    #     si.write(bytes(identifier.value, encoding="ASCII"))
    #     sp.write(si)
    #     # convert to bytes
    #     return sp.getvalue()

    # def supportsParameter(self) -> bytes:
    #     sp = io.BytesIO()
    #     # write the number of standardIdentifiers present
    #     number = len(StandardIdentifiers)
    #     byte_array = number.to_bytes(2, "little")
    #     sp.write(byte_array)

    #     for standard in StandardIdentifiers:
    #         # write the standardIdentifier
    #         sp.write(self.standardIdentifier(standard.value))
    #     # convert to bytes
    #     return sp.getvalue()

    def account_address(self, bs: io.BytesIO):
        addr = bs.read(32)
        return base58.b58encode_check(b"\x01" + addr).decode()

    def contract_address(self, bs: io.BytesIO):
        return int.from_bytes(bs.read(8), byteorder="little"), int.from_bytes(
            bs.read(8), byteorder="little"
        )

    def address(self, bs: io.BytesIO):
        t = int.from_bytes(bs.read(1), byteorder="little")
        if t == 0:
            return self.account_address(bs)
        elif t == 1:
            return self.contract_address(bs)
        else:
            raise Exception("invalid type")

    def receiver(self, bs: io.BytesIO):
        t = int.from_bytes(bs.read(1), byteorder="little")
        if t == 0:
            return self.account_address(bs)
        elif t == 1:
            return self.contract_address(bs), self.receiveHookName(bs)
        else:
            raise Exception("invalid type")

    def url(self, n: int, bs: io.BytesIO):
        data = bs.read(n)
        return data

    def metadataChecksum(self, bs: io.BytesIO):
        t = int.from_bytes(bs.read(1), byteorder="little")
        if t == 0:
            return None
        elif t == 1:
            return bs.read(32)
        else:
            raise Exception("invalid type")

    def metadataUrl(self, bs: io.BytesIO):
        n = int.from_bytes(bs.read(2), byteorder="little")
        url = bs.read(n).decode()
        # checksum = self.metadataChecksum(bs)
        return MetadataUrl(**{"url": url, "checksum": None})

    def tokenAmount(self, bs: io.BytesIO):
        return int.from_bytes(bs.read(8), byteorder="little")

    def receiveHookName(self, bs: io.BytesIO):
        n = int.from_bytes(bs.read(2), byteorder="little")
        name = bs.read(n)
        return bytes.decode(name, "UTF-8")

    def additionalData(self, bs: io.BytesIO):
        n = int.from_bytes(bs.read(2), byteorder="little")
        data = bs.read(n)
        return data

    def tokenID(self, bs: io.BytesIO):
        n = int.from_bytes(bs.read(1), byteorder="little")
        return bytes.hex(bs.read(n))

    def balanceOfQuery(self, tokenID: str, address: str):
        sp = io.BytesIO()

        tokenID = self.generate_tokenID(tokenID)
        address = self.generate_address(address)
        sp.write(tokenID)
        sp.write(address)
        return sp.getvalue()

    def balanceOfParameter(self, tokenID: str, address: str):
        sp = io.BytesIO()

        sp.write(int(1).to_bytes(2, "little"))
        sp.write(self.balanceOfQuery(tokenID, address))
        # convert to bytes
        return sp.getvalue()

    def balanceOfResponse(self, res: bytes):
        bs = io.BytesIO(bytes.fromhex(res.decode()))
        n = int.from_bytes(bs.read(2), byteorder="little")
        result = self.tokenAmount(bs)

        return result

    def generate_tokenID(self, tokenID: str):
        sp = io.BytesIO()

        tokenID_in_bytes = bytes.fromhex(tokenID)

        sp.write(int(len(tokenID_in_bytes)).to_bytes(1, "little"))
        sp.write(tokenID_in_bytes)
        return sp.getvalue()

    def generate_account_address(self, address: str):
        return bytearray(base58.b58decode_check(address)[1:])

    def generate_contract_address(self, address: str):
        # TODO
        sp = io.BytesIO()

        address_in_bytes = bytes.fromhex(address.encode("utf-8"))

        sp.write(address_in_bytes)
        return sp.getvalue()

    def generate_address(self, address: str):
        sp = io.BytesIO()

        if len(address) == 50:
            sp.write(int(0).to_bytes(1, "little"))
            sp.write(self.generate_account_address(address))
        else:
            sp.write(int(1).to_bytes(1, "little"))
            sp.write(self.generate_contract_address(address))

        return sp.getvalue()

    def invoke_token_metadataUrl(self, tokenID: str) -> bool:
        parameter_bytes = self.tokenMetadataParameter(tokenID)

        ii = self.grpcclient.invoke_instance(
            "last_final",
            self.instance_index,
            self.instance_subindex,
            self.entrypoint,
            parameter_bytes,
            self.net,
        )

        res = ii.success.return_value
        return self.tokenMetadataResultParameter(res)

    def tokenMetadataParameter(self, tokenID: str):
        sp = io.BytesIO()

        sp.write(int(1).to_bytes(2, "little"))
        # write the standardIdentifier
        # sp.write(bytearray(self.bytes_from_hex_tokenID(tokenID)))
        sp.write(self.generate_tokenID(tokenID))
        # convert to bytes
        return sp.getvalue()

    def metadata_result(self, bs: bytes):
        n = int(bs[:2].decode("ASCII"))
        bs = io.BytesIO(bs)
        bs.read(2)
        url = self.url(n, bs)
        return url

    def metadata_response(self, bs: bytes):
        # bs: io.BytesIO = io.BytesIO(bs)
        if len(bs) > 0:
            n = int(bs[:2].decode("ASCII"))
            # n = int.from_bytes(bs.read(2), byteorder="big")
            responses = []
            for _ in range(n):
                responses.append(self.metadata_result(bs))
            return responses[0]
        else:
            return False, "Lookup Failure"

    def tokenMetadataResultParameter(self, res: bytes):
        bs = io.BytesIO(bytes.fromhex(res.decode()))
        n = int.from_bytes(bs.read(2), byteorder="little")
        results = []
        for _ in range(0, n):
            results.append(self.metadataUrl(bs))

        return results

    def operator_update(self, bs: io.BytesIO):
        n = int.from_bytes(bs.read(1), byteorder="little")
        if n == 0:
            return "Remove operator"
        elif n == 1:
            return "Add operator"

    def token_id(self, bs: io.BytesIO):
        n = int.from_bytes(bs.read(1), byteorder="little")
        return bytes.hex(bs.read(n))

    def token_amount(self, bs: io.BytesIO):
        x = int.from_bytes(bs.read(1), byteorder="little")
        if x < math.pow(2, 7):
            return x
        else:
            m = self.token_amount(bs)
            return (x - math.pow(2, 7)) + (math.pow(2, 7) * m)

    def transferEvent(self, hexParameter: str):
        bs = io.BytesIO(bytes.fromhex(hexParameter))

        tag_ = int.from_bytes(bs.read(1), byteorder="little")
        token_id_ = self.token_id(bs)
        amount_ = self.token_amount(bs)

        from_ = self.address(bs)
        if type(from_) is not tuple:
            # it's an account address
            if len(from_) != LEN_ACCOUNT_ADDRESS:
                return None

        if type(from_) == tuple:
            from_ = f"<{from_[0]},{from_[1]}>"
        to_ = self.address(bs)
        if type(to_) is not tuple:
            # it's an account address
            if len(to_) != LEN_ACCOUNT_ADDRESS:
                return None

        if type(to_) == tuple:
            to_ = f"<{to_[0]},{to_[1]}>"

        return transferEvent(
            **{
                "tag": tag_,
                "token_id": token_id_,
                "token_amount": amount_,
                "from_address": from_,
                "to_address": to_,
            }
        )

    def updateOperatorEvent(self, hexParameter: str):
        bs = io.BytesIO(bytes.fromhex(hexParameter))

        tag_ = int.from_bytes(bs.read(1), byteorder="little")
        # token_id_ = self.token_id(bs)
        update_ = self.operator_update(bs)

        owner_ = self.address(bs)
        if type(owner_) is not tuple:
            # it's an account address
            if len(owner_) != LEN_ACCOUNT_ADDRESS:
                return None

        if type(owner_) == tuple:
            owner_ = f"<{owner_[0]},{owner_[1]}>"
        operator_ = self.address(bs)
        if type(operator_) is not tuple:
            # it's an account address
            if len(operator_) != LEN_ACCOUNT_ADDRESS:
                return None

        if type(operator_) == tuple:
            operator_ = f"<{operator_[0]},{operator_[1]}>"

        return updateOperatorEvent(
            **{
                "tag": tag_,
                "operator_update": update_,
                "owner": owner_,
                "operator": operator_,
            }
        )

    def mintEvent(self, hexParameter: str):
        bs = io.BytesIO(bytes.fromhex(hexParameter))

        tag_ = int.from_bytes(bs.read(1), byteorder="little")
        token_id_ = self.token_id(bs)
        amount_ = self.token_amount(bs)
        to_ = self.address(bs)
        if type(to_) is not tuple:
            # it's an account address
            if len(to_) != LEN_ACCOUNT_ADDRESS:
                return None

        if type(to_) == tuple:
            to_ = f"<{to_[0]},{to_[1]}>"

        return mintEvent(
            **{
                "tag": tag_,
                "token_id": token_id_,
                "token_amount": amount_,
                "to_address": to_,
            }
        )

    def burnEvent(self, hexParameter: str):
        bs = io.BytesIO(bytes.fromhex(hexParameter))

        tag_ = int.from_bytes(bs.read(1), byteorder="little")
        token_id_ = self.token_id(bs)
        amount_ = self.token_amount(bs)
        from_ = self.address(bs)
        if type(from_) is not tuple:
            # it's an account address
            if len(from_) != LEN_ACCOUNT_ADDRESS:
                return None

        if type(from_) == tuple:
            from_ = f"<{from_[0]},{from_[1]}>"

        return burnEvent(
            **{
                "tag": tag_,
                "token_id": token_id_,
                "token_amount": amount_,
                "from_address": from_,
            }
        )

    def tokenMetaDataEvent(self, hexParameter: str):
        bs = io.BytesIO(bytes.fromhex(hexParameter))

        tag_ = int.from_bytes(bs.read(1), byteorder="little")

        token_id_ = self.token_id(bs)
        metadata_ = self.metadataUrl(bs)

        return tokenMetadataEvent(
            **{
                "tag": tag_,
                "token_id": token_id_,
                "metadata": metadata_,
            }
        )

    def process_log_events(self, hexParameter: str):
        bs = io.BytesIO(bytes.fromhex(hexParameter))

        tag_ = int.from_bytes(bs.read(1), byteorder="little")
        if tag_ == 255:
            try:
                event = self.transferEvent(hexParameter)
                return tag_, event
            except:
                return tag_, None
        elif tag_ == 254:
            try:
                event = self.mintEvent(hexParameter)
                return tag_, event
            except:
                return tag_, None
        elif tag_ == 253:
            try:
                event = self.burnEvent(hexParameter)
                return tag_, event
            except:
                return tag_, None
        elif tag_ == 252:
            try:
                event = self.updateOperatorEvent(hexParameter)
                return tag_, event
            except:
                return tag_, None
        elif tag_ == 251:
            try:
                event = self.tokenMetaDataEvent(hexParameter)
                return tag_, event
            except:
                return tag_, None
        else:
            return tag_, f"Custom even with tag={tag_}."
