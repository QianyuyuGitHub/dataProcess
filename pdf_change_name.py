# -*- coding=utf-8 -*-

import os
import re

name_list = ['N112017-00289',
             'N112017-00096',
             'N112017-00072',
             'N112016-00279',
             'N112017-00124',
             'N112017-00109',
             'N112017-00065',
             'N112017-00022',
             'N112017-00154',
             'N112017-00112',
             'N112017-00025',
             'N112016-00264',
             'N112017-00028',
             'N112017-00253',
             'N112017-00252',
             'N112017-00243',
             'N112017-00240',
             'N112017-00203',
             'N112017-00204',
             'N112017-00064',
             'N112016-00243',
             'N112018-00087',
             'N112017-00221',
             'N112017-00225',
             'N112017-00227',
             'N112017-00217',
             'N112017-00228',
             'N112017-00211',
             'N112017-00213',
             'N112017-00214',
             'N112017-00210']
pdf_link_list = ['http://scis.scichina.com/cn/2018/cover1.jpg',
                 'http://scis.scichina.com/cn/2018/contents1.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00289',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00289',
                 'http://scis.scichina.com/cn/2018/N112017-00289.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00096',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00096',
                 'http://scis.scichina.com/cn/2018/N112017-00096.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00072',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00072',
                 'http://scis.scichina.com/cn/2018/N112017-00072.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112016-00279',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112016-00279',
                 'http://scis.scichina.com/cn/2018/N112016-00279.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00124',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00124',
                 'http://scis.scichina.com/cn/2018/N112017-00124.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00109',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00109',
                 'http://scis.scichina.com/cn/2018/N112017-00109.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00065',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00065',
                 'http://scis.scichina.com/cn/2018/N112017-00065.pdf',
                 'http://scis.scichina.com/cn/2018/cover2.jpg',
                 'http://scis.scichina.com/cn/2018/contents2.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00022',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00022',
                 'http://scis.scichina.com/cn/2018/N112017-00022.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00154',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00154',
                 'http://scis.scichina.com/cn/2018/N112017-00154.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00112',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00112',
                 'http://scis.scichina.com/cn/2018/N112017-00112.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00025',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00025',
                 'http://scis.scichina.com/cn/2018/N112017-00025.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112016-00264',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112016-00264',
                 'http://scis.scichina.com/cn/2018/N112016-00264.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00028',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00028',
                 'http://scis.scichina.com/cn/2018/N112017-00028.pdf',
                 'http://scis.scichina.com/cn/2018/cover3.jpg',
                 'http://scis.scichina.com/cn/2018/contents3.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00253',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00253',
                 'http://scis.scichina.com/cn/2018/N112017-00253.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00252',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00252',
                 'http://scis.scichina.com/cn/2018/N112017-00252.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00243',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00243',
                 'http://scis.scichina.com/cn/2018/N112017-00243.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00240',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00240',
                 'http://scis.scichina.com/cn/2018/N112017-00240.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00203',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00203',
                 'http://scis.scichina.com/cn/2018/N112017-00203.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00204',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00204',
                 'http://scis.scichina.com/cn/2018/N112017-00204.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00064',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00064',
                 'http://scis.scichina.com/cn/2018/N112017-00064.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112016-00243',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112016-00243',
                 'http://scis.scichina.com/cn/2018/N112016-00243.pdf',
                 'http://scis.scichina.com/cn/2018/cover4.jpg',
                 'http://scis.scichina.com/cn/2018/contents4.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112018-00087',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112018-00087',
                 'http://scis.scichina.com/cn/2018/N112018-00087.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00221',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00221',
                 'http://scis.scichina.com/cn/2018/N112017-00221.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00225',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00225',
                 'http://scis.scichina.com/cn/2018/N112017-00225.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00227',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00227',
                 'http://scis.scichina.com/cn/2018/N112017-00227.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00217',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00217',
                 'http://scis.scichina.com/cn/2018/N112017-00217.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00228',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00228',
                 'http://scis.scichina.com/cn/2018/N112017-00228.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00211',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00211',
                 'http://scis.scichina.com/cn/2018/N112017-00211.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00213',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00213',
                 'http://scis.scichina.com/cn/2018/N112017-00213.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00214',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00214',
                 'http://scis.scichina.com/cn/2018/N112017-00214.pdf',
                 'http://engine.scichina.com/doi/10.1360/N112017-00210',
                 'https://scholar.google.com.hk/scholar?q=10.1360/N112017-00210',
                 'http://scis.scichina.com/cn/2018/N112017-00210.pdf']

