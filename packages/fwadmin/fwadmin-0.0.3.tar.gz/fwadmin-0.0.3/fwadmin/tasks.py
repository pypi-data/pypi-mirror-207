"""Tasks executed via Netbox scripts or manually."""
__author__ = "Andrea Dainese"
__contact__ = "andrea@adainese.it"
__copyright__ = "Copyright 2022, Andrea Dainese"
__license__ = "GPLv3"

from datetime import timedelta
import requests

from django.conf import settings
from django.utils import timezone

from fwadmin import models

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get("fwadmin", {})


def terminate_sessions(firewalls=None, script_handler=None):
    """Terminate expired sessions acting on firewalls.

    Expired means end_time + Firewall_Update_interval < now.
    """
    if not firewalls:
        firewalls = []
    # Shift now and consider firewall update interval
    now = timezone.now() - timedelta(seconds=PLUGIN_SETTINGS.get("EDL_UPDATE_INTERVAL"))

    # Clear rejected sessions
    models.SessionRequest.objects.filter(
        status__contains="rejected", cleared=False
    ).exclude(requests__end_at__gt=now).update(cleared=True)

    # Get uncleared sessions
    uncleared_sessionrequest_qs = models.SessionRequest.objects.filter(
        status__contains="approved", cleaned=False, end_at__lt=now
    )

    for uncleared_sessionrequest_o in uncleared_sessionrequest_qs:
        # Get associated DynamicList objects which have no active sessions (from other requests)
        dynamiclist_to_be_cleared_qs = uncleared_sessionrequest_o.dynamic_lists.exclude(
            requests__end_at__gt=now,
        )
        for dynamiclist_to_be_cleared_o in dynamiclist_to_be_cleared_qs:
            for firewall_o in dynamiclist_to_be_cleared_o.firewalls.all():
                if script_handler:
                    script_handler.log_info(
                        "Clearing session using rule "
                        + dynamiclist_to_be_cleared_o.rule
                        + f" in firewall {firewall_o.name} ({firewall_o.model})"
                    )

                if firewall_o.model == "paloalto-panos":
                    # url = f"https://{firewall_o.address}/api/?type=op&cmd=<clear><session><all><filter><rule>{dynamiclist_to_be_cleared_o.rule}</rule><{dynamiclist_to_be_cleared_o.direction}>{connection.ip}</{dynamiclist_to_be_cleared_o.direction}></filter></all></session></clear>&key={firewall_o.secret_key}"
                    # TODO: Check if connection.ip is needed, in this implementation the entire RULE is checked.
                    url = (
                        f"https://{firewall_o.address}/api/?type=op&cmd=<clear><session>"
                        + "<all><filter><rule>{dynamiclist_to_be_cleared_o.rule}</rule>"
                        + "<{dynamiclist_to_be_cleared_o.direction}></{dynamiclist_to_be_cleared_o.direction}>"
                        + "</filter></all>"
                        + "</session></clear>&key={firewall_o.secret_key}"
                    )
                    req = requests.get(url, verify=firewall_o.verify_certs, timeout=15)
                    if req.status_code != 200:
                        if script_handler:
                            script_handler.log_error(
                                "Failed to clear session "
                                + dynamiclist_to_be_cleared_o.id
                            )
                            return req.text

        # Session cleared
        uncleared_sessionrequest_o.created = True
        uncleared_sessionrequest_o.save()

    return ""
