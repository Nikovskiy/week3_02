import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io
import warnings
import altair as alt
warnings.filterwarnings('ignore')




st.title('Генератор статистических исследований чаевых в ресторане')


uploded_file = st.sidebar.file_uploader(label='Download', type='csv')

@st.cache_data
def load(file):
    return pd.read_csv(file)

if uploded_file is not None:
    tips = load(uploded_file)
    
else:
    st.write('**Загрузите свои данные с систему** (sidebar -> download)')
    st.stop()

if uploded_file is not None:
    if st.sidebar.button('**Исходный датасет**'):
        st.write(tips)

    if st.sidebar.button('**Динамика чаевых во времени**'):
        st.write('**Динамика чаевых во времени**')
        date_range = pd.date_range('2023-01-01', '2023-01-31')
        tips['time_order'] = np.random.choice(date_range, size=len(tips))
        df = tips.groupby('time_order')['tip'].sum().reset_index()
        fig1, ax1 = plt.subplots(figsize=(15, 5))
        sns.scatterplot(data=df, x='time_order', y='tip', ax=ax1)
        st.pyplot(fig1)

        buff = io.BytesIO()
        plt.savefig(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Динамика чаевых во времени')

    if st.sidebar.button('**Гистограмма: Суммарный счет**'):
        fig2, ax2 = plt.subplots(figsize=(15, 5))
        st.write('**Гистограмма: Суммарный счет**')
        sns.histplot(data=tips, x='total_bill', ax=ax2)
        st.pyplot(fig2)

        buff = io.BytesIO()
        plt.savefig(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Гистограмма: Суммарный счет')
        

    if st.sidebar.button('**Гистограмма: Суммарный счет с учетом возраста**'):
        st.write('**Гистограмма: Суммарный счет с учетом возраста**')
        fig3 = sns.displot(data=tips, x='total_bill', col='sex')
        st.pyplot(fig3)

        buff = io.BytesIO()
        plt.savefig(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Гистограмма: Суммарный счет с учетом возраста')

    if st.sidebar.button('**Зависимость сумарый счет/чаевые**'):
        st.write('**Зависимость сумарый счет/чаевые**')
        fig4, ax4 = plt.subplots(figsize=(15, 5))
        sns.scatterplot(data=tips, x='total_bill', y='tip')
        st.pyplot(fig4)

        buff = io.BytesIO()
        plt.savefig(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Зависимость сумарый счет/чаевыe')

    if st.sidebar.button('**Зависимость сумарый счет/чаевые/размер**'):
        st.write('**Зависимость сумарый счет/чаевые/размер**')
        fig5 = alt.Chart(tips).mark_circle(size=60).encode(
            x='total_bill',
            y='tip',
            size='size').interactive()
        st.altair_chart(fig5)

        buff = io.BytesIO()
        fig5.save(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Зависимость сумарый счет/чаевые/размер')

    if st.sidebar.button('**Зависимость между днями неделями и размером счета**'):
        st.write('**Зависимость между днями неделями и размером счета**')
        fig6 = alt.Chart(tips).mark_bar().encode(alt.X('total_bill'), alt.Y('day'))
        st.altair_chart(fig6)

        buff = io.BytesIO()
        fig6.save(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Зависимость между днями неделями и размером счета')

    if st.sidebar.button('**Зависимость между днями неделями и размером счета scatterplot**'):
        st.write('**Зависимость между днями неделями и размером счета scatterplot**')
        fig7 = alt.Chart(tips).mark_circle().encode(x='tip', y='day', color='sex')
        st.altair_chart(fig7)

        buff = io.BytesIO()
        fig7.save(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Зависимость между днями неделями и размером счета scatterplot')


    if st.sidebar.button('**box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)**'):
        st.write('**box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)**')
        df = tips.groupby(['day', 'time'])['total_bill'].sum().reset_index()
        fig8 = alt.Chart(tips).mark_boxplot().encode(x='day', y='total_bill', xOffset='time')
        st.altair_chart(fig8)

        buff = io.BytesIO()
        fig8.save(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)')


    if st.sidebar.button('**Гистограммы чаевых на обед и ланч**'):
        st.write('**Гистограммы чаевых на обед и ланч**')
        fig9 = alt.Chart(tips).mark_bar().encode(
            alt.X('total_bill:Q', bin=alt.Bin(maxbins=20), title='Total Bill'),
            alt.Y('count():Q', title='Count')).properties(
            width=200,
            height=200).facet(
            column='time')
        st.altair_chart(fig9)

        buff = io.BytesIO()
        fig9.save(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Гистограммы чаевых на обед и ланч')

    if st.sidebar.button('**Связь размера счета и чаевых, дополнительно разбитая по курящим/некурящим**'):
        st.write('**Связь размера счета и чаевых, дополнительно разбитая по курящим/некурящим**')
        fig10 = alt.Chart(tips).mark_circle().encode(x='tip', y='total_bill', color='sex').facet(column='smoker:N')
        st.altair_chart(fig10)
        sns.relplot(data=tips, x='tip', y='total_bill', hue='sex', col='smoker')

        buff = io.BytesIO()
        fig10.save(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='Связь размера счета и чаевых, дополнительно разбитая по курящим/некурящим')

    if st.sidebar.button('**HeatMap по всем параметрам**'):
        st.write('**HeatMap по всем параметрам**')
        cor_matrix = tips.corr(numeric_only=True)
        fig11 = plt.figure()
        sns.heatmap(cor_matrix, annot=True)
        st.pyplot(fig11)

        buff = io.BytesIO()
        plt.savefig(buff, format='png')
        st.download_button(label='**Скачать график**', data=buff, file_name='HeatMap по всем параметрам')

    

    
    

   














