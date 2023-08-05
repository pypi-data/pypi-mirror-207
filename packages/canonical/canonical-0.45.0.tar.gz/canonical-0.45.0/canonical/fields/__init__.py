# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic


__all__: list[str] = [
    'ResourceKindField'
]


def ResourceVersionField(version: str) -> Any:
    return pydantic.Field(
        default=version,
        alias='apiVersion',
        title='API Version',
        description=(
            "The `apiVersion` property defines the versioned schema of this "
            "representation of an object. Servers should convert recognized "
            "schemas to the latest internal value, and may reject "
            "unrecognized values. More info: https://git.k8s.io/community/"
            "contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
        enum=[version]
    )


def ResourceKindField() -> Any:
    return pydantic.Field(
        default=...
    )