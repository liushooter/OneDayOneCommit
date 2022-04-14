import logging
import logging_loki

handler = logging_loki.LokiHandler(
    url="http://127.0.0.1:3100/loki/api/v1/push",
    # 方便 Query
    tags={"application": "Demo"},
    version="1",
)

logger = logging.getLogger("logger")
logger.addHandler(handler)

for i in range(1, 10):
    logger.error(
    f"ERROR Test - {i}",
    extra={"tags": {"service": "tunnel"}},
    )

"""
export LOKI_ADDR=http://localhost:3100

logcli query '{application="Demo"}'
"""
