#!/bin/python
# main object - `rb` is main package to importing

import os, sys

if __name__.__eq__('__main__').__and__(__package__.__eq__(None) or __package__.__eq__('')):
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    import tinytag, Crypto, pydantic, requests, websocket
except ModuleNotFoundError:
    from .extensions import PyPi
    PyPi().installation(['tinytag', 'pycryptodome', 'pydantic',
                         'requests', 'websocket-client'])

import copy, logging, platform, typing, difflib, inspect

from datetime           import  datetime
from json               import  dumps, loads
from random             import  choice, randint, sample
from re                 import  findall, search, sub, compile
from time               import  sleep, gmtime, localtime
from warnings           import  warn
from requests           import  get, post, session
from abc                import  ABC
from .exceptions        import  *
from .extensions        import  *
from .events            import  *
from .crypto            import  Encryption
from .connection        import  GetData, Urls, Connection, Make
from .storage           import  SQLiteSession
from .clients           import  *
from .UserMethods       import  UserMethods
from .GroupMethods      import  GroupMethods
from .ChannelMethods    import  ChannelMethods
from .rubino            import  RubinoClient
from .BotMethods        import  BotMethods
from .methods           import  Method
from .models            import  Attrs
from .websocket         import WebSocket
from .parser            import  (
    MessageEmpty, MessageEntityBold, MessageEntityCode,
    MessageEntityItalic, MessageEntityHashtag, MessageEntityMention,
    MessageEntityMentionName, MessageEntityPre, MessageEntityStrike,
    MessageEntityTextUrl, MessageEntityUnderline, MessageEntityUnknown,
    MessageEntityUrl, Metas, Tags, MetaDataLoader, MarkDown
    )

if typing.TYPE_CHECKING:
    from . import RubikaClient, UserMethods

try:
    from . import __file__ as base_file
    from . import __name__ as base_log
    from . import __package__ as base_pkg

except ImportError:
    base_file, base_log, base_pkg = locals().get('__file__') or __doc__, locals().get('__name__'), locals().get('__package__')


class Version(str):
    __version__ =   '10.6.9'
    __author__  =   'saleh'
    __lisense__ =   'MIT'
    __module__  =   'rb'
    __library__ =   'rubx' # dynamic underscore


