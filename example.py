import rpc
import time

print("Demo for python-discord-rpc")
client_id = '579211794166579210' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Mängib lolli",
            "details": "Mängib hullu",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "snorkel",
                "small_image": "snorkel",
                "large_text": "snorkel",
                "large_image": "snorkel"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)
