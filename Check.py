import requests
import tkinter.messagebox
user = open('user.txt','r').read().splitlines()
def checking():
        for users in user:
            tik = (f'https://m.tiktok.com/node/share/user/@{users}')
            head = {
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'en-US,en;q=0.9',
                'cache-control':'max-age=0',
                'cookie':'tt_webid_v2=6930696974879032837; tt_webid=6930696974879032837; tt_csrf_token=d8lRPZdjfD3sgWCKlFHeaq-0',
                'sec-fetch-dest':'document',
                'sec-fetch-mode':'navigate',
                'sec-fetch-site':'none',
                'sec-fetch-user':'?1',
                'upgrade-insecure-requests':'1',
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344',

            }
            Tik = requests.get(tik,headers=head)
            if ('"statusCode":10202,"statusMsg":""') in Tik.text:
                tkinter.messagebox.showinfo(title='NewUser',message=users)

            elif ('statusCode":10221') in Tik.text:
                print(f'Status : Banned >> {users}')
            elif ('"pageId"') in Tik.text:
                print(f'Taken >> {users}')
checking()