class RubikaClient(ABC):

    __slots__ = ('self', 'session', 'chat_id',
                 'username', 'app', 'phone_number',
                 'device', 'proxy', 'your_name',
                 'city', 'banner', 'creator_channel_open',
                 'platform', 'api_version', 'headers',
                 'timeout', 'check_update', 'lang_code',
                 'base_logger', 'check_session', 'api_client',
                 'return_data_action')

    __base_class__, __version__, logs, slots = 'RubikaClient', Version.__version__, {}, copy.deepcopy(__slots__)

    def __str__(self, *args) -> (str):
        return dumps({'session': SQLiteSession(self.auth).information()}, indent=2) if self.auth else dumps({'__base_class__': __base_class__}, indent=2)

    def __init__(
        self                :   ('Client'),
        session             :   (str)                               =   (None),
        chat_id             :   (str)                               =   (None),
        username            :   (str)                               =   (None),
        app                 :   (str)                               =   ('rubx'),
        phone_number        :   (str)                               =   (None),
        device              :   (dict)                              =   (Device.DEFAULT_DEVICE),
        proxy               :   (dict)                              =   {'http': 'http://127.0.0.1:9050'},
        your_name           :   (str)                               =   (False),
        city                :   (str)                               =   ('mashhad'),
        banner              :   (bool)                              =   (False),
        creator_channel_open:   (bool)                              =   (False),
        platform            :   (str)                               =   (None),
        api_version         :   (typing.Union[str, int])            =   (None),
        headers             :   (typing.Union[dict, str, list])     =   (None),
        timeout             :   ((typing.Union[int, str]))          =   (5),
        check_update        :   (typing.Optional[bool])             =   (False),
        lang_code           :   (str)                               =   ('fa'),
        base_logger         :   (typing.Union[str, logging.Logger]) =   (None),
        check_session       :   (bool)                              =   (False),
        api_client          :   (str)                               =   (None),
        return_data_action  :   typing.Optional[str]                =   ('dict'),
        *args,
        **kwargs
        ) -> (None):

        '''
        ## IMPORT:
            - from rb import RubikaClient

        ## USE:
        
            `client = RubikaClient('session-key', 'u0...', 'username', 'rubx', your_name='saleh', banner=True, creator_channel_open=True, platform='rubx', api_version='5', timeout=5, proxy={'socks5':'http://127.0.0.1:9050'}, headers={'user-agent':...}, api_client='https://messengerg56c.iranlms.ir:80', ...)`

        ## EXAMPLES:
            
            `with RubikaClient(...) as client:`
                `client.send_message(...)`
            
            # ... or ...
            
            `client = RubikaClient('abcdefghijklmnopqrstuvwxyzzabcde')`
            `client.session = '' # len: 32 chars`
            
            `import socks`
            `client.proxy   = {socks.SOCKS5:'127.0.0.1:9050'}`
            
            `def run(callable, params) -> dict:`
                `return callable(**params)`

        
            print(
                run(
                    client.send_message,
                    dict(
                        chat_id='chat-guid',
                        text='Hey! this message from rubx lib.'
                        )
                    )
                )
            
            
            with RubikaClient('session') as client:
                print(client * '@username') # to getting ifo from a chat


        ## PARAMETERS:
        
            - 1- `self`: is a self obejct
            - 2- `session`: is account key [auth]
            - 3- `chat_id`: is your guid account
            - 4 - `username`: is your username account
            - 5 - `app`: is from app name
            - 6 - `phone_number`: is for using lib with phone_number and geting account key
            - 7 - `device`: is your account device for use token or thumbinline or ...
            - 8 - `proxy`: set proxy http to requests
            - 9 - `your_name`: is for save info in a file.
            - 10 - `city`: is for your countery and city for using client server.
            - 11 - `banner`: is a boolean for print banner
            - 12 - `creator_channel_open`: is for joining your account in creator channel
            - 13 - `platform`: is for using user platform. examples: `rubx` or `web` or `android`
            - 14 - `api_version`: is for using api mode: `5` (for web and rubx) `4` (for rubika app [andorid]) `3` (for m.rubka.ir)
            - 15 - `headers`: is for set header to requests
            - 16 - `timeout`: is for requests timeout
            - 17 - `check_update`: is for checking lib new version
            - 18 - `lang_code`: to app lang code. `en`, `fa`, ...
            - 19 - `base_logger`: is for `__name__`
            - 20 - `check_session`: return a dict type to checking session [AUTH]
            - 21 - `api_client`: to set a server for requests
            - 22 - `return_data_an_dict`: return the json data to str(ordered with dumps) or dict(normal)
        
        
        ## `what is [guid]?` : guide unique identifier | chat id : group guid, channel guid and others ...
        ## `what is [session] or [auth]?`: is your session id (api key) for account.
        ## what is [object]?: the 'object' is 'chat'


        ## ERRORS | EXCEPTIONS:
        
            - `NotREGISTERED`: your session false
            - `InvalidInput` : the request is blocked due to lack of access or wrong parameters.
            - `TooREQUESTS`  : this request is not possible due to the high number of requests. U should try again after a few moments!
            - `InvalidAUTH`‍  : the key or chat id or input entered is invalid, please check the information and then try again.
            - `ConnectError` : the server is down due to many requests and does not respond. You can use 'timeout' .
            - `ClientError`  : the client server is incorrect.
            - `ServerError`  : the server is unable to respond for any reason.
            - `SessionError` : your session is invalid.
            
            #### bypass them using (`try` & `except`) exception and solve them.

        to show public methods:
        ----------------------
            dir(RubikaClient)

        to show method comment [doc]:
        ----------------------------
            help(RubikaClient) or a attrbute

        for getting file thumbnail:
        --------------------------
            `get file bytes and encode to base64` `:` `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`

        ### star the repo: https://github.com/mester-root/rubx
        
        '''

        if kwargs and session is None:
            for key in kwargs.keys():
                if (attr := difflib.get_close_matches(key, RubikaClient.slots)):
                    if attr[0].__eq__('session'):
                        session = kwargs.get(key)

        (self.app, self.proxy, self.enc,
            self.city, self.platform, self.api_version,
            self.headers, self.username, self.chat_id,
            self.handling, self.phone, _log,
            self.timeout, self.lang_code, self.device,
            self.check_session, self.api_client,
            self.last_response, self.banner, self.your_name,
            self.phone_number, self.creator_channel_open, self.check_update,
            self.check_session, self.session) = (app, proxy, Encryption(session),
                                                    city, platform, api_version,
                                                    headers, username, chat_id,
                                                    {}, phone_number, logging.getLogger(__name__),
                                                    timeout, lang_code, device,
                                                    check_session, api_client,
                                                    set(), banner, your_name,
                                                    phone_number, creator_channel_open, check_update,
                                                    check_session, session)

        if kwargs: # to check kwargs name
            for key in kwargs.keys(): # list(kwargs)
                # for name in RubikaClient.slots:
                if (attr := difflib.get_close_matches(key, RubikaClient.slots)): # difflib.SequenceMatcher(None, key.lower(), name).ratio():
                    # kwargs.update({name: kwargs.get(key)}) TODO self(**kwargs)
                    setattr(self, attr[0], kwargs.get(key))

        Infos.citys.append(city)
        Infos.proxys.append(proxy)
        GetData.url: str = (api_client) # TODO: set other params 
        # TODO: set all params in __init__ object

        if banner:
            assert list(map(lambda character: (print(character, flush=True, end=''), sleep(0.01)), f'\n\033[0m< \033[31mrubx \033[0m> \033[36m | \033[31mstarted in \033[0m{str(datetime.datetime.now())}\033[31m| \033[0m{Version.__version__}\n'))
        
        if your_name:
            open('session_info.sty', 'w+').write('name: '+your_name+'\ntime started: '+str(datetime.datetime.now())+f'\key: {session}'+'\nyour ip: '+str(get('https://api.ipify.org').text))

        if session:
            if session.__len__() != 32:
                raise SessionError('Your `session` is invalid - the number of characters in your session is different from 32')

            self.auth: (str) = (session)
            Infos.auth_.append(session)

        elif phone_number:
            Login.SignIn(phone_number, self)

        else:
            try:
                session = open(f'{app}.sty', 'r+').read()
                self.auth = session
                Infos.auth_.append(session)

            except Exception:
                warn('SessionWarning: please insert session key or phone_number in object')

        if creator_channel_open:
            # self.join_channel_action('')
            # __import__('webbrowser').open('https://rubika.ir/TheClient')
            pass

        if app:

            try:
                open(f'{app}.sty', 'r')
            except FileNotFoundError:
                open(f'{app}.sty', 'w').write(session)
                database = SQLiteSession(session)
                database.insert(self.phone, session, self.chat_id, self.api_client or Urls.get_url())

        if check_update:
            UpToDate(Version.__version__, 'https://raw.githubusercontent.com/Mester-Root/rubx/main/rb/version.sty').user

        if check_session:
            self.check_session: dict = _Top(session).detecting()
        
        if isinstance(base_logger, str):
            base_logger: str = logging.getLogger(base_logger)

        elif not isinstance(base_logger, logging.Logger):

            try:
                base_logger: str = base_log
            except Exception: ...

        class Loggers(dict):
            def __missing__(self, key) -> None:
                if key.startswith('rb.'):
                    key = key.split('.', maxsplit=1)[1]

                return base_logger.getChild(key)

        self._log = Loggers()
        # self.__name__ = base_logger
        
        Connection.timeout: int = timeout or 5
        clients.web.update({'lang_code': self.lang_code or 'en'}) # TODO: to set lang_code in rubx and android clients
        
        if isinstance(return_data_action, (str, tuple, list)):

            if isinstance(return_data_action, (list, tuple)):
                Make.action, Make.type = return_data_action

            elif isinstance(return_data_action, str) and any(return_data_action.__contains__(action) for action in ('dict', 'str', 'object', 'model')):
                Make.action: str = return_data_action

        if headers:
            Connection.headers = headers
        if api_version:
            Connection.api_version = api_version
        if self.platform:
            Connection.platform = platform
        if city:
            Connection.city = city
        if proxy:
            Connection.proxy = proxy
        Make.app = self

    def __dir__(self):
        return dir(RubikaClient)

    def __reduce__(self):
        return object.__reduce_ex__

    def __reduce_ex__(self):
        return object.__reduce_ex__

    def __init_subclass__(cls, *args, **kwargs):
        cls.logs.update({'log': (args, kwargs)})

    def __subclasshook__(cls, other: object):
        return any(class_.__dict__.__contains__('__len__').__and__(class_.__dict__.__contains__('__iter__')) for class_ in other.__mro__) if cls is RubikaClient else None

    def __hash__(self):
        return hash(RubikaClient)

    def __call__(self) -> (None):
        pass

    def __enter__(self):
        return (self)

    def __exit__(self, *args,
                 **kwargs) -> (None):
        pass

    @classmethod
    def start(cls, func: object,
              kwargs: dict = None, args: tuple = ()) -> None: # TODO: set runner with start func
        from threading import Thread
        Thread(target=func, args=args, kwargs=kwargs).start()


    @property
    def get_session(self) -> (str):
        '''
        getting session key - auth
        '''

        return self.auth


    @property
    def get_storage(self) -> (str):

        '''
        get local storage - SqliteSession - info's
        '''

        return dumps({'session': SQLiteSession(self.auth).information()}, indent=2)


    def get_me(self) -> str:
        '''
        get my sessions
        '''

        return self.get_storage


    @classmethod
    def run(cls, func: object,
            *args, **kwargs) -> None:
        
        '''
        running sync methods
        '''
        
        __import__('_thread').start_new_thread(func, *args, **kwargs)


    @classmethod
    def pool(cls, func: object,
             args: tuple = (), kwargs: dict = {}) -> typing.Any:

        from multiprocessing.pool import ThreadPool
        pool = ThreadPool(processes=1)

        try:
            return pool.apply_async(func, args, kwargs).get()
        except Exception:
            return pool.apply_async(func).get()


