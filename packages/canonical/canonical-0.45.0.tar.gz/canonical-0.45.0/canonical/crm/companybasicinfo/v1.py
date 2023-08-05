# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

import pydantic

from canonical.fields import ResourceVersionField
from .base import CompanyBasicInfoBase
from .companyaddress import CompanyAddress
from .companychaininfo import CompanyChainInfo
from .companyphonenumber import CompanyPhonenumber


class CompanyBasicInfoV1Spec(pydantic.BaseModel):
    addresses: list[CompanyAddress] = pydantic.Field(
        default=[],
        title="Addresses",
        description="The list of known addresses."
    )

    company_name: str = pydantic.Field(
        default=...,
        title="Name",
        alias='companyName',
        description="The common name of the company."
    )

    chain: CompanyChainInfo = pydantic.Field(
        default_factory=CompanyChainInfo,
        titlte="Chain/franchise information",
        description=(
            "Describes the chain/franchise a business if part of."
        )
    )

    phonenumbers: list[CompanyPhonenumber] = pydantic.Field(
        default=[],
        title="Phonenumbers",
        description=(
            "The list of known phone numbers at which this company may "
            "be contacted."
        )
    )

    website: str | None = pydantic.Field(
        default=None,
        title="Website",
        description="The website of the business, if it has one."
    )

    class Config:
        allow_population_by_field_name: bool = True


class CompanyBasicInfoV1(CompanyBasicInfoBase):
    api_version: Literal['v1'] = ResourceVersionField('v1')
    spec: CompanyBasicInfoV1Spec

    class Config:
        allow_population_by_field_name: bool = True