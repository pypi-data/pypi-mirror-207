from pathlib import Path
from typing import Dict, Union

from loguru import logger

from pseudopeople.configuration.generator import get_configuration
from pseudopeople.exceptions import ConfigurationError
from pseudopeople.schema_entities import DATASETS


def get_config(dataset_name: str = None, user_config: Union[Path, str, Dict] = None) -> Dict:
    """
    Function that returns the pseudopeople configuration,
    including all default values.
    If :code:`dataset_name` is None (the default), the returned dictionary has exactly
    the structure described on the :ref:`Configuration page <configuration_main>`.
    If a dataset name is supplied, only returns the part of the configuration for that
    dataset, i.e. :code:`get_config(dataset_name)` is equivalent to
    :code:`get_config()[dataset_name]`.

    To get the default probability of omission in the Decennial Census dataset:

    .. code-block:: pycon

        >>> import pseudopeople as psp
        >>> psp.get_config('decennial_census')['row_noise']['omit_row']
        {'row_probability': 0.0145}

    To view that same part of the configuration after applying a user override:

    .. code-block:: pycon

        >>> user_config = {'decennial_census': {'row_noise': {'omit_row': {'row_probability': 0.1}}}}
        >>> psp.get_config('decennial_census', user_config)['row_noise']['omit_row']
        {'row_probability': 0.1}

    :param dataset_name: An optional name of dataset to return the configuration
        for (defaults to all dataset configurations). Providing this argument returns
        the configuration for this specific dataset and no other datasets that exist
        in the configuration. Possible dataset names include:

            - "american_community_survey"
            - "decennial_census"
            - "current_population_survey"
            - "social_security"
            - "taxes_1040"
            - "taxes_w2_and_1099"
            - "women_infants_and_children"
    :param user_config: An optional override to the default configuration. Can be
        a path to a configuration YAML file or a dictionary.
    :return: Dictionary of the config.
    :raises ConfigurationError: An invalid configuration is passed with user_config.

    """

    config = get_configuration(user_config)
    if dataset_name:
        if dataset_name in [dataset.name for dataset in DATASETS]:
            config = config[dataset_name]
        else:
            raise ConfigurationError(
                f"'{dataset_name}' provided but is not a valid option for dataset type."
            )
    if user_config and dataset_name not in user_config.keys():
        logger.warning(
            f"'{dataset_name}' provided but is not in the user provided configuration."
        )

    return config.to_dict()