Client = RubikaClient

class SetClient(RubikaClient, UserMethods,
                GroupMethods, ChannelMethods):
    pass


class EventBuilder(Client):
    
    def __str__(self) -> (str):
        return self.jsonify(indent=2)

    def __getattr__(self, name) -> (list):
        return self.find_keys(keys=name)

    def __setitem__(self, key, value) -> (None):
        self.original_update[key] = value

    def __getitem__(self, key):
        return self.original_update[key]

    def __lts__(self, update: list) -> (list):
        for index, element in enumerate(update):
            if isinstance(element, list):
                update[index] = self.__lts__(update=element)

            elif isinstance(element, dict):
                update[index] = EventBuilder(update=element)

            else:
                update[index] = element
        return update

    def __init__(self, update: dict = None) -> (None):

        '''
        # get all keys from a dictionary
        '''

        self.original_update = update

    def to_dict(self) -> (dict):
        return self.original_update

    def jsonify(self, indent=None) -> (str):
        
        result = self.original_update
        result['original_update'] = 'dict{...}'
        
        return dumps(
            result,
            indent=indent,
            ensure_ascii=False,
            default=lambda value: str(value)
            )

    def find_keys(self, keys: list,
                  original_update: str = None) -> (list):

        if not original_update:
            original_update = self.original_update

        if not isinstance(keys, list):
            keys = [keys]

        if isinstance(original_update, dict):
            for key in keys:
                try:
                    update = original_update[key]
                    if isinstance(update, dict):
                        update = EventBuilder(update=update)

                    elif isinstance(update, list):
                        update = self.__lts__(update=update)

                    return update

                except KeyError:
                    pass
            original_update = original_update.values()

        for value in original_update:
            if isinstance(value, (dict, list)):
                try:
                    return self.find_keys(keys=keys, original_update=value)

                except AttributeError:
                    pass

        raise AttributeError(f'Struct object has no attribute {keys}')

    @property
    def action(self):
        return self.find_keys(keys=['author_type'])


    @property
    def type(self):
        try:
            return self.find_keys(keys=['type', 'author_type'])

        except AttributeError:
            pass

    @property
    def raw_text(self):
        try:
            return self.find_keys(keys='text')

        except AttributeError:
            pass

    @property
    def message_id(self):
        try:
            return self.find_keys(keys=['message_id',
                                        'pinned_message_id'])
        except AttributeError:
            pass

    @property
    def reply_message_id(self):
        try:
            return self.find_keys(keys='reply_to_message_id')

        except AttributeError:
            pass

    @property
    def find_rubika_channel_post(self):
        return findall(r'(rubika\.ir\/\w{4,25}\/\w{15})', self.raw_text)

    @property
    def find_rubika_private_link(self):
        return findall(r'(rubika\.ir\/join[c,g]\/\w{32})', self.raw_text)

    @property
    def find_chanel_private_link(self):
        return findall(r'(rubika\.ir\/joinc\/\w{32})', self.raw_text)

    @property
    def find_group_link(self):
        return findall(r'(rubika\.ir\/joing\/\w{32})', self.raw_text)

    @property
    def find_rubika_link(self):
        return findall(r'(rubika\.ir\/\w{4,25})', self.raw_text)

    @property
    def find_atsign(self):
        return findall(r'\@\w{4,25}', self.raw_text)

    @property
    def find_url(self):
        return findall(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}|[a-zA-Z0-9]+\.[^\s]{2,})', self.raw_text)

    @property
    def is_rubika_channel_post(self):
        return (search(r'(rubika\.ir\/\w{4,25}\/\w{15})', self.raw_text)).__bool__()

    @property
    def is_rubika_private_link(self):
        return (search(r'(rubika\.ir\/join[c,g]\/\w{32})', self.raw_text)).__bool__()

    @property
    def is_chanel_private_link(self):
        return (search(r'(rubika\.ir\/joinc\/\w{32})', self.raw_text)).__bool__()

    @property
    def is_group_link(self):
        return (search(r'(rubika\.ir\/joing\/\w{32})', self.raw_text)).__bool__()

    @property
    def is_rubika_link(self):
        return (search(r'(rubika\.ir\/\w{4,25})', self.raw_text)).__bool__()

    @property
    def is_atsign(self):
        return (search(r'\@\w{4,25}', self.raw_text)).__bool__()

    @property
    def is_url(self):
        return (search(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}|[a-zA-Z0-9]+\.[^\s]{2,})', self.raw_text)).__bool__()
    
    @property
    def is_admin(self):
        return any(user.get('member_guid').__eq__(self.author) for user in SetClient(self.auth).get_group_admin_members(self.object_guid).get('data').get('in_chat_members'))
    
    @property
    def is_user(self):
        return self.action.__eq__('User')
    
    @property
    def is_group(self):
        return self.type.__eq__('Group')

    @property
    def is_channel(self):
        return self.type.__eq__('Channel')

    @property
    def is_private(self):
        return self.type.__eq__('User')
    
    @property
    def is_personal(self):
        return self.is_private
    
    @property
    def is_bot(self):
        return self.type.__eq__('Bot')
    
    @property
    def is_service(self):
        return self.type.__eq__('Service')
    
    @property
    def object_guid(self):
        try:
            return self.find_keys(keys=['group_guid', 'object_guid',
                                        'channel_guid', 'user_guid',
                                        'bot_guid', 'service_guid'])
        except AttributeError:
            pass

    @property
    def author(self):
        try:
            return self.find_keys(keys=['author_object_guid'])

        except AttributeError:
            pass
        
    @property
    def author_object_guid(self):
        try:
            return self.author_object_guid

        except AttributeError:
            pass
    
    def guid_type(self, chat_id: str) -> str:
        if isinstance(chat_id, str):
            return Scanner.check_type(chat_id)
    
    def finder(self, filters) -> (object):
        
        if 'group_guid' in filters:
            return self.group_guid if not 'message' in self.original_update.keys() else self.message.group_guid
        elif 'channel_guid' in filters:
            return self.channel_guid if not 'message' in self.original_update.keys() else self.message.channel_guid
        elif 'user_guid' in filters:
            return self.user_guid if not 'message' in self.original_update.keys() else self.message.user_guid
        elif 'object_guid' in filters:
            return self.object_guid if not 'message' in self.original_update.keys() else self.message.object_guid
        else:
            return self.author_object_guid if not 'message' in self.original_update.keys() else self.message.author_object_guid
    
    def pin(self, chat_id: str = None,
            message_id: str = None) -> (dict):

        return SetClient(self.auth).set_pin_message(chat_id = chat_id or self.find_keys(keys=['object_guid', 'author_object_guid', 'channel_guid', 'group_guid', 'user_guid', 'bot_guid', 'service_guid']), message_id = message or self.message_id, action='Pin')
    
    def unpin(self, chat_id: str = None,
              message_id: str = None) -> (dict):

        return SetClient(self.auth).set_pin_message(chat_id = chat_id or self.find_keys(keys=['object_guid', 'author_object_guid', 'channel_guid', 'group_guid', 'user_guid', 'bot_guid', 'service_guid']), message_id = message or self.meesage_id, action='Unpin')

    def seen(self, chat_id: str = None,
             message: str = None) -> (dict):
        
        return SetClient(self.auth).seen_chats({chat_id or self.find_keys(keys=['object_guid', 'author_object_guid', 'channel_guid', 'group_guid', 'user_guid', 'bot_guid', 'service_guid']): message or self.message_id if not 'message' in self.original_update.keys() else self.message.message_id})
    
    def reply(self, *args, **kwargs) -> (dict):
        
        return SetClient(self.auth).send_message(*args, **kwargs)
    
    def respond(self, text: str, 
                action: str = 'author_object_guid') -> (dict):

        return SetClient(self.auth).send_message(text, self.finder(action), reply_to_message_id=self.message_id if not 'message' in self.original_update.keys() else self.message.message_id)
    
    def send(self, text,
             action: str = 'author_object_guid'):
        return SetClient.send_message(text, self.finder(action))
    
    def edit(self, text: str, chat_id: str = None,
             message_id: str = None, action: str = 'author_object_guid', *args, **kwargs) -> (dict):

        return SetClient(self.auth).edit_message(message_id = message_id or self.message_id, text=text, chat_id = chat_id or self.finder(action), *args, **kwargs)
    
    def forwards(self, to: str,
                 _from: str = None, messages: list = None) -> (dict):
        
        return SetClient(self.auth).forward_messages(_from or self.find_keys(keys=['object_guid', 'author_object_guid', 'channel_guid', 'group_guid', 'user_guid', 'bot_guid', 'service_guid']), messages or [self.message_id], to)
    
    def download(self, chat_id: str = None,
                 message: str = None, name: str = None, *args, **kwargs) -> (dict):

        return SetClient(self.auth).get_file('message' if message else '', True, save_as=name, chat_id = chat_id or self.find_keys(keys=['object_guid', 'author_object_guid', 'channel_guid', 'group_guid', 'user_guid', 'bot_guid', 'service_guid']), message = message or self.find_keys(keys=['messaage_id']))

    def delete(self, chat_id: str = None,
               messages: list = None, action: str = 'object_guid', *args, **kwargs) -> (dict):
        
        return SetClient(self.auth).delete_messages(messages or [self.message_id], chat_id or self.finder(action))

    def save(self, action: str = 'author_object_guid') -> (dict):

            return SetClient(self.auth).forward_messages(self.finder(action), [self.message_id], self.chat_id or self.user_guid)

    def activity(self, chat_id: str = None,
                 action: str = 'author_object_guid') -> (dict):
        return SetClient(self.auth).send_chat_activity(self.finder(action), 'is typing...')


