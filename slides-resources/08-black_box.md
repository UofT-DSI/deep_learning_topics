---
marp: true
theme: uncover
_class: invert
paginate: true

style: |
    img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }

---
<style>
    p {
        text-align: left;
        font-size: 30px
    }
    ul {
        margin: 0;
        font-size: 30px;
    }
    table {
        font-size: 30px;
    }
    ol {
        margin: 0;
        font-size: 30px;
    }
    blockquote {
        border-left: 10px solid #ccc;
        margin: 1.5em 10px;
        padding: 0.5em 30px;
        quotes: "\201C""\201D""\2018""\2019";
    }

    blockquote:before {
        color: #ccc;
        content: none;
        font-size: 4em;
        line-height: 0.1em;
        margin-right: 0.25em;
        vertical-align: -0.4em;
    }

    blockquote:after{
        content: none;
        font-size: 4em
    }
    img {
        width: 100%;
        height: auto;
        margin-left: auto;
        margin-right: auto;
    }
    figcaption {
        font-size: 15px;
        text-align: center;
    }
</style>
# **Black Box Model Explainability**
```console
Data Sciences Institute
Topics in Deep Learning
```

---

##### **Outline**

- Black box models
- Local methods
    - SHAP
    - LIME
- Global methods
    - Global surrogate models
    - HRT

---

<!--_color: white -->
<!--_backgroundColor: #f4a534 -->
## `Black Box Models`

---
#### **Complexity vs interpretability**

- Trained DL models are capable of modeling highly complex, non-linear relationships
    - This is partly due to their sheer size (sometimes billions of parameters) and their use of both linear and nonlinear functions

<br/>

- By the same token, well performing models are a sort of "black box": we know they work, but we don't know how
    - Unlike simpler models like linear regression, understanding how black box models arrive at their predictions can be challenging

---
#### **Challenges of black box models**

- **Lack of transparency**: how do models generate their predictions?
<br/>
- **Poor interpretability**: given a certain input, why was a particular prediction made?
<br/>
- **Trust issues**: stakeholders may find it challenging to trust a well-performing model that they cannot understand
<br/>
- **Accountability issues**: if a black box model's behaviour results in serious issues such as death, who should be held accountable?

---

#### **Importance of explainability**

- Explainability is crucial for models deployed in high-stakes environments such as healtchare
<br/>
- The more we understand a model, the more we can:
    - Build trust among stake-holders
    - Foster ethical AI practices
    - Ensure regulatory compliance
    - Facilitate and contextualise model debugging and improvement

---

#### **Lesson objective**

- Explore different methods for understanding how complex, non-linear models work

<br/>

---

<!--_color: white -->
<!--_backgroundColor: #f4a534 -->
## `Local Methods`

---

![Local_Explainability](images/local_explainability.png)

---

#### **Understanding individual predictions**

- **Local explainability methods** offer insights into individual predictions made by black box models
    - They focus on explaining why a particular prediction was made for a specific instance or region of the input space

---

#### **Why does it matter?**

- DL models are trained on datasets that may not be representative of the entire population
    - If the training data contains biases, such as overrepresentation or underrepresentation of certain demographic groups, these biases can be learned by the model
<br/>
- Understanding why a model behaves differently for each individual or subgroup can help stakeholders identify and address algorithmic bias and unintended behaviours

---

#### **Methodological approaches**
In this lesson, we will go over two different approaches for local explainability:
<br/>

**1. Variable attribution (SHAP)**: how does an individual prediction differ from the average, and how can this difference be attributed among the input variables?
<br/>

**2. Surrogate models of behaviour (LIME)**: can we model black box behaviour locally using an easy to interpret white box model?
<br/>

---

<!--_color: white -->
<!--_backgroundColor: #f4a534 -->
## `Variable Attribution: SHAP`

---

#### **SHapley Additive exPlanations (SHAP)**

- SHAP is a method for explaining the output of machine learning models by quantifying the contribution of each feature to the prediction

<br/>

