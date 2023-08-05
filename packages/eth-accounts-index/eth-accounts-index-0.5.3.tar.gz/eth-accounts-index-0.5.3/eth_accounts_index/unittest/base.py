# standard imports
import logging

# external imports
from chainlib.eth.unittest.ethtester import EthTesterCase
from chainlib.connection import RPCConnection
from chainlib.eth.nonce import RPCNonceOracle
from chainlib.eth.address import to_checksum_address
from chainlib.eth.tx import receipt

# local imports
from eth_accounts_index.registry import AccountRegistry

logg = logging.getLogger(__name__)


class TestAccountsIndex(EthTesterCase):

    def setUp(self):
        super(TestAccountsIndex, self).setUp()
        self.conn = RPCConnection.connect(self.chain_spec, 'default')
        nonce_oracle = RPCNonceOracle(self.accounts[0], conn=self.conn)

        c = AccountRegistry(self.chain_spec, signer=self.signer, nonce_oracle=nonce_oracle)
        (tx_hash, o) = c.constructor(self.accounts[0])
        r = self.conn.do(o)
        logg.debug(f'published with hash {r}')

        o = receipt(r)
        r = self.conn.do(o)
        self.address = to_checksum_address(r['contract_address'])

        (tx_hash, o) = c.add_writer(self.address, self.accounts[0], self.accounts[0])
        r = self.conn.do(o)

        o = receipt(r)
        r = self.conn.do(o)
        self.assertEqual(r['status'], 1)
