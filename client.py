from __future__ import annotations

from jira import JIRA

import logging
import sys

bearer      = "ATATT3xFfGF0FbzwLsx9FTcU4KyLjblszYU2B2sgMI4xBdSF8H2YnSqTaODJxarzCgEgOTTSFSAUoWsMTTFW7R8uBATpEPVpsRBvHyMn8NNmaFuLgJ4HZzM4rrAmVhobkr5CJaQCnzMuyzXi7Kr2cEt9dA-SBd0tiUD5QkZBFRpUMBhhwvkwL4A=D78F3348"
email       = "bruno.gl.aquino+soamerprojeto@gmail.com"
password    = "1.change123"
log         = logging.getLogger(__name__)

def connect_jira(log, jira_server, jira_user, jira_password) -> JIRA:
    """
    Connect to JIRA. Return None on error
    """
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        jira_options = {"server": jira_server}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
        return jira
    except Exception as e:
        log.error("Failed to connect to JIRA: %s" % e)
        sys.exit()

def get_client() -> JIRA:
    """
    Get Client
    """
    return connect_jira(log, "https://soamerprojeto.atlassian.net", email, bearer)