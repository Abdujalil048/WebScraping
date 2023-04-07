import logging


class ColoredFormatter(logging.Formatter):
    reset = "\x1b[0m"
    red = "\x1b[31;20m"
    gray = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    bold_red = "\x1b[31;1m"
    fmt = "%(asctime)s [%(name)s:%(levelname)s] - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: gray,
        logging.INFO: gray,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno) + self.fmt + self.reset
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


colored_handler = logging.StreamHandler()

colored_handler.setFormatter(ColoredFormatter())

log_config = {
    'handlers': [colored_handler],
    'datefmt': '%m-%d-%Y %H:%M:%S'
}