class NewMessage(Client):
    
    def __init__(
        self,
        func        :   object,
        filters     :   list  =   None,
        pattern     :   str   =   None,
        commands    :   dict  =   None, 
        gets        :   tuple =   None,
        handle_name :   str   =   'handshake',
        *args
        ) -> (None):
        
        '''
        ## PARAMS:
            - `filters  = ['u0...', ]`
            - `pattern  = '(?) hi \S+'`
            - `commands = {'/start': 'Hey!'}`
            - `gets     = ('/start', '/info')`
        '''

        super().__init__(func, filters, pattern,
                         commands, gets, handle_name)
        (self.pattern, self.filters, self.gets,
         self.handle_name, self.commands, self.func) = (pattern, filters, gets,
                                                        handle_name, commands, func)


    def builder(self) -> iter:
        
        if not isinstance(self.filters, list):
            self.filters: list = [self.filters]
        
        for message in self.func(self.handle_name, get_messages=True, chat_ids=self.filters):
            
            if self.pattern:
                if not isinstance(self.pattern, str):
                    raise ValueError('oh pattern param is not string type.')
                if search(self.pattern, message.get('text') or message):
                    update = EventBuilder(message)
                    yield update

            elif self.commands:
                
                if not isinstance(self.commands, dict):
                    raise ValueError('oh commands param is not dictionary type.')
                    
                if any(message.get('text').__contains__(cmd) for cmd in list(self.commands.keys())):
                    update = EventBuilder(message)
                    yield update

            elif self.gets:
                
                if not isinstance(self.gets, tuple) or isinstance(self.gets, list):
                    raise ValueError('oh gets param is not a tuple or list type.')
                
                if any(cmd in message for cmd in self.gets):
                    update = EventBuilder(message)
                    yield update

            else:
                update = EventBuilder(message)
                yield update


