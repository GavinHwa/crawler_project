# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/2/28 18:34'
# @email = 'fengh@asto-inc.com'
from cralwers import jobs, config
import pickle
import logging
import os
from requests import Session
import time


def main():
    """富宝废有色抓取主函数"""
    session = get_f139_session()
    for each_crawler in jobs.all_fys_crawlers:
        try:
            job = each_crawler(session)
            job.run()
            time.sleep(3)
        except Exception as e:
            logging.info("抓取过程中出错了,报错的原因是：{}".format(str(e)))
            continue
    save_cookies(session.cookies)


def get_f139_session():
    """
    获取富宝抓取存入的cookies,
    没有或失效重新登录并更新本地的cookies文件
    """
    session = Session()
    if not os.path.exists('./data'):
        os.makedirs('./data')
    try:
        if not os.path.exists('./data/f139_cookies.config'):
            logging.info("从本地加载cookies失败")
        else:
            with open('./data/f139_cookies.config', 'rb') as f:
                cookies = pickle.load(f)
            # print(cookies, type(cookies))
            logging.info("从本地加载cookies成功")
            session.cookies = cookies
    except FileNotFoundError:
        logging.error("从本地加载cookies失败,原因是：{}".format("FileNotFoundError"))
    except Exception as e:
        logging.error("从本地加载cookies失败,原因是：{}".format(e))
    return session


def save_cookies(web_cookies):
    """存储cookies到本地"""
    if not os.path.exists('./data'):
        os.makedirs('./data')
    try:
        with open('./data/f139_cookies.config', 'wb') as f:
            pickle.dump(web_cookies, f)
    except Exception as e:
        logging.error('存储cookies到本地报错了,原因是:{}'.format(e))


if __name__ == "__main__":
    main()
