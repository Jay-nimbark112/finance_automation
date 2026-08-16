import logging
from pathlib import Path

def setup_logger():

    BASE_DIR = Path(__file__).resolve().parent.parent

    logs_folder =BASE_DIR / "logs"

    #create logs folder
    logs_folder.mkdir(
        exist_ok=True
    )

    log_file = logs_folder / "automation.log"

    #configuration logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    return logging.getLogger("automation")

