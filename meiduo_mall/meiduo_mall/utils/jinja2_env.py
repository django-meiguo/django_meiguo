from jinja2 import Enviroment


def jinja2_environment(**option):
    '''
    jinja2环境
    :param option: 
    :return: 
    '''
    # 创建环境对象
    env = Enviroment(**option)
    # 自定义语法
    # {{static('静态文件相对路径')}},{{url('路由的命名空间')}}
    # 返回环境对象
