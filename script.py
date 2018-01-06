import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
ad_clicks.groupby('utm_source').user_id.count().reset_index()
print ad_clicks.head()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[False]+clicks_pivot[True])

clicked_A_and_B = ad_clicks.groupby(['is_click','experimental_group']).user_id.count().reset_index()
print(clicked_A_and_B)
clicked_A_and_B_pivot = clicked_A_and_B.pivot(columns='experimental_group',index='is_click',values='user_id')
print clicked_A_and_B_pivot.head()

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print a_clicks.head()
print b_clicks.head()

a_clicks_by_day = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
b_clicks_by_day = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()

a_clicks_by_day_pivot = a_clicks_by_day.pivot(columns='is_click',index='day',values='user_id').reset_index()
b_clicks_by_day_pivot = b_clicks_by_day.pivot(columns='is_click',index='day',values='user_id').reset_index()

a_clicks_by_day_pivot['percent_clicked'] = a_clicks_by_day_pivot[True]/(a_clicks_by_day_pivot[True]+a_clicks_by_day_pivot[False])
b_clicks_by_day_pivot['percent_clicked'] = b_clicks_by_day_pivot[True]/(b_clicks_by_day_pivot[True]+b_clicks_by_day_pivot[False])

print a_clicks_by_day_pivot
print b_clicks_by_day_pivot

#the clicks on both ads fluctuated slightly throughout the week but ad A was clicked on more often than ad B. I recommend that the company use ad A