class Handler(Client):

    def __init__(self, starting: bool = True,
                 *args, **kwargs) -> (None):

        '''
        # Handler | Events


        ## Example:
            from rb import Handler, NewMessage

            with Handler(...) as client:
                client.on(NewMessage(client.handle, handle_name='ChatsUpdates').builder())
                def update(event):
                    pass

        ## Responses:
            - `HandShake`:

                message_updates:

                    {
                        'message_id': ...,
                        'message': {
                            'text': ...,
                            'message_id': ...,
                            'action': ...,
                            'type': ...,
                            'author_object_guid': ..., 
                            },
                        'user_guid': ...,
                        }

                chat_updates:
                    ...

                show_notifications:
                    ...

            - `ChatsUpdates`:
                {
                    'message_id': ...,
                    'text': ...,
                    'author_object_guid' ...,
                    'author_type': ... ,
                    'type': ...
                    }

            - `MessagesUpdates`:
                {
                    'message_id': ...,
                    'text': ...,
                    'author_object_guid' ...,
                    'author_type': ... ,
                    'type': ...
                    }
        '''
        
        super().__init__(starting, *args, **kwargs)
        self.starting = starting

    def __enter__(self):
        return self

    def __exit__(self, *args,
                 **kwargs) -> (None):
        pass

    def __appender(self, msg_id: str = None,
                    action: str = 'edit'):
        
        if action == 'edit':
            if not msg_id in open(self.auth+'-ids.sty', 'r').read():
                open(self.auth+'-ids.sty', 'a+').write(msg_id+'\n')
        else:
            open(self.auth+'-ids.sty', 'w')
    
    def handle(
            self,
            method              :   str                         =   'ChatsUpdates',
            get_chats           :   bool                        =   True,
            get_messages        :   bool                        =   True,
            chat_ids            :   str                         =   None,
            author_guid         :   str                         =   None,
            pattern             :   typing.Union[tuple, list]   =   None,
            show_notifications  :   bool                        =   False
            ) -> (dict):

        '''
        `method`: methods: `ChatsUpdates`, `MessagesUpdates`, `HandShake`
        `get_chats`: the chat updates
        `get_messages`: the message updates
        `chat_ids`: chat filter
        `author_guid`: author_filter
        `pattern`: the pattern is for get message filter: `('^\w{1}start', 'Hey! from rubx lib')`
        '''

        if not method or not isinstance(method, str) or not any(word in method.lower() for word in ('chatsupdates', 'messagesupdates', 'handshake', 'socket')):
            method: str = 'HandShake'

        if (method.lower().__contains__('handshake') or method.lower().__contains__('socket')):

            for msg in self.hand_shake():

                if msg.get('type') == 'messenger':

                    res: dict = msg.get('data')

                    if get_chats and get_messages:
                        if not show_notifications:
                            res.pop('show_notifications')
                        yield res

                    elif get_messages:

                        for i in res.get('message_updates'):

                            if pattern:

                                if not isinstance(pattern, list) or isinstance(pattern, tuple):
                                    raise ValueError('pattern not a tuple or list type.')
        
                                if search(pattern[0], i.get('message').get('text') or ''):
                                    i.update({'pattern': pattern[1]})
                                    yield i
                            else:
                                yield i

                    elif get_chats:
                        for i in res.get('chat_updates'):
                            yield i

                    elif show_notifications:
                        for i in res.get('show_notifications'):
                            yield i

                    else:
                        res.update(res.get('message_updates'))
                        res.update(res.get('chat_updates'))
                        res.update(res.get('show_notifications'))
                        yield res

        elif (method.lower().__contains__('chatsupdates')):

            while (1):
                
                try:
                    for msg in SetClient(self.auth).get_chats_updates().get('data').get('chats'):
                        
                        if not msg.get('last_message').get('message_id') in open(self.auth+'-ids.sty', 'r').read():
                            
                            if chat_ids:
                                
                                if not isinstance(chat_ids, list):
                                    chat_ids: list = [chat_ids]
                                    
                                if msg.get('last_message').get('object_guid') in chat_ids or msg.get('last_message').get('author_object_guid') in chat_ids:
                                    
                                    if pattern:
                                        if search(pattern[0], msg.get('last_message').get('text')):
                                            
                                            msg.update(msg.get('last_message'))
                                            msg.update(msg.get('abs_object') or {})
                                            del msg['last_message']
                                            del msg['abs_object']
                                            msg.update({'pattern': pattern[1]})
                                            
                                            yield msg
                                    else:
                                        
                                        msg.update(msg.get('last_message'))
                                        msg.update(msg.get('abs_object') or {})
                                        del msg['last_message']
                                        del msg['abs_object']
                                        
                                        yield msg
                            else:
                                
                                if pattern and isinstance(pattern, tuple) or isinstance(pattern, list):
                                    if search(pattern[0], msg.get('last_message').get('text')):
                                        
                                        msg.update(msg.get('last_message'))
                                        msg.update(msg.get('abs_object') or {})
                                        msg.update({'pattern': pattern[1]})
                                        del msg['last_message']
                                        del msg['abs_object']
                                        
                                        yield msg
                                else:
                                    
                                    msg.update(msg.get('last_message'))
                                    msg.update(msg.get('abs_object') or {})
                                    del msg['last_message']
                                    del msg['abs_object']
                                    
                                    yield msg
                            
                        self.__appender(msg.get('last_message').get('message_id'), 'edit')
                except Exception:
                    ...

        elif (method.lower().__contains__('messagesupdates')):

            while (1):
                
                try:
                    if chat_ids:
                        
                        if not isinstance(chat_ids, list):
                            chat_ids: list = [chat_ids]
                            
                        for chat_id in chat_ids:
                            for msg in SetClient(self.auth).get_messages_updates(chat_id).get('data').get('updated_messages'):
                                if not msg.get('last_message').get('message_id') in open(self.auth+'-ids.sty', 'r').read().split('\n'):
                                    
                                    if pattern and isinstance(pattern, tuple) or isinstance(pattern, list):
                                        if search(pattern[0], msg.get('last_message').get('text')):
                                            yield [msg.get('last_message'), pattern[1]]
                                    else:
                                        yield msg.get('last_message')
                                
                                self.__appender(msg.get('last_message').get('message_id'), 'edit')
                except Exception:
                    ...

    def hand_shake(self) -> (dict):
        for message in WebSocket(self.auth).connection:
            yield message

    def handler(self, builder: object) -> (typing.Union[object,
                                                        iter, None]):
        
        '''
        ## EXAMPLE:
            
            from rb import Handler, EventBuilder, Filters

            client = Handler(...)
            
            # the funcs: `ChatsUpdates`, `MessagesUpdates`, `HandShake` # websocket
            
            client.add_event_handling(func='HandShake', events=dict(get_messages=True, get_chats=True))
            
            @client.handler
            def update(app: RubikaClient, message: EventBuilder, event):
                ...
        
        '''

        def decorator():

            methods = SetClient(self.auth, return_data_an_dict=False)
            update = Handler(self.auth)
            
            if self.handling.get('events'):
                if not isinstance(self.handling['events'], dict):
                    self.handling.update({'events': dict(get_messages=True, get_chats=True)})
            else:
                self.handling.update({'events': dict(get_messages=True, get_chats=True)})
            if not self.handling.get('func') and isinstance(self.handling.get('func'), str) and self.handling.get('func').lower() in ['handshake', 'chatsupdates', 'messagesupdates']:
                self.handling.update({'func': 'chatsupdates'})
            
            for (event) in (update.handle(method=self.handling.get('func'), **self.handling.get('events') or {})):
                event.update({'auth': self.auth, 'chat_id': self.chat_id or ''})
                message = EventBuilder(event)
                builder(methods, message, event)

        self.__appender(action='create')

        while 1:
            try:
                decorator()
            except Exception:
                pass

    def command_handler(self, func: object,
                        *args, **kwargs): # to handling with custom func

        '''
        from rb import Handler, Filters, Performers

        client = Handler('session')

        def event(message):
            message.respond(message.pattern) # Filters.author - send message to user
        
        client.add_event_handling(Performers.chats_updates, event=dict(get_chats=True, get_messages=True, pattern=(client.regex('/start'), 'Hi from rubx lib.')))
        client.starting = True
        client.command_handler(event)
        '''

        def updater():

            @self.handler
            def update(app, message, event):
                func(message)

        if (self.starting):
            self.__appender(action='create')
            while 1: updater()

    def on(self, event) -> (typing.Union[object, None]):
        
        '''
        ## EXAMPLE:

            from rb import Handler, NewMessage
            
            client = Handler(...)
            
            @client.on(NewMessage(client.handle, handle_name='ChatsUpdates').builder())
            def update(event):
                ...
        
        '''
        
        def decorator(func) -> (None):
            return func

        return decorator

    def add_event_handling(self, **handlers) -> (None):
        # add a handler method and params
        self.handling.update({'func': handlers.get('func') or handlers.get('method'), 'events': handlers.get('events') or handlers.get('event')})
    
    def remove_event_handling(self, func: object):
        try:
            self.handling.pop(func)
        except KeyError:
            ...

    def regex(self, word: str) -> (compile):
        return compile(word)


