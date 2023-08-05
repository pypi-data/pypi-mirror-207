## CSV-Similarity

### Intro

A toolkit to get or remove similar items from the csv file

### Example

```python
from csv_similarity.similarity import *

get_similar(
    input_path=f'data/list_company_news1.csv',
    similarity=0.8,
    save_path=f'data/similarity_report1.csv',
    # stopwords_path=f'{root_path}/stopwords/stopwords',
    stopwords_path='',
    analyze_field='title'
)

remove_similar(
    similarity_report_path=f'data/similarity_report1.csv',
    input_csv_path=f'data/list_company_news1.csv',
    output_path=f'data/list_company_news_without_similar.csv',
)

```

### License

The `csv-similarity` toolkit is developed by [Donghua Chen](https://github.com/dhchenx). 