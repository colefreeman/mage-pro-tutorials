from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.power_bi import PowerBI
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_in_power_bi(*args, **kwargs):
    """
    Template for loading/refreshing data in Power BI.
    Specify your configuration settings in 'io_config.yaml'.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    dataset_id = 'your_dataset_id'
    parameters = {
        # Specify your parameters to perform an enhanced refresh operation.
        # For example: 'type': 'full', 'retryCount': 2
    }

    powerbi = PowerBI.with_config(ConfigFileLoader(config_path, config_profile))
    powerbi.load(dataset_id, parameters)

    # Add aditional logic or create a separate block for retrieving
    # and passing any output data produced by this block run.
    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'