# to finding all attr's
class Classer(object):

    @classmethod
    def create(cls, name, __base, authorise: list = [],
               exception: bool = True, *args, **kwargs) -> object:

        result = None
        if authorise.__contains__(name):
            result = name

        else:
            attr = difflib.get_close_matches(name, authorise, n=1)

            if attr:
                return getattr(__base[0], attr[0])

            else:
                caller = inspect.getframeinfo(inspect.stack()[2][0])
                warn(
                    f'{caller.filename}:{caller.lineno}: do you mean'
                    f' "{name}", "{result}"? correct it')

        if result.__ne__(None) or not exception:
            if result == None:
                result = name
            # setattr(___base[0], result or name, lambda *args, **kwargs: ...)
            # return getattr(__base[0], name)
            return type(result, __base, {'__name__': result, **kwargs}) # add method to class

        raise AttributeError(f'module has no attribute ({name})')


# main class object to set all method for use.
class RubikaClient(SetClient): # TODO: add all methods
    
    __slots__ = ('SetClient', )
    
    def __init__(self, *args, **kwargs) -> None:
        
        '''
        `# rubika > rub > rb`
        
        `import rb`
        `print(help(rb))`
        
        `from rb import *`
        `with RubikaClient('session', base_logger=__name__) as client:`
            `client.proxy = {'http': '127.0.0.1:9050'}`
            `print(client * 'chat-id')`
        '''

        super().__init__(*args, **kwargs)

    def __getattr__(self, name, *args, **kwargs) -> Classer:
        
        # `note`: for: if you forget the method name
        '''
        from rb import RubikaClient
        
        with RubikaClient('session') as client:
            print(client.getChatInfo(client, 'chat-guid')) # GetChatInfo, GETchatINFO, or ...
        '''

        # for: normally
        '''
        from rb import RubikaClient
        
        with RubikaClient('session') as client:
            print(client.get_chat_info('chat-guid'))
        '''
        
        method = Classer.create(name, (SetClient, ), dir(SetClient))
        
        try:
            return method(*args, **kwargs)
        except Exception:
            return method


