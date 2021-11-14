from dotenv import load_dotenv
import json


def retrieveCurrentEnv(filePath: str) -> str:
    with open(filePath, "r") as jsonfile:
        cfg = json.load(jsonfile)
        return cfg["file"]


def load_dotenvHandler():
    load_dotenv(
        "./environments/{envName}.env".format(
            envName=retrieveCurrentEnv("./environments/env.config.json")
        )
    )
