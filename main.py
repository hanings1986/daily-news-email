#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
综合信息分析系统
包含国际新闻摘要和竞彩足球分析功能
"""

import sys
import argparse
from datetime import datetime
from scheduler import CombinedScheduler, start_daily_analysis, run_immediate_analysis, run_immediate_news
from config import Config

def main():
    parser = argparse.ArgumentParser(description='综合信息分析系统')
    parser.add_argument('--run-once', action='store_true', help='立即执行一次竞彩足球分析')
    parser.add_argument('--news-once', action='store_true', help='立即执行一次新闻摘要')
    parser.add_argument('--start-service', action='store_true', help='启动定时服务')
    parser.add_argument('--test', action='store_true', help='测试模式')
    parser.add_argument('--test-news', action='store_true', help='测试新闻摘要功能')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🌍 综合信息分析系统")
    print("=" * 60)
    print(f"启动时间: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}")
    print(f"功能: 每日{Config.NEWS_SCHEDULE_TIME.strftime('%H:%M')}自动生成国际新闻摘要")
    print(f"      每日{Config.FOOTBALL_SCHEDULE_TIME.strftime('%H:%M')}自动分析竞彩足球赛事")
    print("=" * 60)
    
    if args.run_once:
        # 立即执行一次竞彩足球分析
        print("\n📊 执行即时竞彩足球分析...")
        run_immediate_analysis()
        
    elif args.news_once:
        # 立即执行一次新闻摘要
        print("\n📰 执行即时新闻摘要...")
        run_immediate_news()
        
    elif args.start_service:
        # 启动定时服务
        print("\n⏰ 启动定时服务...")
        scheduler = start_daily_analysis()
        
        try:
            # 保持主线程运行
            while True:
                command = input("\n输入 'quit' 退出服务: ").strip().lower()
                if command in ['quit', 'exit', 'q']:
                    scheduler.stop_scheduler()
                    print("服务已停止")
                    break
        except KeyboardInterrupt:
            scheduler.stop_scheduler()
            print("\n服务已停止")
            
    elif args.test:
        # 测试模式
        print("\n🧪 测试模式...")
        run_immediate_analysis()
        
    elif args.test_news:
        # 测试新闻摘要模式
        print("\n🧪 测试新闻摘要功能...")
        run_immediate_news()
        
    else:
        # 交互式模式
        print("\n请选择运行模式:")
        print("1. 立即执行一次竞彩足球分析")
        print("2. 立即执行一次新闻摘要")
        print("3. 启动定时服务（推荐）")
        print("4. 测试竞彩足球分析")
        print("5. 测试新闻摘要")
        print("6. 退出")
        
        while True:
            choice = input("\n请输入选择 (1-6): ").strip()
            
            if choice == '1':
                run_immediate_analysis()
                break
            elif choice == '2':
                run_immediate_news()
                break
            elif choice == '3':
                scheduler = start_daily_analysis()
                try:
                    while True:
                        command = input("\n输入 'quit' 退出服务: ").strip().lower()
                        if command in ['quit', 'exit', 'q']:
                            scheduler.stop_scheduler()
                            print("服务已停止")
                            break
                except KeyboardInterrupt:
                    scheduler.stop_scheduler()
                    print("\n服务已停止")
                break
            elif choice == '4':
                run_immediate_analysis()
                break
            elif choice == '5':
                run_immediate_news()
                break
            elif choice == '6':
                print("退出系统")
                break
            else:
                print("无效选择，请重新输入")

if __name__ == "__main__":
    main()