# To use the async for methods
# TODO: set handler with async.
class Client(RubikaClient):
    
    __slots__ = ('RubikaClient', )
    
    def __init__(self, *args, **kwargs):

        '''
        from rb import Client

        async def run(*args):
            async with Client(...) as client:
                await client.start(client.send_message, 'Hey! from rubx', 'chat-guid')
        
        Client.run(run)
        '''

        super().__init__(*args, **kwargs)
    
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs) -> (None):
        pass

    async def start(self, method: object, *args, **kwargs) -> (dict):
        '''
        get method func to async
        '''
        return method(*args, **kwargs)
    
    @staticmethod
    def run(func: object, *args) -> (None):
        '''
        run main func to use
        
        func | func()
        -------------
        '''
        
        try:
            __import__('asyncio').run(func())
        except Exception:
            __import__('asyncio').run(func)


class BotAPI(ABC):

    __slots__ = ('self', 'base_logger', 'token',
                 'proxy', 'timeout', 'headers', 'return_data_action')

    def __str__(self) -> str:
        return dumps({'session': SQLiteSession(self.token).information()}, indent=4) if self.token else dumps({'__base_class__': 'BotAPI'})

    def __init__(
        self,
        base_logger         : str = __name__,
        token               : str = None,
        proxy               : dict = {'http': '127.0.0.1:9050'},
        timeout             : int  = 5,
        headers             : dict = None,
        return_data_action  : bool = True
        ) -> None:

        '''
        `with BotAPI(__name__, 'token') as app:`
            `app.send_message('chat-id', 'Hey!')`

        token: is api key
        proxy: to set and config proxy for requests
        headers: to set header
        return_data_action: a boolean type, literal: True, False for return keys to obejct or attrbute or dict ...
        '''

        if isinstance(base_logger, str):
            
            try:
                base_logger = logging.getLogger(base_logger)
            except Exception:
                base_logger = logging.getLogger(__name__)

        if token:

            try:
                open(f'{token}.sty', 'r')
            except FileNotFoundError:
                open(f'{token}.sty', 'w+').write(token)
                database = SQLiteSession(token)
                database.insert(None, token, None, 'https://messengerg2b1.iranlms.ir/v3/')
        else:
            
            try:
                token: str = SQLiteSession(token).information()[1]
            except Exception:
                warn('TokenWarn: please insert bot token')
        
        (self.base_logger, self.token, self.proxy,
         self.headers, self.return_data_action, self.handling) = (base_logger, token, proxy,
                                                   headers, return_data_action, {})
        (Connection.timeout, Connection.proxy,
         Connection.headers, Connection.type) = (timeout or 5, proxy,
                                                 headers, return_data_action)


    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass
    
    @property
    def get_token(self) -> str:
        return self.token


