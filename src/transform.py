import json

from quality import validate_data


def transform_data(df):

    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )

    # Conversion des listes/dictionnaires en texte

    for col in df.columns:

        df[col] = df[col].apply(

            lambda x: json.dumps(x)

            if isinstance(x, (list, dict))

            else x

        )

    df = df.drop_duplicates()

    validate_data(df)

    return df