pdf_name_list = ['Website', 'Google Scholar', '新时代 新征程 新使命', 'Website', 'Google Scholar', '社会网络上的观念动力学', 'Website', 'Google Scholar', '康复机器人的人机交互控制方法', 'Website', 'Google Scholar', '利用辅助信息进行矩阵补全的核方法及其在多标记学习中的应用', 'Website', 'Google Scholar', '深度相对度量学习的视觉跟踪', 'Website', 'Google Scholar', '基于三元数极谐–Fourier矩和混沌映射的立体图像零水印算法', 'Website', 'Google Scholar', '基于S3变换的TriBA-Net最短路径路由机制', 'Website', 'Google Scholar', '基于忆阻器模拟的突触可塑性的研究进展', 'Website', 'Google Scholar', '自重构模块化机器人路径规划方法综述', 'Website', 'Google Scholar', '无组织恶意攻击检测问题的研究', 'Website', 'Google Scholar', '点和区间关系的全隐私保密判定', 'Website', 'Google Scholar', '基于D2D的无线多媒体网络编码广播重传策略', 'Website', 'Google Scholar', '双向多天线中继系统中的安全波束成形', 'Website', 'Google Scholar', '结合影子障碍物和ORCA模型的人群仿真方法', 'Website', 'Google Scholar', '基于深度相机的三维人脸迁移', 'Website', 'Google Scholar', '一种鱼眼视频全景拼接中的亮度补偿算法', 'Website', 'Google Scholar', '面向手机网页的大规模WebBIM场景轻量级实时漫游算法', 'Website', 'Google Scholar', 'SDN网络测量技术综述', 'Website', 'Google Scholar', '新一代软件定义体系结构', 'Website', 'Google Scholar', '支持可扩展的在线社交网络数据放置方法', 'Website', 'Google Scholar', '移动通信中基于LCR-DSR技术的信道参数估计算法分析与改进', 'Website', 'Google Scholar', '智能时代的人机交互专刊编者按', 'Website', 'Google Scholar', '智能时代人机交互的一些思考', 'Website', 'Google Scholar', '面向智能时代的人机合作心理模型', 'Website', 'Google Scholar', '实物用户界面 起源、发展与研究趋势', 'Website', 'Google Scholar', '智能时代的人机交互范式', 'Website', 'Google Scholar', '普适计算环境中用户意图推理的Bayes方法', 'Website', 'Google Scholar', '多通道人机交互信息融合的智能方法', 'Website', 'Google Scholar', '面向人类智能增强的多模态人机交互', 'Website', 'Google Scholar', '基于语义三角形的自然人机交互模型', 'Website', 'Google Scholar', '基于Bots的人机交互界面范式']

new_pdf_name_list = []
count = 0
for name in pdf_name_list:
    if (count%3)==2:
        new_pdf_name_list.append(name)
    count += 1
print(new_pdf_name_list)

dir_name = "D:/Downloads/N11201/"

new_pdf_link_list = []
for link in pdf_link_list:
    surfix_search = re.search(r'(.pdf)', link)
    if surfix_search:
        new_pdf_link_list.append(link)
print(new_pdf_link_list)

for _, _, item in os.walk(dir_name):
    for file_name in item:
        file_search = re.search(r'(.*(?=\.pdf))', file_name)
        if file_search.group(0) in name_list:
            index = name_list.index(file_search.group(0))
            os.rename(dir_name + file_name, dir_name + new_pdf_name_list[index]+'.pdf')
        # print(file_search.group(0))

