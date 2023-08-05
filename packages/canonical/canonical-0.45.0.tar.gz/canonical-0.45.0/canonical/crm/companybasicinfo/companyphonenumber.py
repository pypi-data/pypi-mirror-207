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

from canonical import Phonenumber


class CompanyPhonenumber(pydantic.BaseModel):
    kind: Literal['general'] | None = pydantic.Field(
        default=None,
        title="Kind",
        description=(
            "Specifies the kind of phonenumber, or `null` if no specific "
            "kind is known for this number."
        )
    )

    value: Phonenumber = pydantic.Field(
        default=...,
        title="Value",
        description=(
            "Contains the companies' phone number in international format. "
            "International format includes the country code, and is prefixed "
            "with the plus, +, sign. "
        )
    )

    class Config:
        allow_population_by_field_name: bool = True