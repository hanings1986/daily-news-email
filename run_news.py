#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接运行新闻摘要功能
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from news_collector import NewsCollector
from news_generator import NewsGenerator

def main():
    print("=" * 60)
    print("🌍 执行国际新闻摘要")
    print("=" * 60)
    
    try:
        # 创建收集器
        collector = NewsCollector()
        print("✓ 新闻收集器创建成功")
        
        # 收集新闻数据
        news_data = collector.collect_news_data()
        print(f"✓ 成功收集 {len(news_data)} 条新闻数据")
        
        # 分析新闻趋势
        analysis_result = collector.analyze_news_trends(news_data)
        print("✓ 新闻趋势分析完成")
        
        # 生成报告
        generator = NewsGenerator()
        markdown_path = generator.generate_markdown_report(analysis_result)
        print(f"✓ Markdown报告生成成功: {markdown_path}")
        
        # 尝试生成Excel报告
        excel_path = generator.generate_excel_report(analysis_result)
        if excel_path:
            print(f"✓ Excel报告生成成功: {excel_path}")
        
        # 显示统计信息
        print("\n📊 新闻摘要统计:")
        print(f"- 总新闻数: {analysis_result['total_news']}")
        print(f"- 平均重要性: {analysis_result['average_importance']}/10")
        print(f"- 类别分布: {analysis_result['category_distribution']}")
        
        print("\n🔥 最重要的3条新闻:")
        for i, news in enumerate(analysis_result['top_news'], 1):
            print(f"{i}. {news['title']} (重要性: {news['importance']}/10)")
        
        print("\n✅ 新闻摘要功能执行成功！")
        
    except Exception as e:
        print(f"❌ 执行失败: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()