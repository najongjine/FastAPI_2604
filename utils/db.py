import os
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import psycopg
from dotenv import load_dotenv

load_dotenv()

ALLOWED_POSTGRES_PARAMS = {
    "application_name",
    "connect_timeout",
    "dbname",
    "fallback_application_name",
    "gssencmode",
    "host",
    "hostaddr",
    "keepalives",
    "keepalives_count",
    "keepalives_idle",
    "keepalives_interval",
    "load_balance_hosts",
    "options",
    "passfile",
    "password",
    "port",
    "replication",
    "require_auth",
    "requiressl",
    "service",
    "sslcert",
    "sslcompression",
    "sslcrl",
    "sslcrldir",
    "sslkey",
    "sslmode",
    "sslnegotiation",
    "sslpassword",
    "sslrootcert",
    "sslsni",
    "target_session_attrs",
    "tcp_user_timeout",
    "user",
}


def get_postgres_url():
    postgres_url = os.getenv("POSTGRES_URL")
    if not postgres_url:
        raise ValueError("POSTGRES_URL is not set")

    return clean_postgres_url(postgres_url)


def clean_postgres_url(postgres_url):
    parts = urlsplit(postgres_url.strip().strip("\"'"))
    query = urlencode(
        [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if key in ALLOWED_POSTGRES_PARAMS
        ]
    )
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


def get_connection():
    return psycopg.connect(get_postgres_url())
