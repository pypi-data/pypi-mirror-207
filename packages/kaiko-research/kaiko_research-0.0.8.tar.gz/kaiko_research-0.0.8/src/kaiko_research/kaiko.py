import pandas as pd
import importlib
from kaiko_research.api_client import DataAPIClient
from kaiko_research.research_intelligence import ApplyResearchIntelligence
from kaiko_research.list_of_exports import list_of_exports
from datetime import datetime


class KaikoAPIWrapper:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_export_types(self):
        return pd.DataFrame(list_of_exports)[["export_type", "export_name"]]

    def get_export_parameters(self, export_name):
        schemas = importlib.import_module("kaiko_research.endpoint_schemas")
        schema_name = [
            _["schema_name"] for _ in list_of_exports if _["export_name"] == export_name
        ][0]
        schema = getattr(schemas, schema_name)
        return pd.DataFrame(schema)

    def gen_data(self, export_name, export_parameters={}):
        # Create an instance of API client
        api_client = DataAPIClient(self.api_key, export_parameters)
        data = {}
        exports = pd.DataFrame(list_of_exports)
        if (
            export_name
            in exports.loc[
                exports["export_type"] == "Research intelligence", "export_name"
            ].tolist()
        ):
            intelligence_client = ApplyResearchIntelligence(
                self.api_key, export_parameters
            )
            if export_name == "Exchage volume USD":
                data = intelligence_client.exchange_volume_usd()
                return data

        # Make a request to the API and retrieve the data
        data = api_client.fetch_data_batches(export_name)
        # Output the results
        return data

    def output_data(self, export_name, data, output_path):
        today = datetime.now().date()
        data.to_csv(f"{output_path}/{today} - {export_name}.csv", index=False)
        # Write the data to a file or print it to the console
        pass
