import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

result = pd.read_csv('result1124.csv')

tags = result.Tags.values
score = result.Score.values
ans_count = result.AnswerCount.values
view_count = result.ViewCount.values
favor_count = result.FavoriteCount.values

#select valid score evaluated by no less than 3 people
Score_cnt = result.groupby('Score').size().reset_index(name='cnt')
valid_score = Score_cnt[Score_cnt.cnt>=3]['Score']
valid_result=result.merge(valid_score,on='Score')


ACount_Score = valid_result.groupby('Score')['AnswerCount'].agg('mean')
VCount_Score = valid_result.groupby('Score')['ViewCount'].agg('mean')


#select valid wait time over than 0
valid_waittime = result[result.TimeWaited>0]
TW_TVC = valid_waittime.groupby('TitleVerbCount')['TimeWaited'].agg('mean')


#Real Reputation vs Score plot
#TimeWaited vs RealReputation plot
#ViewCount vs TitleVerbCount plot
#AnswerCount vs TimeWaited plot
Score_Reputation = result.groupby('Score')['RealReputation'].agg('mean')
Reputation_TW = valid_waittime.groupby('RealReputation')['TimeWaited'].agg('mean')
TVC_VC = valid_waittime.groupby('TitleVerbCount')['ViewCount'].agg('mean')
TW_Acount = valid_waittime.groupby('TimeWaited')['AnswerCount'].agg('mean')


#All plot
plt.subplot(2,1,1)
ACount_Score.plot()
plt.ylabel('AnswerCount')
plt.subplot(2,1,2)
VCount_Score.plot()
plt.ylabel('ViewCount')
plt.show()

TW_TVC.plot()
plt.ylabel('TimeWaited /h')
plt.show()

Score_Reputation.plot()
plt.ylabel('Real Reputation')
plt.title('Real Reputation vs Score plot')
plt.show()

Reputation_TW.plot()
plt.ylabel('TimeWaited /h')
plt.title('TimeWaited vs RealReputation')
plt.show()

TVC_VC.plot()
plt.ylabel('ViewCount')
plt.title('ViewCount vs TitleVerbCount')
plt.show()

TW_Acount.plot()
plt.ylabel('AnswerCount')
plt.title('AnswerCount vs TimeWaited')
plt.show()
