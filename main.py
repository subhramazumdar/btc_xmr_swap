from bitcoinutils.transactions import Transaction, TxInput, TxOutput, Sequence, TYPE_RELATIVE_TIMELOCK, TYPE_ABSOLUTE_TIMELOCK
from bitcoinutils.script import Script
from state import State
import state
from identity import Id
import scripts
import consts
import hashlib
import binascii
import txs
from channel import Channel, LIGHTNING_STATE, GENERALIZED_STATE
from helper import hash256, print_tx


### Change this flag to test either the lightning or the generalized channel construction
lightning = False

def main():
    ### (Optional) Replace these addresses with others
    id_a = Id('e12048ff037a0f15bcf977c86181828f5e05dbfe6cf2efe9af6362c8d53a00b0') # addr: mwZ5RAPyv7NxHeeqq2zFo8xngHqWiB4Urb
    id_b = Id('e12048ff047a0f15bcf977c86171828f5e05dbfe6cf2efe9af6362c8d53a00b4') # addr: mgUd1ycGZ7GW66XqdjDFkhGNHmf38b6ATL
    print(id_a.addr)
    print(id_b.addr)
    ### Change these inputs to unspent transaction outputs, given the transaction id and the output index
    tx_in1 = TxInput('0642915819408231b5652b977706aba64d51ffdb9a04839dbcf26ed275fee6f6', 0) # A in ai
    tx_in2 = TxInput('5a8d103f6423e298711d6a36770d4c1a8d63ac0994469f35f537798716bc458b', 0) # I in ai

    ### Change these values to carry the same amount as the outputs specified above
    val_a = 1000
    val_b = 0
    # Transaction fee
    fee = 50

    # create channel between AB
   
    c_ab = Channel.from_inputs(id_a, id_b, tx_in1, tx_in2, val_a, val_b, fee, GENERALIZED_STATE)
    print_tx(c_ab.ft, 'FT_AB')
    for name, tx in c_ab.state.get_state_transactions():
        print_tx(tx, name)

    #c_ab.close(val_a, val_b)
    #print_tx(c_ab.close_tx, 'FT_AB close')

if __name__ == "__main__":
    main()

