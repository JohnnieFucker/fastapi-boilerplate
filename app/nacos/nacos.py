"""
 @Author  : Shine
 @File    : nacos.py
 @Time    : 2021/11/27 19:52
 "Life is like riding a bicycle. To keep your balance, you must keep moving." - Albert Einstein

                      。
      。               ~!,
     ~*                ~*@:
    !=-                ~:#@
   @;~                  @#
    #&  ...~;=&&&&&&&=!~,
      ,:%%&!:~~~~~::;!*&%%@#,
     .@@~                  !@
     &@#                .~&&
     #@#-.          &%%@&=!   #@@~     =@#;
     .=@@@#&&*!!!;;:~.        @@@.     ,@
        -:;!!*=&%%@@@@@*     ~@@;
                    ,:@@#    &@@&@&* :&#@#. %%       .!%%*.
        -%%-          @@&   .@@!&@@!  *@@-  @@@@@@@ ,@@  @@
        ,&@=       ~*&#:    -@& @@=   &@*  .@@~ @@* :@@&@@@：
          .;=%%#&*:,..      =@  @@.   @@   ;@=  @@  ~@         *:#。
                            @. .@=    @-   &@   @.   @@@@@      .:*#@@@@@&*;-
                           ,#  #@:                                          &#~
                               @@:                                           *#~
                               *@;                              .!          *#~
                                @#                           .-&#@@@@@@@%%&~
                                 !~                        ~;!&%%.

"""
import nacos
from config import AppConfig

app_conf = AppConfig()

client = nacos.NacosClient(
    app_conf.NACOS['nacos_host'], namespace=app_conf.NACOS['nacos_namespace']
)


async def beat():
    client.add_naming_instance(app_conf.NACOS['service_name'], app_conf.NACOS['service_ip'],
                               app_conf.NACOS['service_port'], app_conf.NACOS['service_group_name'])


def register_nacos():
    client.add_naming_instance(app_conf.NACOS['service_name'], app_conf.NACOS['service_ip'],
                               app_conf.NACOS['service_port'], app_conf.NACOS['service_group_name'])
