"""
tropycal - Package for retrieving and analyzing tropical cyclone data
"""

try:
    from ._version import version as __version__  # noqa: F401
    from ._version import version  # noqa: F401
except ImportError:
    __version__ = "unknown"
    version = __version__
