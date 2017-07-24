# comitup-demo

## Description

This is a quick-and-dirty demonstration package for the
[Comitup](https://davesteele.github.io/comitup/) service. When the
comitup-demo service is started (automatically, at boot), it will clear out
any NetworkManager connections, and restart NetworkManager and Comitup.
It will then announce, using a synthesized voice via an attached speaker,
whenever the following events occur:

* A new user connected to the comitup Access point ("AP")
* A new user accessed a comitup-web page ("web")
* The Internet-facing wifi node is connected ("Successful connection")

Once connected, a web service is started that will allow the person who
initiated the successful connection to enter their name, which is then
announced.

## Requirements

The demo requires the following:

* A Raspberry Pi 3, or Zero-W, with an additional USB wifi adapter
  (the second adapter is a requirement of the demo, not Comitup, and
  the use of a wireless-enabled Pi avoids AP-mode compatibility problems)

* The following packages must be installed:
    - comitup
    - festival
    
* A speaker connected to the Pi audio port

## Installation

Run *install.sh*, and set the *web_service* parameter in
*/etc/comitup.conf* to *demoweb.service*.
