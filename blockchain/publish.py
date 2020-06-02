import rsa
import sys
import argparse
import requests
import time
from transaction import Transaction
import pickle

#rsa_key_format_choices = ['PEM', 'DER']
TRANSACTION_ENDPOINT = "/transactions"

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Publish a transaction to the blockchain")
    parser.add_argument(
        "--pub",
        required=True,
        help="RSA public key (in PEM format) filename",
        type=argparse.FileType('rb')
    )
    #parser.add_argument(
    #    "--pubformat",
    #    default=rsa_key_format_choices[0],
    #    choices=rsa_key_format_choices,
    #    help="RSA public keyfile encoding"
    #)
    parser.add_argument(
        "--priv",
        required=True,
        help="RSA private key (in PEM format) filename",
        type=argparse.FileType('rb')
    )
    #parser.add_argument(
    #    "--privformat",
    #    default=rsa_key_format_choices[0],
    #    choices=rsa_key_format_choices,
    #    help="RSA private keyfile encoding"
    #)
    parser.add_argument(
        "--database",
        default="127.0.0.1:5000", # default to a Flask server on this machine
        help="The IP and port to publish the transaction to"
    )
    parser.add_argument(
        "--data",
        help="The file to publish as this transaction's body",
        type=argparse.FileType('rb')
    )
    args = parser.parse_args()

    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(args.pub.read())
    args.pub.close()
    privkey = rsa.PrivateKey.load_pkcs1(args.priv.read(), 'PEM')
    args.priv.close()

    #pub_and_priv = rsa.key.newkeys(2048)
    #pubkey = pub_and_priv[0]
    #privkey = pub_and_priv[1]

    #args.data.read()
    transaction = Transaction.create_with_keys(pubkey, privkey, args.data.read(), time.time_ns())
    args.data.close()

    r = requests.post("http://" + args.database + TRANSACTION_ENDPOINT, pickle.dumps(transaction))
    if r.status_code == requests.codes.ok:
        print("Published!")
    else:
        print("Error: " + str(r.status_code))
        print("The database's response is:")
        print(r.text)


    