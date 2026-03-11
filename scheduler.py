import schedule
import time
import threading
from datetime import datetime
from data_collector import DataCollector
from report_generator import ReportGenerator
from news_collector import NewsCollector
from news_generator import NewsGenerator
from config import Config

class FootballAnalysisScheduler:
    def __init__(self):
        self.data_collector = DataCollector()
        self.report_generator = ReportGenerator()
        self.is_running = False
        self.scheduler_thread = None
    
    def daily_analysis_task(self):
        """每日竞彩足球分析任务"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始执行竞彩足球分析任务...")
        
        try:
            # 收集数据
            matches = self.data_collector.collect_analysis_data()
            
            # 分析数据
            analysis_data = self.data_collector.analyze_recommendations(matches)
            
            # 生成报告
            report_path = self.report_generator.generate_markdown_report(analysis_data)
            
            # 尝试生成Excel报告
            self.report_generator.generate_excel_report(analysis_data)
            
            # 保存原始数据
            self.data_collector.save_raw_data(analysis_data, f'football_raw_data_{datetime.now().strftime("%Y%m%d_%H%M")}.json')
            
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 竞彩足球分析任务完成，报告已保存至: {report_path}")
            
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 竞彩足球分析任务执行失败: {str(e)}")

class NewsAnalysisScheduler:
    def __init__(self):
        self.news_collector = NewsCollector()
        self.news_generator = NewsGenerator()
        self.is_running = False
        self.scheduler_thread = None
    
    def daily_news_task(self):
        """每日新闻摘要任务"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始执行国际新闻摘要任务...")
        
        try:
            # 收集新闻数据
            news_list = self.news_collector.collect_news_data()
            
            # 分析新闻趋势
            analysis_data = self.news_collector.analyze_news_trends(news_list)
            
            # 生成报告
            report_path = self.news_generator.generate_markdown_report(analysis_data)
            
            # 尝试生成Excel报告
            self.news_generator.generate_excel_report(analysis_data)
            
            # 保存原始数据
            self.news_collector.save_raw_data(analysis_data, f'news_raw_data_{datetime.now().strftime("%Y%m%d_%H%M")}.json')
            
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 新闻摘要任务完成，报告已保存至: {report_path}")
            
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 新闻摘要任务执行失败: {str(e)}")

class CombinedScheduler:
    def __init__(self):
        self.football_scheduler = FootballAnalysisScheduler()
        self.news_scheduler = NewsAnalysisScheduler()
        self.is_running = False
        self.scheduler_thread = None
    
    def setup_schedule(self):
        """设置定时任务"""
        # 每天7:00执行新闻摘要
        schedule.every().day.at(Config.NEWS_SCHEDULE_TIME.strftime('%H:%M')).do(self.news_scheduler.daily_news_task)
        
        # 每天16:45执行竞彩足球分析
        schedule.every().day.at(Config.FOOTBALL_SCHEDULE_TIME.strftime('%H:%M')).do(self.football_scheduler.daily_analysis_task)
        
        # 测试用的定时任务（每分钟执行一次，用于测试）
        # schedule.every(1).minutes.do(self.news_scheduler.daily_news_task)
        # schedule.every(1).minutes.do(self.football_scheduler.daily_analysis_task)
        
        print(f"定时任务已设置:")
        print(f"- 每天 {Config.NEWS_SCHEDULE_TIME.strftime('%H:%M')} 执行国际新闻摘要")
        print(f"- 每天 {Config.FOOTBALL_SCHEDULE_TIME.strftime('%H:%M')} 执行竞彩足球分析")
    
    def run_scheduler(self):
        """运行调度器"""
        self.is_running = True
        self.setup_schedule()
        
        print("综合调度器已启动（包含新闻摘要和竞彩足球分析），按 Ctrl+C 退出")
        
        while self.is_running:
            try:
                schedule.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                print("\n收到中断信号，正在停止调度器...")
                self.stop_scheduler()
                break
            except Exception as e:
                print(f"调度器运行异常: {str(e)}")
                time.sleep(10)  # 异常后等待10秒继续
    
    def start_scheduler_thread(self):
        """在后台线程中启动调度器"""
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            print("调度器已在运行中")
            return
        
        self.scheduler_thread = threading.Thread(target=self.run_scheduler, daemon=True)
        self.scheduler_thread.start()
        print("调度器已在后台线程中启动")
    
    def stop_scheduler(self):
        """停止调度器"""
        self.is_running = False
        print("调度器已停止")
    
    def run_news_once(self):
        """立即执行一次新闻摘要任务"""
        print("立即执行国际新闻摘要任务...")
        self.news_scheduler.daily_news_task()
    
    def run_football_once(self):
        """立即执行一次竞彩足球分析任务"""
        print("立即执行竞彩足球分析任务...")
        self.football_scheduler.daily_analysis_task()
    
    def get_next_run_time(self):
        """获取下一次运行时间"""
        next_run = schedule.next_run()
        if next_run:
            return next_run.strftime('%Y-%m-%d %H:%M:%S')
        return "无定时任务"

# 便捷函数
def start_daily_analysis():
    """启动每日分析服务（包含新闻摘要和竞彩足球分析）"""
    scheduler = CombinedScheduler()
    scheduler.start_scheduler_thread()
    return scheduler

def run_immediate_analysis():
    """立即执行一次竞彩足球分析"""
    scheduler = CombinedScheduler()
    scheduler.run_football_once()

def run_immediate_news():
    """立即执行一次新闻摘要"""
    scheduler = CombinedScheduler()
    scheduler.run_news_once()