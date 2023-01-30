import logging

import azure.functions as func
import json

from GetPerson.executor import Executor


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        executor_obj = Executor()
        person_email = executor_obj.execute()

        return func.HttpResponse(
            json.dumps({"email": person_email}),
            status_code=200,
        )

    except Exception as e:
        logging.exception(f"An error occurred - {e}")
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. But an internal error occurred, check Application logs.",
            status_code=200,
        )
