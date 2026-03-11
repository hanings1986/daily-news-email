import os
from datetime import time

class Config:
    # 定时任务配置
    FOOTBALL_SCHEDULE_TIME = time(16, 45)  # 每天16:45执行竞彩足球分析
    NEWS_SCHEDULE_TIME = time(7, 0)       # 每天7:00执行新闻摘要
    
    # 竞彩足球数据源配置
    FOOTBALL_DATA_SOURCES = {
        '腾讯体育': 'https://sports.qq.com/football/',
        '网易体育': 'https://sports.163.com/football/',
        '新浪体育': 'https://sports.sina.com.cn/football/',
        '虎扑体育': 'https://bbs.hupu.com/soccer'
    }
    
    # 新闻数据源配置
    NEWS_DATA_SOURCES = {
        '国际新闻': {
            '新华网国际': 'http://www.xinhuanet.com/world/',
            '人民网国际': 'http://world.people.com.cn/',
            '环球网国际': 'https://world.huanqiu.com/',
            '央视新闻': 'https://news.cctv.com/world/',
            'BBC中文': 'https://www.bbc.com/zhongwen/simp',
            '路透中文': 'https://cn.reuters.com/',
            '华尔街日报中文': 'https://cn.wsj.com/',
            '金融时报中文': 'https://www.ftchinese.com/'
        },
        '财经新闻': {
            '新浪财经': 'https://finance.sina.com.cn/',
            '网易财经': 'https://money.163.com/',
            '腾讯财经': 'https://finance.qq.com/',
            '东方财富': 'https://www.eastmoney.com/'
        },
        '科技新闻': {
            '新浪科技': 'https://tech.sina.com.cn/',
            '腾讯科技': 'https://tech.qq.com/',
            '网易科技': 'https://tech.163.com/',
            '36氪': 'https://www.36kr.com/'
        }
    }
    
    # 输出配置
    OUTPUT_DIR = 'reports'
    FOOTBALL_REPORT_FILENAME = '竞彩足球分析报告_{date}.md'
    NEWS_REPORT_FILENAME = '国际新闻摘要_{date}.md'
    
    # 分析配置
    HOT_MATCH_THRESHOLD = 5  # 热门赛事讨论数阈值
    MAX_MATCHES = 10  # 最大显示赛事数量
    MAX_NEWS_ITEMS = 15  # 最大新闻条目数量
    
    # 请求配置
    REQUEST_TIMEOUT = 30
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    
    @staticmethod
    def get_football_report_filename():
        """生成竞彩足球报告文件名"""
        from datetime import datetime
        date_str = datetime.now().strftime('%Y%m%d')
        return Config.FOOTBALL_REPORT_FILENAME.format(date=date_str)
    
    @staticmethod
    def get_news_report_filename():
        """生成新闻摘要报告文件名"""
        from datetime import datetime
        date_str = datetime.now().strftime('%Y%m%d')
        return Config.NEWS_REPORT_FILENAME.format(date=date_str)