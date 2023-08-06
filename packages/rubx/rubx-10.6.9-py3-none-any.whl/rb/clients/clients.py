#!/bin/python

import pydantic, typing, string, random
from collections import namedtuple


class Account(pydantic.BaseModel):
    app_version: str = 'MA_2.9.8'
    device_hash: str = 'CEF34215E3E610825DC1C4BF9864D47A'
    device_model: str = 'rubx-lib'
    is_multi_account: typing.Optional[bool] = False
    lang_code: str = 'en'
    system_version: str = 'SDK 22'
    token: str = 'cgpzI3mbTPKddhgKQV9lwS:APA91bE3ZrCdFosZAm5qUaG29xJhCjzw37wE4CdzAwZTawnHZM_hwZYbPPmBedllAHlm60v5N2ms-0OIqJuFd5dWRAqac2Ov-gBzyjMx5FEBJ_7nbBv5z6hl4_XiJ3wRMcVtxCVM9TA-'
    token_type: str = 'FireBase'


class Device(dict):

    '''
    this is a default device for account register
    '''

    DEFAULT_DEVICE: dict = {
        'app_version'           :   'MA_2.9.8',
        'device_hash'           :   'CEF34215E3E610825DC1C4BF9864D47A',
        'device_model'          :   'rubx-lib',
        'is_multi_account'      :   False,
        'lang_code'             :   'fa',
        'system_version'        :   'SDK 22',
        'token'                 :   'cgpzI3mbTPKddhgKQV9lwS:APA91bE3ZrCdFosZAm5qUaG29xJhCjzw37wE4CdzAwZTawnHZM_hwZYbPPmBedllAHlm60v5N2ms-0OIqJuFd5dWRAqac2Ov-gBzyjMx5FEBJ_7nbBv5z6hl4_XiJ3wRMcVtxCVM9TA-',
        'token_type'            :   'Firebase'
    }


    @classmethod
    def draw_device(
        cls,
        app_version: str = 'MA_2.9.8',
        device_model: str = 'RubxModule',
        is_multi_account: typing.Optional[bool] = False,
        lang_code: str = 'en',
        system_version: str = 'SDK 22',
        token_type: str = 'FireBase',
        to_dict: bool = False,
        *args,
        **kwargs,
        ) -> Account:

        '''
        example:
            `cls.draw_device(app_version='MA_3.0.0', is_multi_account=True, lang_code='fa')`
        
        device = Device.DEFAULT_DEVICE or Device.draw_device(to_dict=True)
        '''

        result = Account(app_version=app_version or 'MA_2.8.1',
                    device_hash=''.join(random.sample(string.ascii_uppercase+str(string.digits), 32)),
                    device_model=device_model,
                    is_multi_account=is_multi_account,
                    lang_code=lang_code,
                    system_version=system_version,
                    token='{}:{}'.format(''.join(random.sample(string.ascii_lowercase+string.ascii_uppercase+str(string.digits), 22)), ''.join(random.sample((string.ascii_lowercase+string.ascii_uppercase+str(string.digits)+'_-')*3, 140))),
                    token_type=token_type)

        return dict(result) if to_dict else result


class Proxy:

    http: str = 'http',
    https: str = 'https',
    socks5: str = 'socks5',
    socks4: str = 'socks4'

    def proxy_connection(
        __type: typing.Literal['http', 'https', 'socks5', 'socks4'],
        host: str, port: int, to_dict: bool=False,
        *args, **kwargs) -> dict:

        '''
        `print(proxy_connection('http', '127.0.0.1', 8000))`

        #### for insert into RubikaClient: 
            ```
            # example for a param
            proxy = proxy_connection('http', '127.0.0.1', 9050, to_dict=True)
            ```
        '''

        result = namedtuple('Proxy', __type)(**{__type: host+':'+port.__str__()})
        return result._asdict() if to_dict else result


class Infos:

    '''
    info extends
    '''

    citys, proxys, auth_, sent = [], [], [], lambda data: False if data.get('status').lower() != 'ok' else True


class clients(dict):

    '''
    rubika client platforms
    '''

    (web, android,
     rubx, pwa, mrubika) = (
         {
                'app_name'      :   'Main',
                'app_version'   :   '4.2.2',
                'platform'      :   'Web',
                'package'       :   'web.rubika.ir',
                'lang_code'     :   'fa'
                },
            {
                'app_name'      :   'Main',
                'app_version'   :   '2.8.1',
                'platform'      :   'Android',
                'package'       :   'ir.resaneh1.iptv',
                'lang_code'     :   'fa'
                },
            {
                'app_name'      :   'Main',
                'app_version'   :   '3.0.8',
                'platform'      :   'Android',
                'package'       :   'app.rbmain.a',
                'lang_code'     :   'en'
                },
            {
                'app_name'      :   'Main',
                'app_version'   :   '4.2.0',
                'platform'      :   'PWA',
                'package'       :   'web.rubika.ir'
                },
            {
                'app_name'      :   'Main',
                'package'       :   'm.rubika.ir',
                'app_version'   :   '1.2.1',
                'platform'      :   'PWA',
                }
        )


__all__ = ['Device', 'Infos', 'clients', 'Account', 'Proxy']