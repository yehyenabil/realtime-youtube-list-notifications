from kafka import KafkaConsumer
import json
import telebot


if __name__ == "__main__":
    bot = telebot.TeleBot("6133186190:AAEAxa0-sVKWpl-Xk2relbUWOb_hHfu0EH4")
    consumer = KafkaConsumer(
        "vid_list",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    for msg in consumer:
        bot.send_message(6197032342, "change in this video details {}".format(json.loads(msg.value)))
