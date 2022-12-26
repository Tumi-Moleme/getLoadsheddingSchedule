# getLoadsheddingSchedule

![broken light bulb](./LOAD-SHEDDING-ALERT-1.jpg)

## Installation

>I assume that you are using linux

1. First, you will need to sign up for a Twilio account and obtain a Twilio phone number with WhatsApp capabilities.
2. Next, install the Twilio Python library using pip:

```
pip install twilio
```

3. Make the script executable using the following command: 

```
chmod +x crontab.sh
```

4. Use the cron utility to schedule the script to run every hour. Open the crontab file using the following command:

```
crontab -e
```
5. Add the  line below to the crontab file to run the script every hour:

```
0 * * * * /path/to/run_script.sh
```

6. First, sign up for a Twitter developer account and create a new app. This will give you access to the Twitter API and the necessary API keys and secrets.

7. Install the tweepy library using pip:

```
pip install tweepy
```