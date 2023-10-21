from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10


internetSpeedBot = InternetSpeedTwitterBot()
internetSpeedBot.get_internet_speed()
internetSpeedBot.tweet_at_provider()