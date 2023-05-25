"""
params: 1:1685002007
result: YyiUFIEk3tgySPR1ZZmMEg==
params: 2:1685002008
result: z7tIXWv9sdxJgGaeDpC4pQ==
params: 3:1685002016
result: 3RuAWiF9FvJUwueCaY4ezQ==
params: 4:1685002426
result: HpYR+jHDEXOuE9QSjRQy5g==
"""

import frida
import requests

rpc_sign = """
rpc.exports = {
    getsign: function(plaintext){
      var sig = "";
      Java.perform(
        function(){
            //拿到context上下文
            var currentApplication = Java.use('android.app.ActivityThread').currentApplication();
            var context = currentApplication.getApplicationContext();
            var ChallengeTwoFragment = Java.use('com.yuanrenxue.match2022.fragment.challenge.ChallengeTwoFragment');
            var fragment = ChallengeTwoFragment.$new();
            try {
                sig = fragment.sign(plaintext);
            } catch (e) {
                console.log('err:', e);
            }
        }
      )
       return sig;
    }
};

"""

device = frida.get_usb_device()
_process = device.get_process('猿人学2022')
process = device.attach(_process.pid)
script = process.create_script(rpc_sign)
script.load()


def get_sign(text):
    return script.exports_sync.getsign(text)


def get_timestamp():
    url = 'https://appmatch.yuanrenxue.cn/time?token=WHiC5i1XgfSxhIIp45oW%252FwHbUg1Rd716WAlNoiS%252FvSJgDT%252BAj7vI3dGcP76qP4Xw'
    response = requests.get(url)
    return response.json()['time']


def request():
    total = 0
    for page in range(1, 101):
        print('page:', page)
        timestamp = get_timestamp()
        plaintext = f'{page}:{timestamp}'
        data = {
            'ts': timestamp,
            'page': page,
            'sign': get_sign(plaintext)
        }
        url = "https://appmatch.yuanrenxue.cn/app2?token=WHiC5i1XgfSxhIIp45oW%252FwHbUg1Rd716WAlNoiS%252FvSJgDT%252BAj7vI3dGcP76qP4Xw"
        response = requests.post(url, data=data)
        json_data = response.json()
        for row in json_data['data']:
            total += int(row['value'].strip())
    print(total)



request()
