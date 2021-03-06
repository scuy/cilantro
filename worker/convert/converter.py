import logging
from PIL import Image


def convert_tif2jpg(source_file, target_file):
    if source_file != target_file:
        logging.getLogger(__name__).debug("Converting %s to %s", source_file,
                                          target_file)
        Image.open(source_file).save(target_file)