- This is based on the concept of Shapley values from cooperative game theory: given a set of players (features), how do we distribute the payout (prediction) resulting from a collaborative game (prediction task) 
---

#### **Calculating variable contribution**

- SHAP considers all possible subsets of features, known as coalitions, for a given instance
    - Each coalition represents a different combination of features
<br/>

- For each feature value within a coalition, SHAP calculates its marginal contribution by comparing model predictions with and without the feature value included in the coalition
    - This captures how much the inclusion of that feature value changes the prediction
<br/>

- The Shapley value for each feature value is computed as the **average of its marginal contributions** across all possible coalitions

---

#### **Calculating variable contribution**

- Consider a model predicting risk of heart disease based on **age, cholesterol levels, and smoking status**

- SHAP generates all possible combinations of these features, ranging from no features to all three features included in the coalition

- For each feature value within a coalition, SHAP calculates its marginal contribution by comparing model predictions with and without that feature value included
    - For instance, it measures how much adding the cholesterol level feature to a coalition changes the model's prediction compared to when it's absent

<br/>

--- 
#### **Interpreting SHAP values**

- **Sign**: positive SHAP values indicate that a feature value increases the prediction, while negative values indicate a decrease

- **Magnitude**: the magnitude of the SHAP value represents the importance or impact of that feature value on the prediction

- **Additive property**: the sum of SHAP values across all features equals the difference between instance and average predictions

- **Visual interpretation**: SHAP values can be visualized using various plots, such as the waterfall plot, which displays how individual feature values push the prediction of an instance away from the average value

---

#### **SHAP waterfall plot: predicting the number of rings in an abalone shell**

![SHAP_waterfall_plot](images/SHAP_waterfall.png)

---

#### **Limitations of SHAP**

- **Computationally expensive**: considering all coallitions can be computationally intensive, especially in complex contexts
- **Assumption of independence**: considering all possible coallitions equally may does not reflect feature interdependence, which indicate that certain coallitions are more likely than others in real life
- **Potential misinterpretation**: Users may sometimes misinterpret SHAP values, assuming causality or feature importance and producing false conclusions 

---

<!--_color: white -->
<!--_backgroundColor: #f4a534 -->
## `Surrogate models: LIME`

---

#### **Local Interpretable Model-agnostic Explanations (LIME)**

- LIME is a technique for explaining individual predictions of black box machine learning models at a local level

<br/>

- It approximates the behavior of the black box model by training interpretable surrogate models on perturbed instances around the prediction of interest

<br/>

- LIME provides insights into why a specific prediction was made by highlighting the contribution of different features for that instance

<br/>

---

#### **Mechanistic overview**

 Given an original instance of interest, LIME does the following:

 1. Sample multiple new instances around the original neighbourhood
 2. Weight each new instance according to their proximity to the original
 3. Train a simple, interpretable model (such as linear regression) on the neighbourhood data
 4. Explain the original instance's prediction by interpreting the surrogate model

---

![LIME](images/LIME.png)

---

#### **Limitations of LIME**

- **No single correct way of defining a neighbourhood**: the reweighing function used for new sampled instances based on their distance from the original is variable and can have important impacts in downstream results

- **Generation of unlikely samples**: sampling a neighbourhood by using a normal distribution around the instance of interest may generate samples that wouldn't exist in real data, leading to surrogate models that do not adequately represent the real underlying data distribution

- **Model dependence**: interpretability results heavily depend on the choice of both the black box model and the surrogate model

---

<!--_color: white -->
<!--_backgroundColor: #f4a534 -->
## `Global Methods`

---

![Global_Explainability](images/global_explainability.png)

---

##### **Understanding overall model behaviour**

- **Global explainability methods** offer insights into average model behaviour and general data characteristics

---

##### **Why does it matter?**

- Global explainability enhances our general understanding of a model's decision-making process across an entire dataset, enhancing methodological transparency and increasing trust amongst stakeholders
<br/>

- It also facilitates model debugging and improvement by identifying unexpected behaviours and potential areas of improvement, such as feature selection

---

##### **Methodological approaches**
In this lesson we will go over two different global explainability approaches:

