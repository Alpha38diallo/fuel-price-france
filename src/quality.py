def validate_data(df):

    if df.empty:

        raise ValueError(
            "Dataset vide"
        )

    return True