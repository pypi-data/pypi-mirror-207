#!/usr/bin/env python3

# Partially written with ChatGPT

import os
import time
import json
import sqlite3
import argparse
import requests


def load_config(config_file):
    with open(config_file) as f:
        return json.load(f)


def load_database(config):
    con = sqlite3.connect(config["database"])

    con.execute(
        "CREATE TABLE IF NOT EXISTS subscriptions(phone VARCHAR, icao VARCHAR, description VARCHAR, last_seen INTEGER)"
    )
    con.commit()

    return con


def update_last_seen_time(con, sub_id):
    con.execute(
        "UPDATE subscriptions SET last_seen = ? WHERE rowid = ?",
        (time.time(), sub_id),
    )


def send_text_message(phone, message, key):
    request = {"phone": phone, "message": message, "key": key}
    resp = requests.post("https://textbelt.com/text", request)
    print(resp.json())


def process_subscriptions(con, config, data):
    cur = con.execute(
        "SELECT rowid, phone, icao, description, last_seen FROM subscriptions"
    )

    for sub_id, phone, icao, description, last_seen in cur.fetchall():
        if icao in data and data[icao]["seen"] < config["max_age"]:
            if last_seen + config["min_disappearance"] < time.time():
                message = f"{description}\n{config['tracker']}?icao={icao}"

                send_text_message(phone, message, config["textbelt_key"])

                print(f"{phone}: {message}")

            update_last_seen_time(con, sub_id)

    con.commit()


def get_current_data(config):
    response = requests.get(config["data"])
    planes = response.json()["aircraft"]
    return {plane["hex"]: plane for plane in planes}


def run(config):
    con = load_database(config)

    while True:
        data = get_current_data(config)

        process_subscriptions(con, config, data)

        time.sleep(config["delay"])

    con.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file")
    args = parser.parse_args()

    config = load_config(args.config_file)

    try:
        if config["pid_file"]:
            with open(config["pid_file"], "w+") as f:
                f.write(str(os.getpid()))

        run(config)
    finally:
        if config["pid_file"]:
            os.unlink(config["pid_file"])
