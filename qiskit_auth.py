import os

from qiskit_ibm_provider import IBMProvider

IBMProvider.save_account(os.environ["IBMQ_TOKEN"], overwrite=True)
