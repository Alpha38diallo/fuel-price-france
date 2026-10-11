from config import *

from logger import logger

from extract import FuelExtractor
from transform import transform_data

from load import (
    get_engine,
    load_dataframe
)


def run():

    logger.info(
        "Début pipeline"
    )

    extractor = FuelExtractor(
        DATASET_ID
    )

    dataframe = (
        extractor.extract_all()
    )

    logger.info(
        f"{len(dataframe)} lignes extraites"
    )

    dataframe = (
        transform_data(
            dataframe
        )
    )

    engine = get_engine(
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME
    )

    load_dataframe(
        dataframe,
        engine
    )

    logger.info(
        "Pipeline terminé"
    )


if __name__ == "__main__":

    run()