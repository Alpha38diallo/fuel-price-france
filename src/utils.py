import requests
import time


def request_with_retry(
    url,
    params=None,
    retries=3,
    delay=5
):

    for attempt in range(retries):

        try:

            response = requests.get(
                url,
                params=params,
                timeout=60
            )

            response.raise_for_status()

            return response

        except Exception:

            time.sleep(delay)

    raise Exception(
        "API indisponible"
    )
