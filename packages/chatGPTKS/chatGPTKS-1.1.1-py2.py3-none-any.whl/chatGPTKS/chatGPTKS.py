"""
@Name: chatGPTKS.py
@Auth: MyName
@Date: 2023/5/9-14:37
@Desc: 
@Ver : 0.0.0
"""
import json
import os
import string
import logging

import requests

STATE_OK = 200
logging.basicConfig(level=logging.WARNING)


def readConfig(configPath: string):
    """
    该函数暂时弃用
    输入配置文件的路径，返回json
    Args:
        configPath: 配置文件路径

    Returns:
        json格式

    """
    if not os.path.exists(configPath):
        logging.info("配置文件不存在，将使用config-template.json模板")
        config_path = "./config-template.json"  # TODO 这个需要修理一下
    with open(configPath, "r") as file:
        config = json.load(file)
    logging.debug("json读取成功!")
    return config


def createChatSession():
    """
    创建session，同时把url和初始的data_turbo返回


    Returns:
        session,url,data_turbo:上下文信息

    """

    # url = "http://" + config["base_config"]["ip"] + ":" + config["base_config"]["port"] + config["base_config"]["mode"]
    url = "http://192.168.20.2:8000/completions_turbo"


    #api_key = config["base_config"]["api_key"]
    # api_key = os.environ.get('API_KEY') # TODO 把api_key给封装到环境变量当中去。
    # print(url)

    # 创建一个Session对象
    session = requests.Session()
    #session.headers.update({"api_key": api_key})
    data_turbo = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello i am A"}],
        "max_tokens": 2048,
        "temperature": 0.2,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "top_p": 1.0,
        "stop": ["\nAI:", "\nUser:"]
    }
    logging.debug("创建session成功！")
    return session, url, data_turbo


def sendMessage(user_input: string, session=None, url=None, data_turbo=None, model="gpt-3.5-turbo",
                max_tokens=2048, temperature=0.2, frequency_penalty=0.0, presence_penalty=0.0,
                top_p=1.0, stop=["\nAI:", "\nUser:"]):
    """
    向后端发送信息，把user_input内容添加到data_turbo中实现多轮对话，函数返回发送成功/失败状态，以及AI返回的文本/错误文本
    Args:
        user_input: 用户输入句子
        session: 会话
        url: 接收请求的url地址
        data_turbo: 对话的上下文信息
        model: 选择的模型，可选的有
        max_tokens:返回文本的最大长度
        temperature:温度参数设置，一般在0到1之间，temperature温度值接近 0 时，生成的文本更加确定性和保守，更倾向于选择最高概率的单词或短语。温度值接近 1 时，生成的文本更加随机和创造性，更倾向于从低概率的单词或短语中进行选择。
        frequency_penalty:控制生成文本时对重复内容的惩罚程度,一般在0到1之间，较低的频率惩罚值（如接近 0）会减少对重复内容的惩罚，生成的文本可能会包含更多重复的单词或短语。较高的频率惩罚值（如接近 1）会增加对重复内容的惩罚，生成的文本中重复的单词或短语会更少。
        presence_penalty:控制生成文本时对特定主题或词语出现频率的惩罚程度。一般在0到1之间，较低的存在惩罚值（如接近 0）会减少对特定主题或词语出现频率的惩罚，生成的文本可能会更多地包含与给定主题相关的内容。
较高的存在惩罚值（如接近 1）会增加对特定主题或词语出现频率的惩罚，生成的文本中与给定主题相关的内容会更少。
        top_p:可以控制生成文本时选择的候选词的累积概率阈值。一般在0到1之间。较低的 top_p 值（如 0.1）会限制模型选择的单词范围更为严格，只包括概率分布中最高的 10% 的单词。较高的 top_p 值（如 0.9）会允许更多的候选词被选择，概率分布中更多的单词将被包括在内。
        stop:用于指定生成文本的终止条件。当生成的文本中出现指定的停止词或停止序列时，模型将停止生成文本并返回结果。

    Returns:
        状态值：True表示发送请求成功，并且获得了AI生成的文本
        Text:如果发送请求为True，那么Text的内容为AI生成的本文的内容，否则为错误信息。

    """
    # 返回一个状态值和Text，如果请求成功，那么就返回True和Text,session，否则返回False,错误信息，session
    data_turbo["messages"][-1]["content"] = user_input
    # 发送POST请求
    try:
        response = session.request("POST", url, json=data_turbo)
    except requests.exceptions.ConnectionError:
        return False, "连接失败！请考虑是否是以下原因:\n1)后端未启动；\n2)没有网络；\n3)ip或者port设置错误；\n"

    # 检查响应状态码
    if response.status_code == STATE_OK:
        # 请求成功，处理响应数据
        #print(response.text)
        json_data = json.loads(response.text)
        if "choices" not in json_data:
            return False, json_data["error"]["message"] + ". Error Code: " + str(json_data["code"])
        text = json_data["choices"][0]["message"]["content"]
        # print("AI: " + text)
        data_turbo["model"] = model
        data_turbo["messages"].append(json_data["choices"][0]["message"])
        data_turbo["max_tokens"] = max_tokens
        data_turbo["temperature"] = temperature
        data_turbo["frequency_penalty"] = frequency_penalty
        data_turbo["presence_penalty"] = presence_penalty
        data_turbo["top_p"] = top_p
        data_turbo["stop"] = stop
        return True, text
    else:
        # 请求失败
        # print("POST request failed.")
        # print(response.status_code)
        return False, "POST request failed. Error Code: " + str(response.status_code)
