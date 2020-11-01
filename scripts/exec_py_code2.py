#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys, subprocess, tempfile, time


def get_pyname(FileNum):
    """
    获得py文件名
    """
    return 'test_%d' % FileNum


def write_file(TempFile, pyname, code):
    """
    接收代码写入文件
    :param TempFile: 文件路径
    :param pyname: 写入的文件名
    :param code: 需要写入的代码
    :return: py文件路径
    """
    py_path = os.path.join(TempFile, '%s.py' % pyname)
    with open(py_path, 'w', encoding='utf-8') as f:
        f.write(code)
    return py_path


def decode(s):
    """
    将py文件返回的结果编码
    :param s: 需编码的内容
    :return: 编码后的内容
    """
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')


def exec_main(code):
    """
    主程序
    :param code: 需要运行的代码
    :return:
    """
    # 创建临时文件夹,返回临时文件夹路径
    TempFile = tempfile.mkdtemp(suffix='_test', prefix='python_')
    # 生成文件名
    FileNum = int(time.time() * 1000)
    # python编译器位置
    EXEC = sys.executable
    # 存放结果
    r = dict()
    pyname = get_pyname(FileNum)
    py_path = write_file(TempFile, pyname, code)
    try:
        outdata = decode(subprocess.check_output([EXEC, py_path],
                            stderr=subprocess.STDOUT, timeout=5))

    except Exception as e:
        r["code"] = 'Error'
        # e.output是错误信息标准输出
        r["output"] = decode(e.output)
        return r
    else:
        # 返回成功的数据
        r["code"] = 'Success'
        r["output"] = outdata
        return r


if __name__ == '__main__':
    code = '''def f(a,b):
    return a+b'''
    print(1)
    print(exec_main(code)['output'])