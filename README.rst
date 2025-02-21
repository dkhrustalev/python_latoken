=========================
Welcome to python_latoken
=========================

This is an unofficial Python wrapper, use at your own risk.

If you find any bugs or want to contribute, feel free to submit your improvements.

If you came here looking for LATOKEN exchange, then go `here <https://latoken.com/invite?r=rbjbrtq7>`_.


Source code
  https://github.com/purveyor97/python_latoken

REST API Documentation
  https://api.latoken.com/doc/v2/

STOMP Websockets Documentation
  https://api.latoken.com/doc/ws/

LATOKEN API Telegram
  https://t.me/latoken_api


This library covers
-------------------

- Authentication of private requests for both REST API and STOMP Websockets
- Asyncio websockets with the option to subscribe to multiple streams simultaneously
- General market data such as historic and current prices, orderbooks, active currencies and pairs
- User account balances access
- Deposit address generation
- Withdrawals
- Transfers within the account
- Transfers between accounts (to other users)
- Crypto Spot Trading

This library doesn't cover
--------------------------

- Futures Trading
- Responce exceptions are exchange generated and are not handled by the library

Quick Start
-----------

Register an account on `LATOKEN <https://latoken.com/invite?r=rbjbrtq7>`_.

Generate an API key `here <https://latoken.com/account/apikeys>`_ with relevant permissions.

There are 4 levels of API key permissions at LATOKEN:

- Read only (you can view market and account data)
- Trade on Spot (in addition: place and cancel orders)
- Trade and Transfer (in addition: transfer within your account)
- Full access (in addition: transfer to other users, deposit and withdraw)

Install python_latoken library:

.. code-block:: bash

  pip install git+https://github.com/purveyor97/python_latoken.git#egg=python_latoken
  

Examples of code usage:
-----------------------

- `REST API <https://github.com/purveyor97/python_latoken/blob/main/examples/rest_example.py>`_
- `Websockets <https://github.com/purveyor97/python_latoken/blob/main/examples/websocket_example.py>`_ (async code)
