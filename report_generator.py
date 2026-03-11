import os
from datetime import datetime
from config import Config

class ReportGenerator:
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_markdown_report(self, analysis_data):
        """生成Markdown格式的报告"""
        filename = Config.get_report_filename()
        filepath = os.path.join(self.output_dir, filename)
        
        content = self._build_report_content(analysis_data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"报告已生成: {filepath}")
        return filepath
    
    def _build_report_content(self, analysis_data):
        """构建报告内容"""
        current_time = datetime.now().strftime('%Y年%m月%d日 %H:%M')
        
        content = f"""# 竞彩足球热门赛事分析报告

**生成时间**: {current_time}  
**数据来源**: {', '.join(Config.DATA_SOURCES.keys())}

---

## 📊 今日热门赛事概览

"""
        
        # 添加赛事表格
        content += self._generate_matches_table(analysis_data)
        
        # 添加详细分析
        content += self._generate_detailed_analysis(analysis_data)
        
        # 添加推荐总结
        content += self._generate_recommendation_summary(analysis_data)
        
        # 添加风险提示
        content += self._generate_risk_notice()
        
        return content
    
    def _generate_matches_table(self, analysis_data):
        """生成赛事表格"""
        table = """
| 联赛 | 对阵 | 比赛时间 | 热度指数 | 媒体共识 |
|------|------|----------|----------|----------|
"""
        
        for match_key, data in list(analysis_data.items())[:Config.MAX_MATCHES]:
            league = data['league']
            match_time = data['match_time']
            hot_index = f"{data['hot_index']}/10"
            consensus = data['consensus']
            
            table += f"| {league} | {match_key} | {match_time} | {hot_index} | {consensus} |\n"
        
        return table + "\n"
    
    def _generate_detailed_analysis(self, analysis_data):
        """生成详细分析"""
        content = """
## 🔍 详细赛事分析

"""
        
        for i, (match_key, data) in enumerate(list(analysis_data.items())[:Config.MAX_MATCHES], 1):
            content += f"### {i}. {match_key} ({data['league']})\n\n"
            content += f"**比赛时间**: {data['match_time']}  
**热度指数**: {data['hot_index']}/10  
**媒体共识**: {data['consensus']}\n\n"
            
            # 各媒体分析
            content += "#### 媒体观点汇总\n\n"
            for media, analysis in data['media_analysis'].items():
                content += f"**{media}**: {analysis}  \n"
            
            # 推荐结果
            content += "\n#### 推荐结果\n\n"
            for bet_type, recommendations in data['recommendations'].items():
                content += f"**{bet_type}**: {', '.join(recommendations)}  \n"
            
            content += "\n---\n\n"
        
        return content
    
    def _generate_recommendation_summary(self, analysis_data):
        """生成推荐总结"""
        content = """
## 💡 投资建议总结

"""
        
        # 统计各类型推荐
        bet_types = {}
        for data in analysis_data.values():
            for bet_type, recommendations in data['recommendations'].items():
                if bet_type not in bet_types:
                    bet_types[bet_type] = []
                bet_types[bet_type].extend(recommendations)
        
        # 生成推荐频率统计
        for bet_type, recommendations in bet_types.items():
            from collections import Counter
            counter = Counter(recommendations)
            
            content += f"### {bet_type}推荐频率\n\n"
            for rec, count in counter.most_common():
                percentage = (count / len(list(analysis_data.values()))) * 100
                content += f"- {rec}: {count}次 ({percentage:.1f}%)\n"
            content += "\n"
        
        return content
    
    def _generate_risk_notice(self):
        """生成风险提示"""
        return """
## ⚠️ 风险提示

1. **投资有风险，入市需谨慎**：本分析仅供参考，不构成投资建议
2. **理性投注**：建议控制投注金额，避免过度投入
3. **多方参考**：建议结合其他分析来源进行综合判断
4. **及时止损**：设定合理的止损点，控制风险
5. **遵守法规**：请遵守当地法律法规，理性参与竞彩

---

*本报告由自动分析系统生成，数据来源于各大体育媒体公开信息*  
*更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    def generate_excel_report(self, analysis_data):
        """生成Excel格式报告（可选功能）"""
        try:
            import pandas as pd
            
            # 准备数据
            data_list = []
            for match_key, data in analysis_data.items():
                row = {
                    '联赛': data['league'],
                    '对阵': match_key,
                    '比赛时间': data['match_time'],
                    '热度指数': data['hot_index'],
                    '媒体共识': data['consensus']
                }
                
                # 添加各媒体分析
                for media, analysis in data['media_analysis'].items():
                    row[f'{media}分析'] = analysis
                
                # 添加推荐结果
                for bet_type, recommendations in data['recommendations'].items():
                    row[f'{bet_type}推荐'] = ', '.join(recommendations)
                
                data_list.append(row)
            
            # 创建DataFrame并保存
            df = pd.DataFrame(data_list)
            excel_filename = Config.get_report_filename().replace('.md', '.xlsx')
            excel_path = os.path.join(self.output_dir, excel_filename)
            
            df.to_excel(excel_path, index=False, engine='openpyxl')
            print(f"Excel报告已生成: {excel_path}")
            return excel_path
            
        except ImportError:
            print("未安装pandas/openpyxl，跳过Excel报告生成")
            return None