- **Global surrogates**

- **Holdout Randomization Test (HRT)**

---

<!--_color: white -->
<!--_backgroundColor: #f4a534 -->
## `Global Surrogates`

---

##### **Global surrogate models**

- A global surrogate is a simple, interpretable model (e.g., linear regression or decision tree) trained to approximate the predictions of a black box model
    - We are using simple machine learning to model the behaviour of more complex DL algorithms

---

##### **Basic principle**
A global surrogate model can be obtained and interpreted as follows:
1. Define a dataset $X$
2. Obtain prediction outputs of $X$ using the black box model
3. Select and train an interpretable model using $X$ as input and the black box predictions as output
4. Measure how closely the predictions of both models align
5. Interpret the surrogate model (e.g., which features have the most important coefficients in linear regression)
<br/>

---

![global_surrogate_models](images/global_surrogate.png)

---
##### **Limitations**

- **Misinterpretation**: the insights gained from global surrogate models are related to model behaviour, **NOT** to the characteristics of the data itself
- **Susceptibility to choice of training data for surrogate model**: the surrogate model can be trained in any data of similar distribution to that used by the black box model in training. It can happen that surrogate models can model black box behaviour better for some data subsets than others
- **How good is good enough?**: there are no clear rules to determine how similar the surrogate model predictions have to be to its black box counterpart to be considered an acceptable approximation of behaviour

---

<!--_color: white -->
<!--_backgroundColor: #f4a534 -->
## `Holdout Randomization Test`

---
##### **Holdout Randomization Test (HRT)**

- Given a trained model and a held out test set, HRT repeatedly evaluates model performance on the test set following individual feature perturbations
    - Measuring the impact of these perturbations on model predictions serves as a proxy of overall feature importance
<br/>

- These measures provide insights into feature interactions and overall model behaviour

---

##### **HRT algorithm**

Given a trained model and a test set HRT can be implemented as follows:

1. Compute baseline performance on the test set
2. For each feature in the test set:
    - Shuffle the feature of interest
    - Evaluate test set performance following this shuffle
    - Repeat this process multiple times to generate a distribution of performance given the shuffled feature
    - Compute a test statistic to determine whether or not the disturbance of this feature led to worse test set performance

---

##### **Interpreting HRT results**

- At a high level, HRT conducts a conditional independece test for each feature $X_j$, with the null hypothesis stating that an outcome $y$ is independent of feature $X_j$ given all other features
<br/>

- Intuitively, if $X_j$ is predictive of $y$, perturbing this feature in isolation will break down its relationship to $y$ and lead to drops in performance

---

![HRT](images/HRT.png)

---

##### **Limitations of HRT**

- **Sensitivity to test set size**: effectiveness of HRT may vary depending on the size of the holdout set, with smaller holdout sets potentially leading to less reliable assessments of feature importance

- **Limited interpretability**: while HRT provides insights into feature importance stability, it may not offer detailed explanations for why certain features are deemed important or how they contribute to model prediction

- **Assumption of echangeability**: HRT assumes that feature values are exchangeable, which may not hold true in all datasets, potentially leading to biased assessments of feature importance
    - The act of shuffling features in isolation may introduce unrealistic data upon which feature importance is calculated
---

##### **References**

(1) Molnar, C. (2022). Interpretable Machine Learning:
A Guide for Making Black Box Models Explainable (2nd ed.). [Available online](christophm.github.io/interpretable-ml-book/)

(2) A Data Odyssey. (2023, March 20). SHAP with Python (Code and Explanations) [Video]. YouTube. https://www.youtube.com/watch?v=L8_sVRhBDLU

(3) Tansey, W., Veitch, V., Zhang, H., Rabadan, R., & Blei, D. M. (2018, November 1). The Holdout randomization test for feature selection in black box models. arXiv.org. [Available online](https://arxiv.org/abs/1811.00645)

(4) Spector, A., & Janson, L. (2020, November 30). Powerful knockoffs via minimizing reconstructability. arXiv.org. [Available online](https://arxiv.org/abs/2011.14625)

