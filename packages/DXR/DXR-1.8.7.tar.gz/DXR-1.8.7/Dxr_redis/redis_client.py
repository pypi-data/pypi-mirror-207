# redis连接池
import redis, traceback, sys, time
from loguru import logger
import numpy as np
import cv2
import time


class RedisClient:
    __instance = None

    def __new__(cls, *args, **kwargs):
        # 单例模式
        return cls.__instance or object.__new__(cls)

    def __init__(self, host, port, password=None):
        self.host = host
        self.port = port
        self.redis_conn = None
        try:
            # 拿到一个Redis实例的连接池，避免每次建立、释放连接的开销，节省了每次连接用的时间
            self.POLL = redis.ConnectionPool(host=self.host,
                                             port=self.port,
                                             decode_responses=True,
                                             db=0,
                                             password=password,
                                             max_connections=100)
            logger.info(f'获取Redis连接池, Host={self.host}, Port={self.port}')
        except Exception as e:
            logger.error(f'获取Redis连接池异常, 程序退出:{str(e)},traceback={traceback.format_exc()}')
            sys.exit(0)

    def get_redis_client(self):
        try:
            if self.redis_conn is not None:
                # 从连接池中获取一个连接实例
                self.redis_conn = redis.StrictRedis(connection_pool=self.POLL)
                if self.redis_conn.ping():
                    logger.success(f'获取Redis连接成功, Host={self.host}, Port={self.port}')
                # 清空所有的key
                self.redis_conn.flushall()
            return self.redis_conn
        except Exception as e:
            logger.error(f'Redis连接*异常*:{str(e)},traceback={traceback.format_exc()}')
            # 退出程序
    
            
    def get_redis_data(self, key):
        redis_conn = self.get_redis_client()
        if redis_conn is None:
            return None
        res = redis_conn.get(key)
        redis_out = {'Frame': None, 'bFlag': False, 'error': False, 'iTargetNum': 0, 'rect': [], 'sValue': ''}
        if isinstance(res, str):
            redis_data = eval(res)
            # redis_data.pop('Frame')
            i_type_list = [] # 算法类型
            s_type_list = [] # 算法名称
            if bool(redis_data):
                if redis_data['Frame'] is not None:
                    # 将字节数据转为 numpy 数组
                    nparr = np.frombuffer(redis_data['Frame'], np.uint8)
                    # 将 numpy 数组转为 cv2 图片格式
                    redis_out['Frame'] = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                result=redis_data['Result']
                for algtyep in result:
                    i_type_list.append(algtyep)
                    # print(result[algtyep])
                    s_type_list.append(result[algtyep].get('sType', ''))
                    redis_out['bFlag'] = redis_out['bFlag'] or result[algtyep]['bFlag']
                    redis_out['error'] = redis_out['error'] or result[algtyep]['error']
                    if bool(result[algtyep]['lResults']):
                        res_key = result[algtyep]['lResults'].get('res_key', 'rect')
                        if res_key =='':
                            res_key = 'rect'
                        if res_key != '':
                            redis_out['iTargetNum'] += len(result[algtyep]['lResults'][res_key])
                        redis_out['rect'] = result[algtyep]['lResults'][res_key]
                        redis_out['sValue'] = result[algtyep]['lResults'].get('sValue', '')
                        Value = ''
                        if isinstance(redis_out['sValue'], list) and len(redis_out['sValue'])>0:  # 如果 self.sValue 是一个列表
                            Value = redis_out['sValue'][0]  # 将其转换为字符串并去掉第一层列表嵌套
                            if isinstance(Value, list) and len(Value)>0:  # 如果字符串表示的值是一个列表
                                Value = Value[0]  # 去掉第二层列表嵌套
                        # 判断Value 为小数字符串或整数字符串
                        if Value:
                            redis_out['iTargetNum'] = Value
                redis_out['iType'] = ','.join(i_type_list)
                redis_out['sType'] = ','.join(s_type_list)
        return redis_out



if __name__ == '__main__':
    # 密码
    redis_client = RedisClient('10.10.9.46', 7777, '123456')
    redis_out = redis_client.get_redis_data('cam_rtsp_left')
    print(redis_out)
