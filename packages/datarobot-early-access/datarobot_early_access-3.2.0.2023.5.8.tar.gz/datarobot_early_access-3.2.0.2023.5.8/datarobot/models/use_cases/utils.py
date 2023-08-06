#
# Copyright 2023 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
from typing import Any, Dict, List, Optional, Union


def resolve_use_case(
    params: Dict[str, Any],
    use_case_id: Optional[Union[str, List[str]]] = None,
    use_case_key: str = "experiment_container_id",
) -> Dict[str, Any]:
    """
    Add a global Use Case ID to query params for a list operation if no use_case_id has been passed
    This method supports checking for `use_case_id` in a params dict if users can build their own params dict.
    Parameters
    ----------
    params : Dict[str, Any]
        The query params dict to add a Use Case ID to, if a global ID exists, or if one was passed in directly.
    use_case_id : Optional[Union[str, List[str]]]
        Optional. The use case ID to add to a query params dict.
    use_case_key : Optional[str]
        Optional. The key that will be used in the query params for Use Case ID. Default is 'experiment_container_id'.
    Returns
    -------
    params : Dict[str, Any]
        If a Use Case ID is available, the params with the ID added. Otherwise, return the dict unmodified.
    """
    # Check to see if a use_case_id is already in the params dict
    if not params.get(use_case_key):
        # If use_case_id is not in the dict, add in the manually passed value, if it exists
        params[use_case_key] = use_case_id
    return params
