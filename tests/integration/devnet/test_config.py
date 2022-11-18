#    Copyright 2022 Frank V. Castellucci
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# -*- coding: utf-8 -*-

"""Configuration testing."""

from pysui.sui import SuiConfig, SuiAddress


def test_multi_address_pass(configuration):
    """test_multi_address Validates multiple addresses.

    :param configuration: A devnet configuration
    :type configuration: SuiConfig
    """
    assert isinstance(configuration, SuiConfig)
    assert configuration.rpc_url == "https://fullnode.devnet.sui.io:443"
    assert configuration.faucet_url == "http://faucet.devnet.sui.io/gas"
    assert len(configuration.addresses) >= 2


def test_address_keypair_parity_pass(configuration):
    """test_address_keypair_parity_pass Validates address and keypair parity.

    :param configuration: A devnet configuration
    :type configuration: SuiConfig
    """
    assert len(configuration.addresses) == len(configuration.keystrings)


def test_address_keypairs_match_pass(configuration):
    """test_address_keypairs_match_pass Verify addresses are one of keystrings.

    :param configuration: A devnet configuration
    :type configuration: SuiConfig
    """
    active_address = configuration.active_address
    addresses = set(configuration.addresses)
    assert active_address.identifier in addresses
    for keystring in configuration.keystrings:
        address = SuiAddress.from_keypair_string(keystring)
        assert address.identifier in addresses
