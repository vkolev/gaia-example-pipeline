from gaiasdk import sdk
import logging
import time


def create(args):
    logging.info("Create with args:")
    logging.info(args)
    time.sleep(10)


def update(args):
    logging.info("Update with args:")
    logging.info(args)
    time.sleep(5)


def main():
    logging.basicConfig(level=logging.INFO)
    createUser = sdk.Job("Create user", "Create a user with args", create)
    updateUser = sdk.Job("Update user", "Updates the user with args", update, ["Create user"])
    sdk.serve([createUser, updateUser])