class SetAPIS(BotAPI, BotMethods): ...


class MessageHandler(object):

    def __str__(self) -> (str):
        return dumps(self.result_data, indent=4,
                     ensure_ascii=False, default=str)

    def __getattr__(self, name) -> (list):
        return self.keys_finder(keys=name)

    def __setitem__(self, key, value) -> (None):
        self.result_data[key] = value

    def __getitem__(self, key):
        return self.result_data[key]

    def __lts__(self, update: list) -> (list):
        
        for index, element in enumerate(update):
            if isinstance(element, list):
                update[index] = self.__lts__(update=element)

            elif isinstance(element, dict):
                update[index] = MakeDataKeys(update=element)

            else:
                update[index] = element
        return update

    def __init__(self, update: dict = None) -> (None):
        
        '''
        message finder
        '''
        
        self.result_data = update

    def keys_finder(self, keys: list,
                  result_data: str = None) -> (list):

        if not result_data:
            result_data = self.result_data

        if not isinstance(keys, list):
            keys = [keys]

        if isinstance(result_data, dict):
            for key in keys:
                try:
                    update = result_data[key]
                    if isinstance(update, dict):
                        update = MakeDataKeys(update=update)

                    elif isinstance(update, list):
                        update = self.__lts__(update=update)

                    return update

                except KeyError:
                    pass
            result_data = result_data.values()

        for value in result_data:
            if isinstance(value, (dict, list)):
                try:
                    return self.keys_finder(keys=keys, result_data=value)

                except AttributeError:
                    pass
        else:
            raise KeyError('This value is not found')

    @property
    def raw_text(self):
        return self.keys_finder(['text'])

    @property
    def message_id(self):
        return self.keys_finder(['message_id'])

    @property
    def reply_to_message_id(self):
        return self.keys_finder(['reply_to_message_id'])

    @property
    def chat_id(self):
        return self.keys_finder(['chat_id'])

    def reply(self, text: str) -> typing.Union[str, dict]:
        return SetAPIS(token=self.token).send_message(self.chat_id, text, reply_to_message_id=self.message_id)


# the main class to usage rubika bot api's
class BotAPI(SetAPIS):


    def __init__(self, *args, **kwargs) -> None:
        '''
        bot methods api client
        '''
        
        super().__init__(*args, **kwargs)


    def __getattr__(self, name, *args, **kwargs) -> typing.TypeVar:
        
        # `note`: for: if you forget the method name
        '''
        from rb import BotAPI

        with BotAPI(__name__, 'token') as app:
            print(client.sendMessage(app, 'chat-guid', 'Hey')) # SendMessage, SENDmessage, sendMESSAGE, or ...
        '''

        # for: normally
        '''
        from rb import BotAPI
        
        with BotAPI(__name__, 'token') as app:
            print(app.send_message('chat-guid', 'Hey'))
        '''
        
        method = Classer.create(name, (SetAPIS, ), dir(SetAPIS))
        
        try:
            return method(*args, **kwargs)
        except Exception:
            return method


    def add_event_handling(
        pattern: typing.Union[typing.Tuple[str],
                              typing.List[str]],
        *args,
        **kwargs
        ) -> None:
        
        '''
        `self.add_event_handling(pattern=(r'\w{1}start', 'Hey!'))`
        '''
    
        if not isinstance(pattern, (tuple, list)):
            raise ValueError('The \'pattern\' is invalid, pattern is not a tuple or list')
        else:
            if pattern.__len__() < 2:
                raise IndexError('The \'pattern\' is invalid, len pattern is not 2')

        self.handling.update({'pattern': pattern})


    def handler(self, builder: object, __limit: int = 1) -> None:

        '''
        with BotAPI(__name__, 'token') as app:
            app.add_event_handling(pattern=('\w{1}start', 'Hey!'))
            
            @app.handler
            def update(methods, update, event):
                ...
        
        '''

        def decorator(*args, **kwargs) -> typing.Any:
            
            pattern, methods = None, SetAPIS(token=self.token)
            
            if self.handling.get('pattern'):
                pattern: typing.Union[list, tuple] = self.handling['pattern']
            
            while 1:
                
                for event in self.get_updates(__limit).get('updates'):
                    event.update({'pattern': pattern[1], 'token': self.token})
                    
                    if pattern:
                            update = MessageHandler(event)
                            if re.compile(pattern[0]).search(update.raw_text):
                                builder(methods, update, event)
                    else:
                        update = MessageHandler(event)
                        builder(methods, update, event)

        while 1:
            try:
                decorator()
            except Exception:
                pass


class StartClient(RubikaClient): ...


__all__ = ['Client', 'RubikaClient',
           'RubinoClient', 'WebSocket',
           'Handler', 'NewMessage',
           'EventBuilder', 'Filters',
           'Performers', 'Method', 'Attrs']

__version__ = Version.__version__