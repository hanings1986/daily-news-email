#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
国际新闻摘要生成模块
负责生成格式化的新闻摘要报告
"""

import os
import pandas as pd
from datetime import datetime
from config import Config

class NewsGenerator:
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_markdown_report(self, analysis_data):
        """
        生成Markdown格式的新闻摘要报告
        """
        filename = Config.get_news_report_filename()
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # 报告标题
            f.write(f"# 🌍 国际新闻摘要报告\n\n")
            f.write(f"**生成时间**: {analysis_data['analysis_time']}\n\n")
            
            # 概览统计
            f.write("## 📊 今日新闻概览\n\n")
            f.write(f"- **总新闻数**: {analysis_data['total_news']} 条\n")
            f.write(f"- **平均重要性**: {analysis_data['average_importance']}/10\n")
            f.write(f"- **分析时间**: {analysis_data['analysis_time']}\n\n")
            
            # 类别分布
            f.write("### 📈 新闻类别分布\n\n")
            for category, count in analysis_data['category_distribution'].items():
                f.write(f"- **{category}**: {count} 条\n")
            f.write("\n")
            
            # 来源分布
            f.write("### 📰 新闻来源分布\n\n")
            for source, count in analysis_data['source_distribution'].items():
                f.write(f"- **{source}**: {count} 条\n")
            f.write("\n")
            
            # 重点新闻
            f.write("## 🔥 今日重点新闻\n\n")
            for i, news in enumerate(analysis_data['top_news'], 1):
                f.write(f"### {i}. {news['title']}\n")
                f.write(f"**来源**: {news['source']} | **类别**: {news['category']} | **发布时间**: {news['publish_time']}\n\n")
                f.write(f"**摘要**: {news['summary']}\n\n")
                f.write(f"**重要性**: ⭐{'⭐' * (news['importance'] // 2)}{'☆' if news['importance'] % 2 else ''} ({news['importance']}/10)\n\n")
            
            # 详细新闻列表
            f.write("## 📋 详细新闻列表\n\n")
            f.write("| 序号 | 标题 | 来源 | 类别 | 重要性 | 发布时间 |\n")
            f.write("|------|------|------|------|--------|----------|\n")
            
            for i, news in enumerate(analysis_data['news_list'], 1):
                importance_stars = '⭐' * (news['importance'] // 2) + ('☆' if news['importance'] % 2 else '')
                f.write(f"| {i} | {news['title']} | {news['source']} | {news['category']} | {importance_stars} | {news['publish_time']} |\n")
            f.write("\n")
            
            # 趋势分析
            f.write("## 📈 今日新闻趋势分析\n\n")
            
            # 根据新闻内容分析主要趋势
            international_count = analysis_data['category_distribution'].get('国际新闻', 0)
            finance_count = analysis_data['category_distribution'].get('财经新闻', 0)
            tech_count = analysis_data['category_distribution'].get('科技新闻', 0)
            
            f.write("### 主要关注领域\n\n")
            if international_count > finance_count and international_count > tech_count:
                f.write("🌍 **国际政治局势**是今日主要关注焦点，特别是地缘政治冲突和外交关系发展。\n\n")
            elif finance_count > international_count and finance_count > tech_count:
                f.write("💰 **财经市场动态**是今日主要关注焦点，关注全球经济走势和市场波动。\n\n")
            else:
                f.write("🔬 **科技创新发展**是今日主要关注焦点，关注技术突破和行业趋势。\n\n")
            
            # 重要性分析
            if analysis_data['average_importance'] >= 7:
                f.write("### ⚠️ 高重要性提醒\n\n")
                f.write("今日新闻整体重要性较高，涉及重大国际事件和重要政策变化，建议重点关注。\n\n")
            elif analysis_data['average_importance'] >= 5:
                f.write("### 📢 中等重要性提醒\n\n")
                f.write("今日新闻重要性中等，包含一些重要事件和趋势性内容，建议适当关注。\n\n")
            else:
                f.write("### 📰 常规新闻提醒\n\n")
                f.write("今日新闻以常规报道为主，重要性相对较低，可选择性阅读。\n\n")
            
            # 风险提示
            f.write("## ⚠️ 风险提示\n\n")
            f.write("1. **信息来源多样性**：本报告整合多个新闻源，但信息准确性仍需读者自行判断\n")
            f.write("2. **时效性限制**：新闻信息具有时效性，部分内容可能已经更新或变化\n")
            f.write("3. **观点中立性**：不同媒体可能有不同立场，建议综合参考多方观点\n")
            f.write("4. **投资建议**：本报告不构成任何投资建议，财经信息仅供参考\n\n")
            
            # 报告说明
            f.write("---\n")
            f.write("*本报告由国际新闻摘要系统自动生成，仅供信息参考使用。*\n")
            f.write("*生成时间：{}*\n".format(datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')))
        
        print(f"Markdown格式新闻摘要报告已生成: {filepath}")
        return filepath
    
    def generate_excel_report(self, analysis_data):
        """
        生成Excel格式的新闻摘要报告（可选功能）
        """
        try:
            import pandas as pd
            
            # 创建Excel文件
            filename = Config.get_news_report_filename().replace('.md', '.xlsx')
            filepath = os.path.join(self.output_dir, filename)
            
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                # 新闻详情表
                news_df = pd.DataFrame(analysis_data['news_list'])
                news_df = news_df[['title', 'source', 'category', 'importance', 'publish_time', 'summary']]
                news_df.to_excel(writer, sheet_name='新闻详情', index=False)
                
                # 统计汇总表
                stats_data = []
                for category, count in analysis_data['category_distribution'].items():
                    stats_data.append({'统计类型': '类别分布', '项目': category, '数量': count})
                
                for source, count in analysis_data['source_distribution'].items():
                    stats_data.append({'统计类型': '来源分布', '项目': source, '数量': count})
                
                stats_data.append({'统计类型': '总体统计', '项目': '总新闻数', '数量': analysis_data['total_news']})
                stats_data.append({'统计类型': '总体统计', '项目': '平均重要性', '数量': analysis_data['average_importance']})
                
                stats_df = pd.DataFrame(stats_data)
                stats_df.to_excel(writer, sheet_name='统计汇总', index=False)
                
                # 重点新闻表
                top_news_df = pd.DataFrame(analysis_data['top_news'])
                top_news_df = top_news_df[['title', 'source', 'category', 'importance', 'publish_time', 'summary']]
                top_news_df.to_excel(writer, sheet_name='重点新闻', index=False)
            
            print(f"Excel格式新闻摘要报告已生成: {filepath}")
            return filepath
            
        except ImportError:
            print("警告: 未安装pandas库，无法生成Excel报告")
            print("请运行: pip install pandas openpyxl")
            return None
        except Exception as e:
            print(f"生成Excel报告失败: {str(e)}")
            return None

if __name__ == "__main__":
    # 测试报告生成功能
    from news_collector import NewsCollector
    
    collector = NewsCollector()
    news_data = collector.collect_news_data()
    analysis_result = collector.analyze_news_trends(news_data)
    
    generator = NewsGenerator()
    generator.generate_markdown_report(analysis_result)
    generator.generate_excel_report(analysis_result)