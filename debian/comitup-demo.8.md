% comitup-demo(8)
%
% May 2021

# NAME

comitup-demo -- Manage wifi connections on headless, unconnected systems

## SYNOPSIS

`systemctl [start|stop] comitup-demo`

## DESCRIPTION

The **comitup-demo** service turns a device into a demostration system for the
Comitup WiFi management service. On startup, it will wipe all NetworkManager
WiFi configurations, and restart NetworkManager. It will announce, using voice
systhesis over audio, when someone connects to the Comitup hotspot, accesses
the Comitup WiFi configuration website, or creates a successful upstream
connection. After that, it launches a web interface that allows (only) the
person who made the connection to enter their name for announcement.

When installed, the **comitup-demo** package will override any *web_service*
defined in _comitup.conf_.

## COPYRIGHT

Comitup-demo is Copyright (C) 2021 David Steele &lt;steele@debian.org&gt;.

## SEE ALSO

comitup(8), comitup-conf(5), demoweb(8)
