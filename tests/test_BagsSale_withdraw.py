import pytest
import logging
from brownie import Wei, reverts
LOGGER = logging.getLogger(__name__)

def test_BagsSale_withdraw_0eth(accounts, sale, bagsERC20):
    sale.withdraw({'from':accounts[0]})


