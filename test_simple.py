# 简单测试脚本
print("开始测试新闻摘要功能...")

# 导入模块
try:
    from news_collector import NewsCollector
    from news_generator import NewsGenerator
    print("模块导入成功")
    
    # 测试收集器
    collector = NewsCollector()
    news_data = collector.collect_news_data()
    print(f"收集到 {len(news_data)} 条新闻")
    
    # 测试分析器
    analysis_result = collector.analyze_news_trends(news_data)
    print("新闻分析完成")
    
    # 测试生成器
    generator = NewsGenerator()
    report_path = generator.generate_markdown_report(analysis_result)
    print(f"报告生成成功: {report_path}")
    
    print("✅ 新闻摘要功能测试成功！")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")
    import traceback
    traceback.print_exc()