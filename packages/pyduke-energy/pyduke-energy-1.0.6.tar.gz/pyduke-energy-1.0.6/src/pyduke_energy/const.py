"""Constant Defintions."""

CUST_API_BASE_URL = "https://cust-api.duke-energy.com/gep/v2/"
CUST_PILOT_API_BASE_URL = "https://cust-pilot-api.duke-energy.com/"
IOT_API_BASE_URL = "https://app-core1.de-iot.io/rest/cloud/"
FASTPOLL_ENDPOINT = "smartmeter/fastpoll/start"
OAUTH_ENDPOINT = "auth/oauth2/token"
SMARTMETER_AUTH_ENDPOINT = "smartmeter/v1/auth"
ACCT_ENDPOINT = "auth/account-list"
ACCT_DET_ENDPOINT = "auth/account-details"
GW_STATUS_ENDPOINT = "gw/gateways/status"
GW_USAGE_ENDPOINT = "smartmeter/usageByHour"

# hard-coded from Android app
BASIC_AUTH = (
    "Basic ZEJEMnl0TE1IYm9UMjBNNDRkQVRqM29JelNoUG15NGQ6ODZ0QW1zVXFZcmV3R3N2WA=="
)

DEFAULT_TIMEOUT = 10  # seconds

MQTT_HOST = "app-core1.de-iot.io"
MQTT_PORT = 443
MQTT_ENDPOINT = "/app-mqtt"
MQTT_KEEPALIVE = 50  # Seconds, it appears the server will disconnect after 60s idle

# in minutes, how long a fastpoll interval is
FASTPOLL_TIMEOUT_MIN = 15

# in seconds, how long to until the fastpoll request has timed out and a new one needs to be made
FASTPOLL_TIMEOUT_SEC = (FASTPOLL_TIMEOUT_MIN * 60) - 3  # seconds

# in seconds, how long to wait for a message before retrying fastpoll or reconnecting
MESSAGE_TIMEOUT_SEC = 60

# number of times a message timeout can occur before just reconnecting
MESSAGE_TIMEOUT_RETRY_COUNT = 3

# number of times a message timeout can occur before we totally give up (allow 2 fastpolls)
MESSAGE_TIMEOUT_GIVE_UP_COUNT = 2 * FASTPOLL_TIMEOUT_MIN * 60 / MESSAGE_TIMEOUT_SEC

# in minutes, minimum amount of time to wait before retrying connection on forever loop
FOREVER_RETRY_MIN_MINUTES = 1

# in minutes, maximum amount of time to wait before trying connection on forever loop
FOREVER_RETRY_MAX_MINUTES = 60

# in seconds, how long to wait for a connection before timing out
CONNECT_TIMEOUT_SEC = 60
