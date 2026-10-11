import pandas as pd

from logger import logger
from utils import request_with_retry


class FuelExtractor:

    BASE_URL = (
        "https://data.economie.gouv.fr/api/explore/v2.1"
    )

    def __init__(self, dataset_id):

        self.dataset_id = dataset_id

    def extract_all(self):

        offset = 0
        limit = 100

        rows = []

        while True:

            url = (
                f"{self.BASE_URL}"
                "/catalog/datasets/"
                f"{self.dataset_id}"
                "/records"
            )

            params = {
                "limit": limit,
                "offset": offset
            }

            response = request_with_retry(
                url,
                params=params
            )

            data = response.json()

            records = data.get(
                "results",
                []
            )

            if not records:
                break

            rows.extend(records)

            offset += limit

            logger.info(
                f"{len(rows)} lignes récupérées"
            )

        return pd.json_normalize(rows)