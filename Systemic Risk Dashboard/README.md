# systemic-risk-dashboard

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/vsub21/systemic-risk-dashboard/master?filepath=systemic-risk-dashboard.ipynb)

Implementation of dashboard used in "A Data Science Approach to Predict the Impact of Collateralization on Systemic Risk" published in [*From Security to Community Detection in Social Networking Platforms*](https://www.springer.com/gp/book/9783030112851). Link to chapter found [here](http://www.bookmetrix.com/detail/chapter/6b880ca4-a6e4-467e-a3f4-6aec662b7513).

![](https://i.imgur.com/Z1JUT5q.gif)

---

In this paper, we simulate and analyze the impact of financial regulations concerning the collateralization of derivative trades on systemic risk - a topic that has been vigorously discussed since the financial crisis in 2007/08. Experts often disagree on the efficacy
of these regulations. Compounding this problem banks regard their trade data required for a full analysis as proprietary. 

We adapt a simulation technology combining advances in graph theory to randomly generate entire financial systems sampled from realistic distributions with a novel open source risk engine to compute risks in financial systems under different regulations. This allows us to consistently evaluate, predict and optimize the impact of financial regulations on all levels - from a single trade to systemic risk - before it is implemented.

The resulting data set is accessible to contemporary data science techniques like data mining, anomaly detection and visualization. We find that collateralization reduces the costs of resolving a financial system in crisis, yet it does not change the distribution of those costs and can have adverse effects on individual participants in extreme situations.
 
---

This dashboard serves as a front-end for the [Open Source Risk Engine](http://www.opensourcerisk.org/) as a joint venture between the [Columbia Fintech Laboratory](http://fintech.datascience.columbia.edu/) and [Quaternion Risk Management](https://www.quaternion.com/). This was created by [Vivek Subramaniam](https://github.com/vsub21) with mentorship from [Nikolai Nowaczyk](https://github.com/niknow). This dashboard depicts the effects of varying collateralization configurations (IM, VM, and IM/VM) on the trade relations and risk associated with counterparties within financial systems.

An interactive example can be launched via the Binder badge above, and the notebook can be downloaded for personal use and modification as well. 

To use locally:

* Clone the repo and the conda environment: ```conda env create -f environment.yml```

* Activate the environment: ```conda activate fintech-lab36```

* Run the notebook: ```jupyter notebook```
