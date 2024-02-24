import os

from qiskit_ibm_provider import IBMProvider
from qiskit_ibm_runtime import QiskitRuntimeService

IBMProvider.save_account(os.environ["IBMQ_TOKEN"], overwrite=True)
QiskitRuntimeService.save_account(channel='ibm_quantum', token='my_token', overwrite=True)