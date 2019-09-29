# Introduction to Data With Python

## A Brief from Industry

### Pembagian Role dalam Data officer

Umumnya role dalam data officer terbagi menjadi:

1. **Data Engineer**: *pondasi dan infrastruktur data officer*
   - Membuat data pipeline dari berbagai sumber (data lake, support data) dan menyalurkannya ke satu sumber (data warehouse)
   - Mengubah data ke dalam format tertentu
   - Membuat scheduler (program yang berjalan pada waktu/periode tertentu) untuk menarik data
   - Bertanggung jawab dalam mengurus basis data (cloud)
   - Bertanggung jawab untuk memberikan data pendukung bagi Data analyst
   - kuat dalam pemograman, database dan infrastruktur
2. **Data Scientist**: *membuat kebijakan berdasakan data*
   - Mengubah data menjadi sebuah fitur atau metriks
   - Mengembangkan model AI dan menyediakan API
   - Bertanggung jawab atas model yang dirancang
   - Lebih dalam dengan model AI (machine learning & deep learning)
   - kuat dalam statistik, matematika dan AI
3. **Data Analyst**: *partnernya growth dan strategic*
   - Fokus dengan memberikan insight dan rekomendasi dari bisnis
   - Memberikan report dan monitoring (biasanya dalam bentuk dashboard) ke unit bisnis
   - Bertanggung jawab dalam memberikan laporan secara langsung (ad-hoc) ke divisi tertentu
   - Bertanggung jawab untuk meningkatkan kualitas data yang digunakan
   - Kuat dalam statistika, business knowledge, product understanding dan SQL (atau query language lainnya)
4. **Business Intelligence**: *anak panah dari data*
   - Menyelaraskan insight dari data dengan bisnis yang berjalan
   - Memberikan gambaran bagaimana data dapat membantu company
   - Menyediakan data dictionary atau format data sebagai petunjuk untuk stakeholder (software engineer atau data engineer)
   - Memvisualisasikan data
   - Kuat dalam membuat laporan (scripting), visualisasi data, high level business metrics (revenue, gross margin, net profit margin, cost of customer acquisition)
  
Yang jarang

1. Data Storyteller: Melakukan visualisasi data dan bercerita tentang data
2. Qualitative expert: Mengumpulkan dan mengolah data kualitatif (dokumen, suara/audio, video, gambar atau dataset) dan memberikan keputusan

### Tech Stack dalam data officer

> You have two weapons (to analyze data), yourselves and the library

Umumnya teck stack yang digunakan dalam data officer adalah:

1. **Data Engineer**: hadoop, Airflow, Luigi, StackStorm, Oozie, Fluentd/bit, LogStash, Kafka, Redis, cloud service (AWS, GCP), query language, programming language: Elixir, Go, Java, Ruby dan Python
2. **Data Scientist**: Python data Stack: numpy, pandas, matplotlib, family scipy; deep learning stack: tensorflow, keras, pytorch, caffe; stack untuk eksperimen: planout, Ax, botorch, mergexp
3. **Data Analyst**: query language, python data stack + visualization, R stack, tableau, powerBI, redash, superset
4. **Business Intelligence**: query language, python data stack + visualization, R stack, tableau, powerBI, redash, superset

[Roadmap Data Engineering](https://github.com/hasbrain/data-engineer-roadmap)

[Roadmap Data Science # 1](https://towardsdatascience.com/a-road-map-for-data-science-d1977504a72b)

[Roadmap Data Science # 2](https://www.analyticsvidhya.com/blog/2019/01/learning-path-data-scientist-machine-learning-2019/)

[Roadmap Data Analyst # 1](https://study.com/become_a_data_analyst.html)

[Roadmap Data Analyst # 2](https://www.investopedia.com/articles/professionals/121515/data-analyst-career-path-qualifications.asp)

[Roadmap Business Intelligence](https://www.analyticsvidhya.com/blog/2019/01/learning-path-data-scientist-machine-learning-2019/)

## Data Science With Python Core skills

### Data Analysis Technique Intro

Ada beberapa tahap yang perlu dilakukan sebelum melakukan sebuah analisis, yakni melihat dahulu apa-apa yang ada dalam data tersebut antara lain seperti melihat trend, sumber data, keabsahan data, kelengkapan data dan deskripsi dari data. Proses ini biasa disebut dengan EDA, Exploratory Data Analysis. EDA dilakukan untuk melihat apa yang bisa disampaikan oleh data kepada kita.

**Overview dari materi**:

- When to do Exploratory Data Analysis (EDA) and why we do it?
- What are the objectives in doing Exploratory Data Analysis?
- What method are done during EDA?
- What task are done during EDA?

**Mengapa harus melakukan EDA?**:

- EDA is done prior to modelling the predictive analysis or machine learning specific task
- EDA is valuable to data science projects since it allows to get closer to the certainty that the future results will be valid, correctly interpreted, and applicable to the desired business contexts
- Such level of certainty can be achieved only after raw data is validated and checked for anomalies
- EDA also helps to find insights that were not evident or worth investigating to business stakeholders and data scientists but can be very informative about a particular business

**Apakah akibat jika kita melewatkan proses EDA?**:

Such inconsiderate behavior can lead to skewed data, with outliers and too many missing values and, therefore, some sad outcomes for the project:

- generating inaccurate models;
- generating accurate models on the wrong data;
- choosing the wrong variables for the model;
- inefficient use of the resources, including the rebuilding of the model.

**Tujuan dari EDA**:

- Discover Patterns
- Spot Anomalies
- Frame Hypothesis
- Check Assumptions
  
**Yang dilakukan dari EDA**:

- Trends
- Distribution
- Mean
- Median
- Outlier
- Spread measurement (SD)
- Correlations
- Hypothesis testing
- Visual Exploration

**Review Materi**:

- Univariate visualization — provides summary statistics for each field in the raw data set
- Bivariate visualization — is performed to find the relationship between each variable in the dataset and the target variable of interest
- Multivariate visualization — is performed to understand interactions between different fields in the dataset
- Dimensionality reduction — helps to understand the fields in the data that account for the most variance between observations and allow for the processing of a reduced volume of data. Through these methods, the data scientist validates assumptions and identifies patterns that will allow for the understanding of the problem and model selection and validates that the data has been generated in the way it was expected to. So, value distribution of each field is checked, a number of missing values is defined, and the possible ways of replacing them are found.

## Pandas Operation

Adapun operasi dalam pandas yang akan dibahas adalah:

    • Merging columns
    • Merging with indexs
    • Concate Datasets
    • Reshaping Datasets
    • Pivot tables
    • Duplicates analysis in Datasets
    • Mapping in Dataframe
    • Binning of values
    • Observation, filtering and basic analysis
    • Data visualization introduction and introduction to seaborn
    • Histogram visualization
    • Seaborn KDE Plot (Univariates and Multivariates)
    • Plotting multiple charts with seaborn
    • Box plot visualization
    • Regression plot with seaborn
    • Violin plot
    • Heat maps visualization
    • Cluster Maps visualizstion

## Referensi

1. [Rebecca Vickery: data understanding](https://medium.com/@rebecca.vickery)
2. [Geopandas](https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d)
3. [Mapping in Python](https://towardsdatascience.com/mapping-geograph-data-in-python-610a963d2d7f)
