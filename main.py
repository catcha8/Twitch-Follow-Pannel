import os, requests,random,threading

def get_id(channel_name):

    json = {"operationName": "ChannelShell",
            "variables": {
                "login": channel_name
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe"
                }
            }
        }

    headers = {
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }
    r = requests.post('https://gql.twitch.tv/gql', json=json, headers=headers)
    return r.json()['data']['userOrError']['id']
sem = threading.Semaphore(200)


class Twitch():

    def sub(type,channel_ID):
        with sem:

            filefile = open('tokens.txt')
            token = random.choice(open("tokens.txt", "r" ).read().splitlines())
            filefile.close()

            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-GB',
                'Authorization': f'OAuth {token}',
                'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                'Connection': 'keep-alive',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Origin': 'https://www.twitch.tv',
                'Referer': 'https://www.twitch.tv/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                }

            if type == "Followed":
                data = '[{"operationName":"FollowButton_FollowUser","variables":{"input":{"disableNotifications":false,"targetID":"'+channel_ID+'"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"}}}]'
            else:
                data = '[{"operationName":"FollowButton_UnfollowUser","variables":{"input":{"targetID":"'+channel_ID+'"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880"}}}]'

            r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
            if r.status_code == 200:
                print(f"[+] {type} {channel_name}")
            else:
                print("Error")


Happy = True # if u star me

if Happy :
    channel_name = input("Enter channel name --> ")
    print("[1] Follow\n[2] Unfollow")

    choice = int(input(("Enter option --> ")))
    threads = input("Amount --> ")
    id = get_id(channel_name=channel_name)
    if choice == 1:
        type = "Followed"
    else:
        type = "UnFollowed"
    for i in range(int(threads)):
        threading.Thread(target=Twitch.sub,args=(type,id,)).start()
