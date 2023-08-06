# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from synctera_client.paths.ach_transaction_simulations_receiving_return import Api

from synctera_client.paths import PathValues

path = PathValues.ACH_TRANSACTION_SIMULATIONS_RECEIVING_RETURN