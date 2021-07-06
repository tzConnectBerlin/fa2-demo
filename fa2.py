#!/usr/bin/env python3

##################################################################################################
# Trivial example of mint and burn of a contract on the florencenet Tezos testnet.
contract_id='KT1XtDdQcB6WCtnUsv8Da7fRNVN7teMunsvS' # address of FA2 contract
owner='tz1RjonN5qEJM8cZhKcfGyoEqhw1FNB4ti6w' # address of owner
privkey='edsk4LzAuuQF1FkFHV5qXmpL8a5YNtJh1pTtkAYjAVBKCSAbp6LCCD' # private key of owner
#
# install pytezos first!
from pytezos import pytezos

def admin_account():
    ''' Return an initialised pytezos object using the admin key defined in this file '''
    return pytezos.using(
        key = privkey,
        shell = 'http://florence.newby.org:8732') # My private node, can replace with a public one

def contract():
    ''' Return an initialised contract object for the FA2 contract with id above'''
    client = admin_account()
    return client.contract(contract_id)

def initialize():
    contract_ = contract()
    account = admin_account()
    operations = []
    results = []
    for i in range(1,50):
        name = f"token-{i}"
        count = 1
        symbol = f"TKN{i}"
        token_id = i
        operations.append(contract_.create_token(token_id,
                                                {"name": name.encode('utf-8'),
                                                 "symbol": symbol.encode('utf-8'),
                                                 "isTransferable": "true".encode('utf-8'),
                                                }
        ))
        operations.append(contract_.mint_tokens([
            { "owner": owner,
              "token_id": token_id,
              "amount": count } ] ))
        results.append({
            "name": name,
            "token_id": token_id,
            "symbol": symbol,
            "minted": count,
            "owner": owner,
            })

    res = account.bulk(*operations).autofill(gas_limit=100000, fee=280000).sign().inject(_async = False)
    return res

# Needed to unpause, like this:
# >>> c.pause(False).inject()


def transfer(token_id, dest):
    c = contract()
    c.transfer(
        [ { "from_": admin_account().key.public_key_hash(),
            "txs": [
                { "to_": dest,
                  "token_id": token_id,
                  "amount": 1 }]}]).inject()
