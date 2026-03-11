#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
国际新闻数据采集模块
负责从多个新闻源收集最新的国际新闻
"""

import json
import os
import random
from datetime import datetime, timedelta
from config import Config

class NewsCollector:
    def __init__(self):
        self.news_data = []
        
    def get_mock_news(self):
        """
        获取模拟新闻数据（用于演示）
        实际使用时应该替换为真实的数据采集逻辑
        """
        # 模拟国际新闻数据
        international_news = [
            {
                'title': '美伊冲突进入第四天，霍尔木兹海峡航运受阻',
                'source': '新华网国际',
                'category': '国际新闻',
                'summary': '美伊冲突持续升级，伊朗宣布关闭霍尔木兹海峡，全球油价大幅上涨。',
                'importance': 9,
                'publish_time': (datetime.now() - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'http://www.xinhuanet.com/world/2026-03/09/c_1129430000.htm'
            },
            {
                'title': '中俄外长紧急通话，呼吁美伊立即停火',
                'source': '人民网国际',
                'category': '国际新闻',
                'summary': '中国外交部长王毅与俄罗斯外长拉夫罗夫举行紧急通话，一致呼吁立即停止军事行动。',
                'importance': 8,
                'publish_time': (datetime.now() - timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'http://world.people.com.cn/n1/2026/0309/c1002-40123456.html'
            },
            {
                'title': '联合国安理会就美伊局势举行紧急会议',
                'source': '央视新闻',
                'category': '国际新闻',
                'summary': '联合国安理会就美伊冲突召开紧急会议，中俄等国呼吁通过外交途径解决分歧。',
                'importance': 7,
                'publish_time': (datetime.now() - timedelta(hours=6)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'https://news.cctv.com/2026/03/09/ARTI1234567890.shtml'
            },
            {
                'title': '国际油价突破84美元，创年内新高',
                'source': '新浪财经',
                'category': '财经新闻',
                'summary': '受美伊冲突影响，布伦特原油价格单日飙升超过8%，突破84美元/桶。',
                'importance': 8,
                'publish_time': (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'https://finance.sina.com.cn/roll/2026-03-09/doc-ihxyz123456.shtml'
            },
            {
                'title': '全球航运业面临严重冲击',
                'source': '网易财经',
                'category': '财经新闻',
                'summary': '霍尔木兹海峡关闭导致近500艘船舶滞留，航运保险费用大幅上涨。',
                'importance': 7,
                'publish_time': (datetime.now() - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'https://money.163.com/26/0309/12/XYZ123456.html'
            },
            {
                'title': 'AI技术助力国际关系分析',
                'source': '腾讯科技',
                'category': '科技新闻',
                'summary': '人工智能技术在国际关系分析中发挥重要作用，帮助预测地缘政治风险。',
                'importance': 6,
                'publish_time': (datetime.now() - timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'https://tech.qq.com/a/20260309/0123456.htm'
            },
            {
                'title': '欧洲多国呼吁美伊保持克制',
                'source': 'BBC中文',
                'category': '国际新闻',
                'summary': '德国、法国等欧洲国家呼吁美伊双方保持克制，避免局势进一步升级。',
                'importance': 6,
                'publish_time': (datetime.now() - timedelta(hours=7)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'https://www.bbc.com/zhongwen/simp/world-678901234'
            },
            {
                'title': '中东股市大幅波动',
                'source': '华尔街日报中文',
                'category': '财经新闻',
                'summary': '受冲突影响，中东地区主要股市出现大幅波动，投资者避险情绪升温。',
                'importance': 5,
                'publish_time': (datetime.now() - timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'https://cn.wsj.com/articles/SB1234567890'
            }
        ]
        
        # 随机添加一些次要新闻
        secondary_news_templates = [
            {'title': '{}召开国际会议讨论地区安全', 'source': '环球网国际', 'category': '国际新闻'},
            {'title': '{}发布经济数据，显示{}', 'source': '金融时报中文', 'category': '财经新闻'},
            {'title': '{}科技公司发布新产品', 'source': '36氪', 'category': '科技新闻'},
            {'title': '{}国家领导人发表重要讲话', 'source': '人民网国际', 'category': '国际新闻'}
        ]
        
        countries = ['美国', '中国', '俄罗斯', '英国', '法国', '德国', '日本', '韩国']
        economic_terms = ['经济增长稳定', '通胀压力缓解', '就业市场改善', '外贸数据向好']
        companies = ['苹果', '谷歌', '微软', '亚马逊', '特斯拉', 'Meta']
        
        for i in range(7):
            template = random.choice(secondary_news_templates)
            if '{}召开国际会议' in template['title']:
                title = template['title'].format(random.choice(countries))
                summary = f"{random.choice(countries)}主持召开国际会议，讨论地区安全与合作事宜。"
            elif '{}发布经济数据' in template['title']:
                title = template['title'].format(random.choice(countries), random.choice(economic_terms))
                summary = f"{random.choice(countries)}发布最新经济数据，显示{random.choice(economic_terms)}。"
            elif '{}科技公司发布新产品' in template['title']:
                title = template['title'].format(random.choice(companies))
                summary = f"{random.choice(companies)}发布新一代产品，技术创新引领行业发展。"
            else:
                title = template['title'].format(random.choice(countries))
                summary = f"{random.choice(countries)}国家领导人就当前国际形势发表重要看法。"
            
            secondary_news = {
                'title': title,
                'source': template['source'],
                'category': template['category'],
                'summary': summary,
                'importance': random.randint(3, 5),
                'publish_time': (datetime.now() - timedelta(hours=random.randint(10, 24))).strftime('%Y-%m-%d %H:%M:%S'),
                'url': f'https://example.com/news/{random.randint(1000, 9999)}'
            }
            international_news.append(secondary_news)
        
        return international_news
    
    def collect_news_data(self):
        """
        收集新闻数据
        返回按重要性排序的新闻列表
        """
        print("开始收集国际新闻数据...")
        
        # 获取模拟新闻数据
        news_list = self.get_mock_news()
        
        # 按重要性排序
        news_list.sort(key=lambda x: x['importance'], reverse=True)
        
        # 限制最大新闻数量
        news_list = news_list[:Config.MAX_NEWS_ITEMS]
        
        print(f"成功收集 {len(news_list)} 条新闻数据")
        return news_list
    
    def analyze_news_trends(self, news_list):
        """
        分析新闻趋势
        返回分析结果字典
        """
        # 按类别统计
        category_stats = {}
        source_stats = {}
        
        for news in news_list:
            category = news['category']
            source = news['source']
            
            if category not in category_stats:
                category_stats[category] = 0
            category_stats[category] += 1
            
            if source not in source_stats:
                source_stats[source] = 0
            source_stats[source] += 1
        
        # 计算平均重要性
        avg_importance = sum(news['importance'] for news in news_list) / len(news_list)
        
        # 找出最重要的3条新闻
        top_news = sorted(news_list, key=lambda x: x['importance'], reverse=True)[:3]
        
        analysis_result = {
            'total_news': len(news_list),
            'category_distribution': category_stats,
            'source_distribution': source_stats,
            'average_importance': round(avg_importance, 1),
            'top_news': top_news,
            'news_list': news_list,
            'analysis_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return analysis_result
    
    def save_raw_data(self, data, filename):
        """
        保存原始数据到文件
        """
        os.makedirs('data', exist_ok=True)
        filepath = os.path.join('data', filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"原始数据已保存至: {filepath}")

if __name__ == "__main__":
    # 测试新闻采集功能
    collector = NewsCollector()
    news_data = collector.collect_news_data()
    analysis_result = collector.analyze_news_trends(news_data)
    
    print(f"\n新闻分析结果:")
    print(f"总新闻数: {analysis_result['total_news']}")
    print(f"类别分布: {analysis_result['category_distribution']}")
    print(f"平均重要性: {analysis_result['average_importance']}")
    
    print(f"\n最重要的3条新闻:")
    for i, news in enumerate(analysis_result['top_news'], 1):
        print(f"{i}. {news['title']} (重要性: {news['importance']})")