from io import BytesIO

from dash import html
from wordcloud import WordCloud
from src.utils import encode_image
from src import config
from dash_holoniq_wordcloud import DashWordcloud


# def create_wordcloud():
#     return html.Img(id='wordcloud', className='border-widget')


# def create_wordcloud_image(word_counts):
#     if not word_counts:
#         return ''
#     img = BytesIO()
#     wc = WordCloud(background_color='white', height=config.WORDCLOUD_IMAGE_HEIGHT, width=config.WORDCLOUD_IMAGE_WIDTH, random_state=1)
#     wc.fit_words(word_counts)
#     wc.to_image().save(img, format='PNG')
#     return encode_image(img.getvalue())

def create_wordcloud():
    wordcloud = DashWordcloud(
        id='wordcloud',
        list=[],#group_by_count[['class_name', 'count_in_selection']].values,
        width=config.WORDCLOUD_IMAGE_WIDTH, height=config.WORDCLOUD_IMAGE_HEIGHT,
        gridSize=16,
        backgroundColor='white',
        shuffle=False,
        rotateRatio=0.5,
        shape='square',
        hover=True,
        weightFactor=10
    )