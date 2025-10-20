# !/usr/bin/env python3
"""xtlog基本用法示例。

本示例展示了xtlog库的基本用法，包括：
- 基本日志记录
- 不同级别的日志
- 设置日志级别
- 异常捕获

Author: sandorn sandorn@live.cn
Github: http://github.com/sandorn/xtlog
"""

from __future__ import annotations

from xtlog import mylog


def basic_logging():
    """基本日志记录示例"""
    print('\n基本日志记录示例...\n')

    # 记录不同级别的日志
    mylog.debug('这是一条调试日志')
    mylog.info('这是一条信息日志')
    mylog.success('这是一条成功日志')
    mylog.warning('这是一条警告日志')
    mylog.error('这是一条错误日志')
    mylog.critical('这是一条严重错误日志')

    # 直接调用日志实例
    mylog('这是直接调用的第一条日志', '这是直接调用的第二条日志')


def set_log_level_example():
    """设置日志级别示例"""
    print('\n设置日志级别示例...\n')

    # 查看当前配置
    config = mylog.get_config()
    print(f'当前日志级别: {config["level"]}')

    # 设置日志级别为WARNING
    print('将日志级别设置为 WARNING')
    mylog.set_level('WARNING')

    # 此时只有WARNING及以上级别的日志会被记录
    mylog.debug('这条调试日志不会显示')
    mylog.info('这条信息日志不会显示')
    mylog.warning('这条警告日志会显示')
    mylog.error('这条错误日志会显示')

    # 恢复日志级别为DEBUG
    print('将日志级别恢复为 DEBUG')
    mylog.set_level('DEBUG')

    # 验证日志级别已恢复
    mylog.debug('现在调试日志可以显示了')


def exception_handling():
    """异常处理示例"""
    print('\n异常处理示例...\n')

    try:
        # 可能引发异常的代码
        return 1 / 0
    except Exception as e:
        # 使用xtlog记录异常
        mylog.exception(f'发生异常: {e!s}')


def main():
    """主函数，演示xtlog的基本用法"""
    # 1. 基本日志记录
    basic_logging()

    # 2. 设置日志级别
    set_log_level_example()

    # 3. 异常处理
    exception_handling()

    print('\nxtlog基本用法演示完成！')


if __name__ == '__main__':
    main()
