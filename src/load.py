from sqlalchemy import create_engine


def get_engine(
    user,
    password,
    host,
    port,
    dbname
):

    if password:

        connection_string = (
            f"postgresql://"
            f"{user}:{password}"
            f"@{host}:{port}/{dbname}"
        )

    else:

        connection_string = (
            f"postgresql://"
            f"{user}@{host}:{port}/{dbname}"
        )

    return create_engine(
        connection_string
    )


def load_dataframe(
    dataframe,
    engine
):

    dataframe.to_sql(
        "fuel_prices",
        con=engine,
        if_exists="replace",
        index=False
    )